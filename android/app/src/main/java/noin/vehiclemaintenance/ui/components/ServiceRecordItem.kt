package noin.vehiclemaintenance.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.data.model.ServiceLog
import noin.vehiclemaintenance.ui.theme.*
import java.text.NumberFormat
import java.text.SimpleDateFormat
import java.util.*

@Composable
fun ServiceRecordItem(
    log: ServiceLog,
    currencySymbol: String = "$",
    odometerUnit: String = "mi",
    modifier: Modifier = Modifier
) {
    val dateFormatter = SimpleDateFormat("MMM dd, yyyy", Locale.US)
    val formattedDate = dateFormatter.format(Date(log.serviceDate))
    val formattedOdometer = NumberFormat.getNumberInstance(Locale.US).format(log.odometer)
    val formattedCost = String.format(Locale.US, "%.2f", log.costCents / 100.0)

    val icon = when (log.serviceType) {
        "oil_change" -> Icons.Default.Build
        "tire_rotation" -> Icons.Default.Sync
        "brakes" -> Icons.Default.Warning
        "battery" -> Icons.Default.BatteryChargingFull
        else -> Icons.Default.Handyman
    }

    Box(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(14.dp))
            .background(TkSurface)
            .border(1.dp, TkBorder, RoundedCornerShape(14.dp))
            .padding(16.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            verticalAlignment = Alignment.CenterVertically
        ) {
            // Service Icon Badge
            Box(
                modifier = Modifier
                    .size(44.dp)
                    .clip(RoundedCornerShape(10.dp))
                    .background(TkSurfaceElevated),
                contentAlignment = Alignment.Center
            ) {
                Icon(
                    imageVector = icon,
                    contentDescription = null,
                    tint = TkAccent,
                    modifier = Modifier.size(22.dp)
                )
            }

            Spacer(modifier = Modifier.width(14.dp))

            // Center details
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = log.title,
                    color = TkText,
                    fontSize = 15.sp,
                    fontWeight = FontWeight.SemiBold,
                    maxLines = 1
                )
                Spacer(modifier = Modifier.height(3.dp))
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(
                        text = formattedDate,
                        color = TkTextMuted,
                        fontSize = 13.sp
                    )
                    if (!log.serviceProvider.isNullOrBlank()) {
                        Text(
                            text = " • ${log.serviceProvider}",
                            color = TkTextMuted,
                            fontSize = 13.sp
                        )
                    }
                }
                if (!log.partNumbers.isNullOrBlank()) {
                    Spacer(modifier = Modifier.height(2.dp))
                    Text(
                        text = "Parts: ${log.partNumbers}",
                        color = TkTextMuted,
                        fontSize = 12.sp,
                        maxLines = 1
                    )
                }
            }

            Spacer(modifier = Modifier.width(10.dp))

            // Right costs & mileage
            Column(horizontalAlignment = Alignment.End) {
                Text(
                    text = "$currencySymbol$formattedCost",
                    color = TkText,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.Bold,
                    fontFamily = FontFamily.Monospace
                )
                Spacer(modifier = Modifier.height(3.dp))
                Text(
                    text = "$formattedOdometer $odometerUnit",
                    color = TkAccent,
                    fontSize = 12.sp,
                    fontWeight = FontWeight.Medium,
                    fontFamily = FontFamily.Monospace
                )
            }
        }
    }
}
