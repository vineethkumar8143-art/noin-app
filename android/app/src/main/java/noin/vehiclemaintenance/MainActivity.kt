package noin.vehiclemaintenance

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.navigation.compose.rememberNavController
import noin.vehiclemaintenance.ui.navigation.NoinNavHost
import noin.vehiclemaintenance.ui.theme.NoinTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        val app = application as NoinApp
        val repository = app.repository

        setContent {
            NoinTheme {
                val navController = rememberNavController()
                NoinNavHost(
                    navController = navController,
                    repository = repository
                )
            }
        }
    }
}
