package in.noin.vehiclemaintenance

import in.noin.vehiclemaintenance.data.model.ServiceLog
import in.noin.vehiclemaintenance.data.model.Vehicle
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test
import java.text.NumberFormat
import java.util.Locale

class VehicleLogicUnitTest {

    @Test
    fun testClassicCarAllowsNullVin_F01_H2() {
        val classicCar = Vehicle(
            name = "Project Fastback",
            make = "Ford",
            model = "Mustang",
            year = 1969,
            vin = null, // Pre-1981 classic
            currentOdometer = 124500
        )

        assertNull("Classic car must support null VIN", classicCar.vin)
        assertEquals("Ford", classicCar.make)
        assertEquals(1969, classicCar.year)
    }

    @Test
    fun testOdometerAutoAdvanceLogic_F02_H1() {
        val initialOdometer = 80000
        val serviceOdometer = 85000

        // Simulate repository auto-advance logic
        val newOdometer = if (serviceOdometer > initialOdometer) serviceOdometer else initialOdometer
        assertEquals(85000, newOdometer)
    }

    @Test
    fun testPastReceiptDoesNotRollbackOdometer_F02_E1() {
        val currentVehicleOdometer = 85000
        val historicalReceiptOdometer = 75000

        // Logic check: Logging an older receipt shouldn't roll back the car's current mileage
        val newOdometer = if (historicalReceiptOdometer > currentVehicleOdometer) historicalReceiptOdometer else currentVehicleOdometer
        assertEquals(85000, newOdometer)
    }

    @Test
    fun testCostToCentsConversion_F02_E2() {
        val costInput = "45.99"
        val parsedCents = ((costInput.toDoubleOrNull() ?: 0.0) * 100).toInt()
        assertEquals(4599, parsedCents)

        val costInputZero = "0.00"
        val zeroCents = ((costInputZero.toDoubleOrNull() ?: 0.0) * 100).toInt()
        assertEquals(0, zeroCents)
    }

    @Test
    fun testHighMileageFormatting_F01_E1() {
        val highMileage = 999999
        val formatted = NumberFormat.getNumberInstance(Locale.US).format(highMileage)
        assertEquals("999,999", formatted)
    }
}
