package noin.vehiclemaintenance.ui.screens

import android.content.Intent
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.PictureAsPdf
import androidx.compose.material.icons.filled.Share
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.core.content.FileProvider
import noin.vehiclemaintenance.data.repository.VehicleRepository
import noin.vehiclemaintenance.ui.components.NoinButton
import noin.vehiclemaintenance.ui.theme.*
import noin.vehiclemaintenance.util.DossierPdfGenerator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.util.Locale

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DossierExportScreen(
    vehicleId: String,
    repository: VehicleRepository,
    onNavigateBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()

    val vehicle by repository.getVehicle(vehicleId).collectAsState(initial = null)
    val logs by repository.getLogsForVehicle(vehicleId).collectAsState(initial = emptyList())

    var isGenerating by remember { mutableStateOf(false) }
    var shareFileUri by remember { mutableStateOf<android.net.Uri?>(null) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Buyer Resale Dossier",
                        color = TkText,
                        fontSize = 18.sp,
                        fontWeight = FontWeight.Bold
                    )
                },
                navigationIcon = {
                    IconButton(onClick = onNavigateBack) {
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                            contentDescription = "Back",
                            tint = TkText
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = TkBg)
            )
        },
        containerColor = TkBg,
        modifier = modifier
    ) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
                .padding(20.dp),
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            Column {
                // Dossier Mockup Card
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clip(RoundedCornerShape(16.dp))
                        .background(TkSurfaceCard)
                        .border(1.dp, TkBorder, RoundedCornerShape(16.dp))
                        .padding(24.dp)
                ) {
                    Column(horizontalAlignment = Alignment.CenterHorizontally) {
                        Box(
                            modifier = Modifier
                                .size(64.dp)
                                .clip(RoundedCornerShape(16.dp))
                                .background(TkSurfaceElevated),
                            contentAlignment = Alignment.Center
                        ) {
                            Icon(
                                imageVector = Icons.Default.PictureAsPdf,
                                contentDescription = null,
                                tint = TkAccent,
                                modifier = Modifier.size(36.dp)
                            )
                        }

                        Spacer(modifier = Modifier.height(16.dp))

                        Text(
                            text = "${vehicle?.year ?: ""} ${vehicle?.make ?: ""} ${vehicle?.model ?: ""}",
                            color = TkText,
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Bold
                        )

                        Spacer(modifier = Modifier.height(4.dp))

                        Text(
                            text = "Official Maintenance History Dossier",
                            color = TkAccent,
                            fontSize = 13.sp,
                            fontWeight = FontWeight.Medium
                        )

                        Spacer(modifier = Modifier.height(20.dp))

                        HorizontalDivider(color = TkBorder)

                        Spacer(modifier = Modifier.height(16.dp))

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text("Total Documented Records", color = TkTextMuted, fontSize = 13.sp)
                            Text("${logs.size}", color = TkText, fontSize = 13.sp, fontWeight = FontWeight.Bold)
                        }

                        Spacer(modifier = Modifier.height(8.dp))

                        val totalCost = String.format(Locale.US, "%.2f", logs.sumOf { it.costCents } / 100.0)
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text("Total Service Invested", color = TkTextMuted, fontSize = 13.sp)
                            Text("$$totalCost", color = TkText, fontSize = 13.sp, fontWeight = FontWeight.Bold)
                        }
                    }
                }

                Spacer(modifier = Modifier.height(20.dp))

                Text(
                    text = "Handing this formatted report directly to prospective buyers or mechanics proves consistent care and maximizes resale value without disclosing personal information.",
                    color = TkTextMuted,
                    fontSize = 13.sp,
                    lineHeight = 18.sp
                )
            }

            Column {
                NoinButton(
                    text = if (isGenerating) "Generating PDF..." else "Export & Share Dossier (PDF)",
                    enabled = !isGenerating && vehicle != null && logs.isNotEmpty(),
                    onClick = {
                        isGenerating = true
                        coroutineScope.launch {
                            val v = vehicle ?: return@launch
                            val pdfFile = withContext(Dispatchers.IO) {
                                DossierPdfGenerator.generateDossier(context, v, logs)
                            }

                            val uri = FileProvider.getUriForFile(
                                context,
                                "${context.packageName}.fileprovider",
                                pdfFile
                            )

                            isGenerating = false

                            // Launch native Android Share Sheet
                            val shareIntent = Intent(Intent.ACTION_SEND).apply {
                                type = "application/pdf"
                                putExtra(Intent.EXTRA_STREAM, uri)
                                addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                            }
                            context.startActivity(Intent.createChooser(shareIntent, "Share Vehicle Dossier"))
                        }
                    }
                )

                Spacer(modifier = Modifier.height(16.dp))
            }
        }
    }
}
