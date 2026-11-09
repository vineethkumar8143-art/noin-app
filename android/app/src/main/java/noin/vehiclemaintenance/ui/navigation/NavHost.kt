package noin.vehiclemaintenance.ui.navigation

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.navArgument
import noin.vehiclemaintenance.data.repository.VehicleRepository
import noin.vehiclemaintenance.ui.screens.*

sealed class Screen(val route: String) {
    object Onboarding : Screen("onboarding")
    object GarageHome : Screen("garage_home")
    object AddVehicle : Screen("add_vehicle")
    object VehicleDetail : Screen("vehicle_detail/{vehicleId}") {
        fun createRoute(vehicleId: String) = "vehicle_detail/$vehicleId"
    }
    object QuickLog : Screen("quick_log/{vehicleId}") {
        fun createRoute(vehicleId: String) = "quick_log/$vehicleId"
    }
    object DossierExport : Screen("dossier_export/{vehicleId}") {
        fun createRoute(vehicleId: String) = "dossier_export/$vehicleId"
    }
    object PrivacyGuarantee : Screen("privacy_guarantee")
    object ProUpgrade : Screen("pro_upgrade")
}

@Composable
fun NoinNavHost(
    navController: NavHostController,
    repository: VehicleRepository,
    modifier: Modifier = Modifier
) {
    NavHost(
        navController = navController,
        startDestination = Screen.GarageHome.route,
        modifier = modifier
    ) {
        composable(Screen.Onboarding.route) {
            OnboardingScreen(
                onFinishOnboarding = {
                    navController.navigate(Screen.AddVehicle.route) {
                        popUpTo(Screen.Onboarding.route) { inclusive = true }
                    }
                },
                onSkipToGarage = {
                    navController.navigate(Screen.GarageHome.route) {
                        popUpTo(Screen.Onboarding.route) { inclusive = true }
                    }
                }
            )
        }

        composable(Screen.GarageHome.route) {
            GarageHomeScreen(
                repository = repository,
                onVehicleClick = { vehicleId ->
                    navController.navigate(Screen.VehicleDetail.createRoute(vehicleId))
                },
                onAddVehicleClick = {
                    navController.navigate(Screen.AddVehicle.route)
                },
                onLogServiceClick = { vehicleId ->
                    navController.navigate(Screen.QuickLog.createRoute(vehicleId))
                },
                onPrivacyClick = {
                    navController.navigate(Screen.PrivacyGuarantee.route)
                },
                onProClick = {
                    navController.navigate(Screen.ProUpgrade.route)
                }
            )
        }

        composable(Screen.AddVehicle.route) {
            AddVehicleScreen(
                repository = repository,
                onNavigateBack = { navController.popBackStack() }
            )
        }

        composable(
            route = Screen.VehicleDetail.route,
            arguments = listOf(navArgument("vehicleId") { type = NavType.StringType })
        ) { backStackEntry ->
            val vehicleId = backStackEntry.arguments?.getString("vehicleId") ?: return@composable
            VehicleDetailBayScreen(
                vehicleId = vehicleId,
                repository = repository,
                onNavigateBack = { navController.popBackStack() },
                onLogServiceClick = { id ->
                    navController.navigate(Screen.QuickLog.createRoute(id))
                },
                onGenerateDossierClick = { id ->
                    navController.navigate(Screen.DossierExport.createRoute(id))
                }
            )
        }

        composable(
            route = Screen.QuickLog.route,
            arguments = listOf(navArgument("vehicleId") { type = NavType.StringType })
        ) { backStackEntry ->
            val vehicleId = backStackEntry.arguments?.getString("vehicleId") ?: return@composable
            QuickLogEntryScreen(
                vehicleId = vehicleId,
                repository = repository,
                onNavigateBack = { navController.popBackStack() }
            )
        }

        composable(
            route = Screen.DossierExport.route,
            arguments = listOf(navArgument("vehicleId") { type = NavType.StringType })
        ) { backStackEntry ->
            val vehicleId = backStackEntry.arguments?.getString("vehicleId") ?: return@composable
            DossierExportScreen(
                vehicleId = vehicleId,
                repository = repository,
                onNavigateBack = { navController.popBackStack() }
            )
        }

        composable(Screen.PrivacyGuarantee.route) {
            PrivacyGuaranteeScreen(
                onNavigateBack = { navController.popBackStack() }
            )
        }

        composable(Screen.ProUpgrade.route) {
            ProUpgradeScreen(
                onNavigateBack = { navController.popBackStack() },
                onPurchaseTier = { tier ->
                    // Launch Google Play Billing Flow for tier.id
                    navController.popBackStack()
                },
                onRestorePurchases = {
                    // Query In-App Purchases from Google Play
                    navController.popBackStack()
                }
            )
        }
    }
}
