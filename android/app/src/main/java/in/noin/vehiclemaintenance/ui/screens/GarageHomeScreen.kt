package in.noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.DirectionsCar
import androidx.compose.material.icons.filled.Shield
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
import in.noin.vehiclemaintenance.data.model.Vehicle
import in.noin.vehiclemaintenance.data.repository.VehicleRepository
import in.noin.vehiclemaintenance.ui.components.MaintenanceStatusBanner
import in.noin.vehiclemaintenance.ui.components.OdometerWidget
import in.noin.vehiclemaintenance.ui.components.StatusLevel
import in.noin.vehiclemaintenance.ui.components.NoinButton
import in.noin.vehiclemaintenance.ui.theme.*

@Composable
fun GarageHomeScreen(
    repository: VehicleRepository,
    onVehicleClick: (String) -> Unit,
    onAddVehicleClick: () -> Unit,
    onLogServiceClick: (String) -> Unit,
    onPrivacyClick: () -> Unit,
    onProClick: () -> Unit = {},
    modifier: Modifier = Modifier
) {
    val vehicles by repository.getAllVehicles().collectAsState(initial = emptyList())

    Scaffold(
        topBar = {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(TkBg)
                    .statusBarsPadding()
                    .padding(horizontal = 20.dp, vertical = 16.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Column {
                    Text(
                        text = "NOIN",
                        color = TkAccent,
                        fontSize = 13.sp,
                        fontWeight = FontWeight.Black,
                        letterSpacing = 1.5.sp
                    )
                    Text(
                        text = "Your Garage Bay",
                        color = TkText,
                        fontSize = 20.sp,
                        fontWeight = FontWeight.Bold
                    )
                }

                Row(
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    // Pro Badge Action
                    Surface(
                        color = TkSurfaceElevated,
                        shape = RoundedCornerShape(10.dp),
                        border = androidx.compose.foundation.BorderStroke(1.dp, TkAccent.copy(alpha = 0.5f)),
                        modifier = Modifier
                            .height(40.dp)
                            .clickable { onProClick() }
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.padding(horizontal = 10.dp)
                        ) {
                            Text(text = "★", color = TkAccent, fontSize = 12.sp)
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(
                                text = "PRO",
                                color = TkText,
                                fontWeight = FontWeight.Black,
                                fontSize = 12.sp,
                                letterSpacing = 0.5.sp
                            )
                        }
                    }

                    IconButton(
                        onClick = onPrivacyClick,
                        modifier = Modifier
                            .size(40.dp)
                            .clip(RoundedCornerShape(10.dp))
                            .background(TkSurfaceElevated)
                    ) {
                        Icon(
                            imageVector = Icons.Default.Shield,
                            contentDescription = "Privacy Guarantee",
                            tint = TkAccent
                        )
                    }

                    IconButton(
                        onClick = onAddVehicleClick,
                        modifier = Modifier
                            .size(40.dp)
                            .clip(RoundedCornerShape(10.dp))
                            .background(TkSurfaceElevated)
                    ) {
                        Icon(
                            imageVector = Icons.Default.Add,
                            contentDescription = "Add Vehicle",
                            tint = TkAccent
                        )
                    }
                }
            }
        },
        containerColor = TkBg,
        modifier = modifier
    ) { innerPadding ->
        if (vehicles.isEmpty()) {
            EmptyGarageState(
                onAddVehicleClick = onAddVehicleClick,
                modifier = Modifier.padding(innerPadding)
            )
        } else {
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding)
                    .padding(horizontal = 20.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                items(vehicles) { vehicle ->
                    VehicleBayCard(
                        vehicle = vehicle,
                        onCardClick = { onVehicleClick(vehicle.id) },
                        onLogClick = { onLogServiceClick(vehicle.id) }
                    )
                }
                item {
                    Spacer(modifier = Modifier.height(24.dp))
                }
            }
        }
    }
}

@Composable
fun VehicleBayCard(
    vehicle: Vehicle,
    onCardClick: () -> Unit,
    onLogClick: () -> Unit
) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onCardClick() },
        shape = RoundedCornerShape(16.dp),
        colors = CardDefaults.cardColors(containerColor = TkSurfaceCard)
    ) {
        Column(modifier = Modifier.padding(18.dp)) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = "${vehicle.year} ${vehicle.make.uppercase()} ${vehicle.model.uppercase()}",
                        color = TkText,
                        fontSize = 17.sp,
                        fontWeight = FontWeight.Bold
                    )
                    if (vehicle.name.isNotBlank()) {
                        Text(
                            text = vehicle.name,
                            color = TkTextMuted,
                            fontSize = 13.sp
                        )
                    }
                }

                Box(
                    modifier = Modifier
                        .size(38.dp)
                        .clip(RoundedCornerShape(8.dp))
                        .background(TkSurfaceElevated),
                    contentAlignment = Alignment.Center
                ) {
                    Icon(
                        imageVector = Icons.Default.DirectionsCar,
                        contentDescription = null,
                        tint = TkAccent,
                        modifier = Modifier.size(20.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(14.dp))

            OdometerWidget(
                mileage = vehicle.currentOdometer,
                unit = vehicle.odometerUnit
            )

            Spacer(modifier = Modifier.height(12.dp))

            MaintenanceStatusBanner(
                status = StatusLevel.UP_TO_DATE,
                message = "All scheduled services up to date"
            )

            Spacer(modifier = Modifier.height(14.dp))

            NoinButton(
                text = "+ Log Service",
                onClick = onLogClick
            )
        }
    }
}

@Composable
fun EmptyGarageState(
    onAddVehicleClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier
            .fillMaxSize()
            .padding(24.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Box(
                modifier = Modifier
                    .size(72.dp)
                    .clip(RoundedCornerShape(18.dp))
                    .background(TkSurfaceCard),
                contentAlignment = Alignment.Center
            ) {
                Icon(
                    imageVector = Icons.Default.DirectionsCar,
                    contentDescription = null,
                    tint = TkAccent,
                    modifier = Modifier.size(36.dp)
                )
            }
            Spacer(modifier = Modifier.height(18.dp))
            Text(
                text = "Your Garage is Empty",
                color = TkText,
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold
            )
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = "Add your car, truck, or motorcycle to start tracking maintenance with zero accounts or subscriptions.",
                color = TkTextMuted,
                fontSize = 14.sp,
                textAlign = androidx.compose.ui.text.style.TextAlign.Center,
                modifier = Modifier.padding(horizontal = 16.dp)
            )
            Spacer(modifier = Modifier.height(24.dp))
            NoinButton(
                text = "Park Your First Vehicle",
                onClick = onAddVehicleClick,
                modifier = Modifier.width(260.dp)
            )
        }
    }
}
