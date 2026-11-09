package in.noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import in.noin.vehiclemaintenance.ui.components.NoinButton
import in.noin.vehiclemaintenance.ui.theme.*

enum class PricingTier(val id: String, val title: String, val price: String, val subtext: String, val badge: String?) {
    LIFETIME("tk_lifetime_multibay", "Lifetime Multi-Bay", "$19.99", "One-time payment • Own forever", "MOST POPULAR"),
    MONTHLY("tk_sub_monthly_multibay", "Monthly Pass", "$2.99", "Billed monthly • Cancel anytime", null)
}

data class PlanFeature(
    val title: String,
    val freeDesc: String,
    val proDesc: String,
    val proOnly: Boolean = false
)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProUpgradeScreen(
    onNavigateBack: () -> Unit,
    onPurchaseTier: (PricingTier) -> Unit,
    onRestorePurchases: () -> Unit,
    modifier: Modifier = Modifier
) {
    var selectedTier by remember { mutableStateOf(PricingTier.LIFETIME) }

    val upgradeFeatures = listOf(
        PlanFeature("Garage Bays", "1 Vehicle", "Unlimited Fleet", proOnly = true),
        PlanFeature("Resale Dossier", "1-Page Basic", "Multi-Page A4", proOnly = true),
        PlanFeature("Receipt Photo Vault", "Manual log", "Unlimited Photos", proOnly = true)
    )

    val baselineGuarantees = listOf(
        "100% Offline SQLite: Private local storage, zero accounts",
        "Zero Ads & Trackers: Completely clutter-free forever",
        "Full Data Portability: Export raw CSV/JSON anytime at $0"
    )

    Scaffold(
        containerColor = TkBackground,
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "NOIN PRO",
                        color = TkText,
                        fontWeight = FontWeight.Black,
                        fontSize = 15.sp,
                        letterSpacing = 1.2.sp
                    )
                },
                navigationIcon = {
                    IconButton(onClick = onNavigateBack) {
                        Icon(
                            imageVector = Icons.Default.ArrowBack,
                            contentDescription = "Back",
                            tint = TkText
                        )
                    }
                },
                actions = {
                    TextButton(onClick = onRestorePurchases) {
                        Text(
                            text = "Restore",
                            color = TkAccent,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.Bold
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = TkBackground
                )
            )
        }
    ) { paddingValues ->
        Column(
            modifier = modifier
                .fillMaxSize()
                .padding(paddingValues)
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 20.dp, vertical = 12.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            // Hero Title
            Text(
                text = "Say Goodbye to Subscription Traps",
                color = TkText,
                fontSize = 22.sp,
                fontWeight = FontWeight.Black,
                textAlign = TextAlign.Center,
                lineHeight = 28.sp
            )

            Spacer(modifier = Modifier.height(8.dp))

            Text(
                text = "Incumbents charge $30–$50 every single year just to record your oil changes. Noin is built on honest pricing for gearheads.",
                color = TkTextMuted,
                fontSize = 13.sp,
                textAlign = TextAlign.Center,
                lineHeight = 19.sp,
                modifier = Modifier.padding(horizontal = 8.dp)
            )

            Spacer(modifier = Modifier.height(20.dp))

            // Tier Selector Cards
            PricingTier.values().forEach { tier ->
                val isSelected = selectedTier == tier
                val borderColor = if (isSelected) TkAccent else TkBorder

                Card(
                    colors = CardDefaults.cardColors(
                        containerColor = if (isSelected) TkSurfaceElevated else TkSurfaceCard
                    ),
                    shape = RoundedCornerShape(14.dp),
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 6.dp)
                        .border(
                            width = if (isSelected) 2.dp else 1.dp,
                            color = borderColor,
                            shape = RoundedCornerShape(14.dp)
                        )
                        .clickable { selectedTier = tier }
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                RadioButton(
                                    selected = isSelected,
                                    onClick = { selectedTier = tier },
                                    colors = RadioButtonDefaults.colors(
                                        selectedColor = TkAccent,
                                        unselectedColor = TkBorderInput
                                    )
                                )
                                Spacer(modifier = Modifier.width(8.dp))
                                Column {
                                    Text(
                                        text = tier.title,
                                        color = TkText,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 16.sp
                                    )
                                    Text(
                                        text = tier.subtext,
                                        color = TkTextMuted,
                                        fontSize = 12.sp
                                    )
                                }
                            }

                            Text(
                                text = tier.price,
                                color = if (isSelected) TkAccent else TkText,
                                fontWeight = FontWeight.ExtraBold,
                                fontSize = 20.sp,
                                fontFamily = FontFamily.Monospace
                            )
                        }

                        tier.badge?.let { badgeText ->
                            Spacer(modifier = Modifier.height(10.dp))
                            Surface(
                                color = TkAccent,
                                shape = RoundedCornerShape(4.dp)
                            ) {
                                Text(
                                    text = "★ $badgeText",
                                    color = TkOnAccent,
                                    fontSize = 10.sp,
                                    fontWeight = FontWeight.Black,
                                    letterSpacing = 0.8.sp,
                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 2.dp)
                                )
                            }
                        }
                    }
                }
            }

            Spacer(modifier = Modifier.height(24.dp))

            // Redesigned Comparison Feature Matrix
            Surface(
                color = TkSurfaceCard,
                shape = RoundedCornerShape(14.dp),
                border = androidx.compose.foundation.BorderStroke(1.dp, TkBorder),
                modifier = Modifier.fillMaxWidth()
            ) {
                Column {
                    // Explicit Column Headers
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(TkSurfaceElevated)
                            .padding(horizontal = 14.dp, vertical = 10.dp),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "FEATURE",
                            color = TkTextMuted,
                            fontSize = 11.sp,
                            fontWeight = FontWeight.ExtraBold,
                            letterSpacing = 0.6.sp,
                            modifier = Modifier.weight(1.3f)
                        )
                        Text(
                            text = "FREE TIER",
                            color = TkTextMuted,
                            fontSize = 11.sp,
                            fontWeight = FontWeight.Bold,
                            textAlign = TextAlign.Center,
                            modifier = Modifier.weight(1f)
                        )
                        Box(
                            modifier = Modifier.weight(1.15f),
                            contentAlignment = Alignment.Center
                        ) {
                            Surface(
                                color = TkAccent,
                                shape = RoundedCornerShape(5.dp)
                            ) {
                                Text(
                                    text = "PRO ★",
                                    color = TkOnAccent,
                                    fontSize = 10.sp,
                                    fontWeight = FontWeight.Black,
                                    letterSpacing = 0.5.sp,
                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                                )
                            }
                        }
                    }

                    Divider(color = TkBorder, thickness = 1.dp)

                    // Upgrade Feature Rows
                    upgradeFeatures.forEachIndexed { idx, feat ->
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(horizontal = 14.dp, vertical = 12.dp),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Column(modifier = Modifier.weight(1.3f)) {
                                Text(
                                    text = feat.title,
                                    color = TkText,
                                    fontSize = 13.sp,
                                    fontWeight = FontWeight.Bold
                                )
                                Text(
                                    text = if (feat.title == "Garage Bays") "Vehicles tracked" else if (feat.title == "Resale Dossier") "Proof of care PDF" else "Invoices & parts",
                                    color = TkTextMuted,
                                    fontSize = 11.sp
                                )
                            }

                            Text(
                                text = feat.freeDesc,
                                color = TkTextMuted,
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Medium,
                                textAlign = TextAlign.Center,
                                modifier = Modifier.weight(1f)
                            )

                            Box(
                                modifier = Modifier.weight(1.15f),
                                contentAlignment = Alignment.Center
                            ) {
                                Surface(
                                    color = if (feat.title == "Resale Dossier") TkSurfaceElevated else Color(0xFFECFDF5),
                                    shape = RoundedCornerShape(6.dp),
                                    border = androidx.compose.foundation.BorderStroke(
                                        1.dp,
                                        if (feat.title == "Resale Dossier") TkBorder else Color(0xFFA7F3D0)
                                    )
                                ) {
                                    Text(
                                        text = feat.proDesc,
                                        color = if (feat.title == "Resale Dossier") TkText else Color(0xFF047857),
                                        fontSize = 11.sp,
                                        fontWeight = FontWeight.ExtraBold,
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                                    )
                                }
                            }
                        }

                        if (idx < upgradeFeatures.size - 1) {
                            Divider(color = Color(0xFFF1F5F9), thickness = 1.dp)
                        }
                    }

                    // Shared Guarantees Strip
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(TkSurfaceElevated)
                            .padding(horizontal = 14.dp, vertical = 10.dp)
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Text(
                                text = "✓ ",
                                color = TkSuccess,
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Black
                            )
                            Text(
                                text = "Included on Both Free & Pro:",
                                color = TkText,
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Bold
                            )
                        }
                        Spacer(modifier = Modifier.height(2.dp))
                        Text(
                            text = "100% Offline SQLite • Zero Ads & Trackers • Full CSV/JSON Export",
                            color = TkTextMuted,
                            fontSize = 11.sp,
                            lineHeight = 16.sp,
                            modifier = Modifier.padding(start = 16.dp)
                        )
                    }
                }
            }

            Spacer(modifier = Modifier.height(28.dp))

            // Primary Call to Action Button
            NoinButton(
                text = if (selectedTier == PricingTier.LIFETIME) "Unlock Multi-Bay Garage ($19.99 Once)" else "Start Monthly Pass ($2.99/mo)",
                onClick = { onPurchaseTier(selectedTier) },
                modifier = Modifier.fillMaxWidth()
            )

            Spacer(modifier = Modifier.height(12.dp))

            // Trust guarantee
            Text(
                text = "🔒 Secure checkout via Google Play Billing. 100% money-back guarantee.",
                color = TkTextMuted,
                fontSize = 11.sp,
                textAlign = TextAlign.Center
            )

            Spacer(modifier = Modifier.height(16.dp))
        }
    }
}
