package noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.PictureAsPdf
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.data.repository.VehicleRepository
import noin.vehiclemaintenance.ui.components.OdometerWidget
import noin.vehiclemaintenance.ui.components.ServiceRecordItem
import noin.vehiclemaintenance.ui.components.NoinButton
import noin.vehiclemaintenance.ui.theme.*
import java.util.Locale

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun VehicleDetailBayScreen(
    vehicleId: String,
    repository: VehicleRepository,
    onNavigateBack: () -> Unit,
    onLogServiceClick: (String) -> Unit,
    onGenerateDossierClick: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    val vehicle by repository.getVehicle(vehicleId).collectAsState(initial = null)
    val logs by repository.getLogsForVehicle(vehicleId).collectAsState(initial = emptyList())
    val totalCostCents by repository.getTotalCost(vehicleId).collectAsState(initial = 0)

    val formattedTotalCost = String.format(Locale.US, "%.2f", (totalCostCents ?: 0) / 100.0)

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = vehicle?.let { "${it.year} ${it.make} ${it.model}" } ?: "Vehicle Bay",
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
                actions = {
                    IconButton(
                        onClick = { onGenerateDossierClick(vehicleId) },
                        modifier = Modifier
                            .padding(end = 8.dp)
                            .size(38.dp)
                            .clip(RoundedCornerShape(8.dp))
                            .background(TkSurfaceElevated)
                    ) {
                        Icon(
                            imageVector = Icons.Default.PictureAsPdf,
                            contentDescription = "Export Dossier",
                            tint = TkAccent,
                            modifier = Modifier.size(20.dp)
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = TkBg)
            )
        },
        containerColor = TkBg,
        modifier = modifier
    ) { innerPadding ->
        vehicle?.let { v ->
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding)
                    .padding(horizontal = 20.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                item {
                    Spacer(modifier = Modifier.height(4.dp))
                    OdometerWidget(
                        mileage = v.currentOdometer,
                        unit = v.odometerUnit
                    )
                }

                // Summary Stats Strip
                item {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(12.dp))
                            .background(TkSurfaceCard)
                            .padding(16.dp),
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        Column {
                            Text(
                                text = "TOTAL LOGS",
                                color = TkTextMuted,
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Bold,
                                letterSpacing = 1.sp
                            )
                            Spacer(modifier = Modifier.height(4.dp))
                            Text(
                                text = "${logs.size} Records",
                                color = TkText,
                                fontSize = 18.sp,
                                fontWeight = FontWeight.Bold
                            )
                        }

                        Column(horizontalAlignment = Alignment.End) {
                            Text(
                                text = "LIFETIME MAINTENANCE",
                                color = TkTextMuted,
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Bold,
                                letterSpacing = 1.sp
                            )
                            Spacer(modifier = Modifier.height(4.dp))
                            Text(
                                text = "$$formattedTotalCost",
                                color = TkAccent,
                                fontSize = 18.sp,
                                fontWeight = FontWeight.Bold
                            )
                        }
                    }
                }

                item {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "SERVICE HISTORY",
                            color = TkAccent,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Bold,
                            letterSpacing = 1.sp
                        )
                        Text(
                            text = "${logs.size} entries",
                            color = TkTextMuted,
                            fontSize = 12.sp
                        )
                    }
                }

                if (logs.isEmpty()) {
                    item {
                        Box(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clip(RoundedCornerShape(12.dp))
                                .background(TkSurface)
                                .padding(28.dp),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(
                                text = "No maintenance logs yet. Tap '+ Log Service' below to record your first oil change, tires, or repair.",
                                color = TkTextMuted,
                                fontSize = 13.sp,
                                textAlign = androidx.compose.ui.text.style.TextAlign.Center
                            )
                        }
                    }
                } else {
                    items(logs) { log ->
                        ServiceRecordItem(
                            log = log,
                            odometerUnit = v.odometerUnit
                        )
                    }
                }

                item {
                    Spacer(modifier = Modifier.height(8.dp))
                    NoinButton(
                        text = "+ Log Service",
                        onClick = { onLogServiceClick(v.id) }
                    )
                    Spacer(modifier = Modifier.height(24.dp))
                }
            }
        }
    }
}
