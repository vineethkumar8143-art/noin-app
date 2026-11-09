package noin.vehiclemaintenance.data.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey
import java.util.UUID

@Entity(tableName = "vehicles")
data class Vehicle(
    @PrimaryKey
    val id: String = UUID.randomUUID().toString(),
    val name: String,
    val make: String,
    val model: String,
    val year: Int,
    val vin: String? = null,
    @ColumnInfo(name = "license_plate")
    val licensePlate: String? = null,
    @ColumnInfo(name = "current_odometer")
    val currentOdometer: Int = 0,
    @ColumnInfo(name = "odometer_unit")
    val odometerUnit: String = "mi", // "mi" or "km"
    @ColumnInfo(name = "fuel_unit")
    val fuelUnit: String = "gal",    // "gal" or "L"
    @ColumnInfo(name = "currency_code")
    val currencyCode: String = "USD",
    @ColumnInfo(name = "is_archived")
    val isArchived: Boolean = false,
    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis(),
    @ColumnInfo(name = "updated_at")
    val updatedAt: Long = System.currentTimeMillis()
)
