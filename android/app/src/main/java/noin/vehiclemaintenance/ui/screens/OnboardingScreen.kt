package noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
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
import noin.vehiclemaintenance.ui.components.NoinButton
import noin.vehiclemaintenance.ui.theme.*

data class OnboardingSlide(
    val icon: String,
    val tag: String,
    val title: String,
    val description: String,
    val highlight: String
)

@Composable
fun OnboardingScreen(
    onFinishOnboarding: () -> Unit,
    onSkipToGarage: () -> Unit,
    modifier: Modifier = Modifier
) {
    var currentSlideIndex by remember { mutableStateOf(0) }

    val slides = listOf(
        OnboardingSlide(
            icon = "🛡️",
            tag = "LOCAL-FIRST INTEGRITY",
            title = "Own Your Garage Data",
            description = "No mandatory accounts, no cloud dependencies, and zero corporate telemetry. All vehicle logs remain safely stored on your device's local SQLite database.",
            highlight = "100% Offline • Zero Data Hostage"
        ),
        OnboardingSlide(
            icon = "⚡",
            tag = "FRICTIONLESS LOGGING",
            title = "1-Tap Maintenance Records",
            description = "Pre-configured smart tiles for synthetic oil, brakes, tire rotations, and batteries. Automatically tracks mileage progression with rollback protection.",
            highlight = "Log in under 5 seconds at the bay"
        ),
        OnboardingSlide(
            icon = "📄",
            tag = "MAXIMIZE RESALE VALUE",
            title = "Buyer-Ready Resale Dossier",
            description = "Generate an institutional-grade, multi-column PDF maintenance ledger at any time. Hand it directly to private buyers to prove every dollar and service performed.",
            highlight = "Built-in Canvas PDF Engine"
        )
    )

    val currentSlide = slides[currentSlideIndex]

    Scaffold(
        containerColor = TkBackground,
        topBar = {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 20.dp, vertical = 16.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "NOIN",
                    color = TkText,
                    fontWeight = FontWeight.Black,
                    letterSpacing = 1.5.sp,
                    fontSize = 14.sp
                )

                if (currentSlideIndex < slides.size - 1) {
                    TextButton(onClick = onSkipToGarage) {
                        Text(
                            text = "Skip",
                            color = TkTextMuted,
                            fontSize = 13.sp,
                            fontWeight = FontWeight.SemiBold
                        )
                    }
                }
            }
        }
    ) { paddingValues ->
        Column(
            modifier = modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(horizontal = 24.dp, vertical = 16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            Spacer(modifier = Modifier.height(12.dp))

            // Slide Hero Illustration / Badge
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center,
                modifier = Modifier.weight(1f)
            ) {
                Box(
                    modifier = Modifier
                        .size(100.dp)
                        .clip(RoundedCornerShape(28.dp))
                        .background(TkSurfaceElevated),
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        text = currentSlide.icon,
                        fontSize = 44.sp
                    )
                }

                Spacer(modifier = Modifier.height(28.dp))

                // Tag
                Surface(
                    color = TkSurface,
                    shape = RoundedCornerShape(6.dp),
                    border = androidx.compose.foundation.BorderStroke(1.dp, TkBorder)
                ) {
                    Text(
                        text = currentSlide.tag,
                        color = TkAccent,
                        fontSize = 11.sp,
                        fontWeight = FontWeight.ExtraBold,
                        letterSpacing = 1.sp,
                        modifier = Modifier.padding(horizontal = 10.dp, vertical = 4.dp)
                    )
                }

                Spacer(modifier = Modifier.height(16.dp))

                // Title
                Text(
                    text = currentSlide.title,
                    color = TkText,
                    fontSize = 26.sp,
                    fontWeight = FontWeight.Black,
                    textAlign = TextAlign.Center,
                    lineHeight = 32.sp
                )

                Spacer(modifier = Modifier.height(14.dp))

                // Description
                Text(
                    text = currentSlide.description,
                    color = TkTextMuted,
                    fontSize = 14.sp,
                    lineHeight = 22.sp,
                    textAlign = TextAlign.Center,
                    modifier = Modifier.padding(horizontal = 12.dp)
                )

                Spacer(modifier = Modifier.height(20.dp))

                // Highlight Badge
                Surface(
                    color = TkSurfaceCard,
                    shape = RoundedCornerShape(8.dp),
                    border = androidx.compose.foundation.BorderStroke(1.dp, TkBorderInput)
                ) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier.padding(horizontal = 14.dp, vertical = 8.dp)
                    ) {
                        Text(
                            text = "✓",
                            color = TkSuccess,
                            fontWeight = FontWeight.Bold,
                            fontSize = 13.sp,
                            modifier = Modifier.padding(end = 6.dp)
                        )
                        Text(
                            text = currentSlide.highlight,
                            color = TkText,
                            fontSize = 12.sp,
                            fontWeight = FontWeight.SemiBold,
                            fontFamily = FontFamily.Monospace
                        )
                    }
                }
            }

            // Bottom Navigation & Stepper
            Column(
                modifier = Modifier.fillMaxWidth(),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                // Stepper indicators
                Row(
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.padding(bottom = 24.dp)
                ) {
                    slides.indices.forEach { index ->
                        Box(
                            modifier = Modifier
                                .height(6.dp)
                                .width(if (index == currentSlideIndex) 28.dp else 8.dp)
                                .clip(CircleShape)
                                .background(if (index == currentSlideIndex) TkAccent else TkBorder)
                        )
                    }
                }

                if (currentSlideIndex < slides.size - 1) {
                    NoinButton(
                        text = "Next: ${slides[currentSlideIndex + 1].title}",
                        onClick = { currentSlideIndex++ },
                        modifier = Modifier.fillMaxWidth()
                    )
                } else {
                    NoinButton(
                        text = "Park Your First Vehicle →",
                        onClick = onFinishOnboarding,
                        modifier = Modifier.fillMaxWidth()
                    )
                }

                Spacer(modifier = Modifier.height(8.dp))

                Text(
                    text = "Free forever for 1 vehicle • No credit card required",
                    color = TkTextMuted,
                    fontSize = 11.sp,
                    fontWeight = FontWeight.Medium,
                    modifier = Modifier.padding(bottom = 8.dp)
                )
            }
        }
    }
}
