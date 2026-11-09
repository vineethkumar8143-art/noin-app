package noin.vehiclemaintenance.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable

private val DayLightColorScheme = lightColorScheme(
    primary = TkAccent,
    onPrimary = TkOnAccent,
    primaryContainer = TkSurfaceElevated,
    onPrimaryContainer = TkText,
    secondary = TkAccent,
    onSecondary = TkOnAccent,
    background = TkBg,
    onBackground = TkText,
    surface = TkSurface,
    onSurface = TkText,
    surfaceVariant = TkSurfaceCard,
    onSurfaceVariant = TkTextMuted,
    outline = TkBorder,
    outlineVariant = TkBorderInput,
    error = TkDanger,
    onError = TkOnDanger
)

@Composable
fun NoinTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = DayLightColorScheme,
        typography = Typography,
        content = content
    )
}
