package noin.vehiclemaintenance.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import noin.vehiclemaintenance.data.model.ServiceLog
import noin.vehiclemaintenance.data.repository.VehicleRepository
import noin.vehiclemaintenance.ui.components.QuickServiceTile
import noin.vehiclemaintenance.ui.components.StandardCategories
import noin.vehiclemaintenance.ui.components.NoinButton
import noin.vehiclemaintenance.ui.theme.*
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun QuickLogEntryScreen(
    vehicleId: String,
    repository: VehicleRepository,
    onNavigateBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    val coroutineScope = rememberCoroutineScope()
    val vehicle by repository.getVehicle(vehicleId).collectAsState(initial = null)

    var selectedCategoryKey by remember { mutableStateOf("oil_change") }
    var title by remember { mutableStateOf("Full Synthetic Oil & Filter") }
    var odometerText by remember { mutableStateOf("") }
    var costText by remember { mutableStateOf("") }
    var providerText by remember { mutableStateOf("DIY / Home") }
    var partNumbersText by remember { mutableStateOf("") }
    var notesText by remember { mutableStateOf("") }

    // Prefill odometer from vehicle if empty
    LaunchedEffect(vehicle) {
        if (odometerText.isEmpty() && vehicle != null && vehicle!!.currentOdometer > 0) {
            odometerText = vehicle!!.currentOdometer.toString()
        }
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Log Maintenance",
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
                .padding(horizontal = 20.dp, vertical = 12.dp)
        ) {
            Text(
                text = "SERVICE TYPE",
                color = TkAccent,
                fontSize = 12.sp,
                fontWeight = FontWeight.Bold,
                letterSpacing = 1.sp
            )
            Spacer(modifier = Modifier.height(10.dp))

            // Quick Category Selector Row
            LazyRow(
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                modifier = Modifier.fillMaxWidth()
            ) {
                items(StandardCategories) { category ->
                    QuickServiceTile(
                        category = category,
                        isSelected = selectedCategoryKey == category.key,
                        onSelect = {
                            selectedCategoryKey = category.key
                            title = when (category.key) {
                                "oil_change" -> "Full Synthetic Oil & Filter"
                                "tire_rotation" -> "Tire Rotation & Balance"
                                "brakes" -> "Front & Rear Brake Pads"
                                "battery" -> "12V AGM Battery Replacement"
                                else -> "Custom Service"
                            }
                        },
                        modifier = Modifier.width(105.dp)
                    )
                }
            }

            Spacer(modifier = Modifier.height(20.dp))

            // Title Input
            OutlinedTextField(
                value = title,
                onValueChange = { title = it },
                label = { Text("Service Description") },
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

            // Odometer Input
            OutlinedTextField(
                value = odometerText,
                onValueChange = { odometerText = it.filter { char -> char.isDigit() } },
                label = { Text("Odometer at Service (${vehicle?.odometerUnit ?: "mi"})") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
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

            // Cost Input
            OutlinedTextField(
                value = costText,
                onValueChange = { costText = it },
                label = { Text("Total Cost (${vehicle?.currencyCode ?: "$"})") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
                placeholder = { Text("45.00") },
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

            // Service Provider
            OutlinedTextField(
                value = providerText,
                onValueChange = { providerText = it },
                label = { Text("Service Performed By (DIY / Shop Name)") },
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

            // Part Numbers
            OutlinedTextField(
                value = partNumbersText,
                onValueChange = { partNumbersText = it },
                label = { Text("Part Numbers / Oil Weight (Optional)") },
                placeholder = { Text("e.g. 5W-30 Mobil1 (5qt), Filter #15400") },
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

            // Notes
            OutlinedTextField(
                value = notesText,
                onValueChange = { notesText = it },
                label = { Text("Mechanic Notes (Optional)") },
                minLines = 2,
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
                text = "Save Service Record",
                enabled = title.isNotBlank() && odometerText.isNotBlank(),
                onClick = {
                    coroutineScope.launch {
                        val parsedOdometer = odometerText.toIntOrNull() ?: 0
                        val parsedCostCents = ((costText.toDoubleOrNull() ?: 0.0) * 100).toInt()

                        val newLog = ServiceLog(
                            vehicleId = vehicleId,
                            serviceType = selectedCategoryKey,
                            title = title,
                            odometer = parsedOdometer,
                            costCents = parsedCostCents,
                            serviceProvider = providerText.ifBlank { "DIY" },
                            partNumbers = partNumbersText.ifBlank { null },
                            notes = notesText.ifBlank { null }
                        )

                        repository.logService(newLog)
                        onNavigateBack()
                    }
                }
            )

            Spacer(modifier = Modifier.height(24.dp))
        }
    }
}
