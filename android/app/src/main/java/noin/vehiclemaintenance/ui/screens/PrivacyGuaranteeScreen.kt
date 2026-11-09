package noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Shield
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.ui.theme.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PrivacyGuaranteeScreen(
    onNavigateBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Privacy & Data Guarantee",
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
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 20.dp, vertical = 16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Hero Shield Box
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(16.dp))
                    .background(TkSurfaceCard)
                    .border(1.dp, TkBorder, RoundedCornerShape(16.dp))
                    .padding(20.dp),
                contentAlignment = Alignment.Center
            ) {
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Box(
                        modifier = Modifier
                            .size(60.dp)
                            .clip(RoundedCornerShape(14.dp))
                            .background(TkSurfaceElevated),
                        contentAlignment = Alignment.Center
                    ) {
                        Icon(
                            imageVector = Icons.Default.Shield,
                            contentDescription = null,
                            tint = TkAccent,
                            modifier = Modifier.size(32.dp)
                        )
                    }
                    Spacer(modifier = Modifier.height(12.dp))
                    Text(
                        text = "100% On-Device & Offline",
                        color = TkText,
                        fontSize = 17.sp,
                        fontWeight = FontWeight.Bold
                    )
                    Spacer(modifier = Modifier.height(4.dp))
                    Text(
                        text = "Your vehicle records never leave your phone.",
                        color = TkTextMuted,
                        fontSize = 13.sp
                    )
                }
            }

            Text(
                text = "OUR CORE PRIVACY PROMISES",
                color = TkAccent,
                fontSize = 12.sp,
                fontWeight = FontWeight.Bold,
                letterSpacing = 1.sp
            )

            PrivacyPillarCard(
                icon = Icons.Default.Lock,
                title = "Local SQLite Storage Only",
                description = "All vehicle profiles, service receipts, part numbers, and costs reside in an encrypted Room SQLite database on your device. We have no external servers holding your data."
            )

            PrivacyPillarCard(
                icon = Icons.Default.CheckCircle,
                title = "Zero Location or Telemetry Spying",
                description = "Unlike commercial trackers, Noin never requests background GPS location permissions, reads your contacts, or sells your driving telemetry to third-party insurance brokers."
            )

            PrivacyPillarCard(
                icon = Icons.Default.CheckCircle,
                title = "Zero Hostage Data",
                description = "Your records are yours forever. You can export complete CSV or JSON backups anytime, free of charge. If you uninstall the app or upgrade devices, you take your data with you."
            )

            PrivacyPillarCard(
                icon = Icons.Default.CheckCircle,
                title = "Transparent Business Model",
                description = "No recurring monthly fees for basic tracking. We offer an optional $19.99 lifetime unlock for multi-car garages, ensuring our incentives align with keeping your software reliable."
            )

            Spacer(modifier = Modifier.height(20.dp))
        }
    }
}

@Composable
fun PrivacyPillarCard(
    icon: ImageVector,
    title: String,
    description: String
) {
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(14.dp))
            .background(TkSurface)
            .border(1.dp, TkBorder, RoundedCornerShape(14.dp))
            .padding(16.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            verticalAlignment = Alignment.Top
        ) {
            Box(
                modifier = Modifier
                    .size(36.dp)
                    .clip(RoundedCornerShape(8.dp))
                    .background(TkSurfaceElevated),
                contentAlignment = Alignment.Center
            ) {
                Icon(
                    imageVector = icon,
                    contentDescription = null,
                    tint = TkAccent,
                    modifier = Modifier.size(18.dp)
                )
            }
            Spacer(modifier = Modifier.width(12.dp))
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = title,
                    color = TkText,
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold
                )
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = description,
                    color = TkTextMuted,
                    fontSize = 12.sp,
                    lineHeight = 17.sp
                )
            }
        }
    }
}
