package noin.vehiclemaintenance.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
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
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.ui.theme.*

data class ServiceCategory(
    val key: String,
    val title: String,
    val icon: ImageVector
)

val StandardCategories = listOf(
    ServiceCategory("oil_change", "Oil & Filter", Icons.Default.Build),
    ServiceCategory("tire_rotation", "Tyres", Icons.Default.Sync),
    ServiceCategory("brakes", "Brakes", Icons.Default.Warning),
    ServiceCategory("battery", "Battery", Icons.Default.BatteryChargingFull),
    ServiceCategory("inspection", "Inspection", Icons.Default.Search),
    ServiceCategory("custom", "Other", Icons.Default.Settings)
)

@Composable
fun QuickServiceTile(
    category: ServiceCategory,
    isSelected: Boolean,
    onSelect: () -> Unit,
    modifier: Modifier = Modifier
) {
    val borderColor = if (isSelected) TkAccent else TkBorder
    val bgColor = if (isSelected) TkSurfaceElevated else TkSurfaceCard
    val iconColor = if (isSelected) TkAccent else TkTextMuted
    val textColor = if (isSelected) TkText else TkTextMuted

    Box(
        modifier = modifier
            .height(84.dp)
            .clip(RoundedCornerShape(12.dp))
            .background(bgColor)
            .border(if (isSelected) 2.dp else 1.dp, borderColor, RoundedCornerShape(12.dp))
            .clickable { onSelect() }
            .padding(8.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Icon(
                imageVector = category.icon,
                contentDescription = category.title,
                tint = iconColor,
                modifier = Modifier.size(26.dp)
            )
            Spacer(modifier = Modifier.height(6.dp))
            Text(
                text = category.title,
                color = textColor,
                fontSize = 12.sp,
                fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Medium,
                textAlign = TextAlign.Center,
                maxLines = 1
            )
        }
    }
}
