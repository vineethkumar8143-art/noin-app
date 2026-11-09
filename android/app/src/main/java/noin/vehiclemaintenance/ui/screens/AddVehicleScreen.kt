package noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.data.model.Vehicle
import noin.vehiclemaintenance.data.repository.VehicleRepository
import noin.vehiclemaintenance.ui.components.NoinButton
import noin.vehiclemaintenance.ui.theme.*
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddVehicleScreen(
    repository: VehicleRepository,
    onNavigateBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    val coroutineScope = rememberCoroutineScope()

    var nickname by remember { mutableStateOf("") }
    var yearText by remember { mutableStateOf("2020") }
    var make by remember { mutableStateOf("") }
    var model by remember { mutableStateOf("") }
    var odometerText by remember { mutableStateOf("0") }
    var vinText by remember { mutableStateOf("") }
    var unitSelected by remember { mutableStateOf("mi") } // "mi" or "km"

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Park New Vehicle",
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
                .padding(horizontal = 20.dp, vertical = 16.dp)
        ) {
            // Make
            OutlinedTextField(
                value = make,
                onValueChange = { make = it },
                label = { Text("Make (e.g. Toyota, Ford, Honda)") },
                modifier = Modifier.fillMaxWidth(),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = TkAccent,
                    unfocusedBorderColor = TkBorderInput,
                    focusedLabelColor = TkAccent,
                    unfocusedLabelColor = TkTextMuted,
                    focusedTextColor = TkText,
                    unfocusedTextColor = TkText
                ),
                shape = RoundedCornerShape(10.dp)
            )

            Spacer(modifier = Modifier.height(14.dp))

            // Model
            OutlinedTextField(
                value = model,
                onValueChange = { model = it },
                label = { Text("Model (e.g. Tacoma, Mustang, Civic)") },
                modifier = Modifier.fillMaxWidth(),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = TkAccent,
                    unfocusedBorderColor = TkBorderInput,
                    focusedLabelColor = TkAccent,
                    unfocusedLabelColor = TkTextMuted,
                    focusedTextColor = TkText,
                    unfocusedTextColor = TkText
                ),
                shape = RoundedCornerShape(10.dp)
            )

            Spacer(modifier = Modifier.height(14.dp))

            // Year & Unit Row
            Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                OutlinedTextField(
                    value = yearText,
                    onValueChange = { yearText = it.filter { c -> c.isDigit() } },
                    label = { Text("Year") },
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    modifier = Modifier.weight(1f),
                    colors = OutlinedTextFieldDefaults.colors(
                        focusedBorderColor = TkAccent,
                        unfocusedBorderColor = TkBorderInput,
                        focusedLabelColor = TkAccent,
                        unfocusedLabelColor = TkTextMuted,
                        focusedTextColor = TkText,
                        unfocusedTextColor = TkText
                    ),
                    shape = RoundedCornerShape(10.dp)
                )

                OutlinedTextField(
                    value = odometerText,
                    onValueChange = { odometerText = it.filter { c -> c.isDigit() } },
                    label = { Text("Starting Odometer") },
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    modifier = Modifier.weight(1.5f),
                    colors = OutlinedTextFieldDefaults.colors(
                        focusedBorderColor = TkAccent,
                        unfocusedBorderColor = TkBorderInput,
                        focusedLabelColor = TkAccent,
                        unfocusedLabelColor = TkTextMuted,
                        focusedTextColor = TkText,
                        unfocusedTextColor = TkText
                    ),
                    shape = RoundedCornerShape(10.dp)
                )
            }

            Spacer(modifier = Modifier.height(14.dp))

            // Nickname
            OutlinedTextField(
                value = nickname,
                onValueChange = { nickname = it },
                label = { Text("Nickname (Optional e.g. Daily Driver)") },
                modifier = Modifier.fillMaxWidth(),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = TkAccent,
                    unfocusedBorderColor = TkBorderInput,
                    focusedLabelColor = TkAccent,
                    unfocusedLabelColor = TkTextMuted,
                    focusedTextColor = TkText,
                    unfocusedTextColor = TkText
                ),
                shape = RoundedCornerShape(10.dp)
            )

            Spacer(modifier = Modifier.height(14.dp))

            // VIN (Optional - Directly solves classic car / motorcycle user complaint)
            OutlinedTextField(
                value = vinText,
                onValueChange = { vinText = it.uppercase() },
                label = { Text("VIN (Optional — pre-1981 / classics leave blank)") },
                modifier = Modifier.fillMaxWidth(),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = TkAccent,
                    unfocusedBorderColor = TkBorderInput,
                    focusedLabelColor = TkAccent,
                    unfocusedLabelColor = TkTextMuted,
                    focusedTextColor = TkText,
                    unfocusedTextColor = TkText
                ),
                shape = RoundedCornerShape(10.dp)
            )

            Spacer(modifier = Modifier.height(28.dp))

            NoinButton(
                text = "Park in Garage Bay",
                enabled = make.isNotBlank() && model.isNotBlank() && yearText.isNotBlank(),
                onClick = {
                    coroutineScope.launch {
                        val parsedYear = yearText.toIntOrNull() ?: 2020
                        val parsedOdometer = odometerText.toIntOrNull() ?: 0

                        val newVehicle = Vehicle(
                            name = nickname.ifBlank { "$make $model" },
                            make = make.trim(),
                            model = model.trim(),
                            year = parsedYear,
                            vin = vinText.ifBlank { null },
                            currentOdometer = parsedOdometer,
                            odometerUnit = unitSelected
                        )

                        repository.saveVehicle(newVehicle)
                        onNavigateBack()
                    }
                }
            )
        }
    }
}
