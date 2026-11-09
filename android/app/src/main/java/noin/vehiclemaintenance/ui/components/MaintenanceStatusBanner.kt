package noin.vehiclemaintenance.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.ui.theme.*

enum class StatusLevel {
    UP_TO_DATE,
    DUE_SOON,
    OVERDUE
}

@Composable
fun MaintenanceStatusBanner(
    status: StatusLevel,
    message: String,
    modifier: Modifier = Modifier
) {
    val (borderColor, icon, tintColor) = when (status) {
        StatusLevel.UP_TO_DATE -> Triple(TkSuccess, Icons.Default.CheckCircle, TkSuccess)
        StatusLevel.DUE_SOON -> Triple(TkAccent, Icons.Default.Info, TkAccent)
        StatusLevel.OVERDUE -> Triple(TkDanger, Icons.Default.Warning, TkDanger)
    }

    Box(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(12.dp))
            .background(TkSurfaceCard)
            .border(1.dp, borderColor, RoundedCornerShape(12.dp))
            .padding(horizontal = 16.dp, vertical = 12.dp)
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically
        ) {
            Icon(
                imageVector = icon,
                contentDescription = null,
                tint = tintColor,
                modifier = Modifier.size(20.dp)
            )
            Spacer(modifier = Modifier.width(10.dp))
            Text(
                text = message,
                color = TkText,
                fontSize = 13.sp,
                fontWeight = FontWeight.Medium
            )
        }
    }
}
