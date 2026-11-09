package noin.vehiclemaintenance.data.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey
import java.util.UUID

@Entity(
    tableName = "fuel_logs",
    foreignKeys = [
        ForeignKey(
            entity = Vehicle::class,
            parentColumns = ["id"],
            childColumns = ["vehicle_id"],
            onDelete = ForeignKey.CASCADE
        )
    ],
    indices = [
        Index(value = ["vehicle_id", "fuel_date"])
    ]
)
data class FuelLog(
    @PrimaryKey
    val id: String = UUID.randomUUID().toString(),
    @ColumnInfo(name = "vehicle_id")
    val vehicleId: String,
    @ColumnInfo(name = "fuel_date")
    val fuelDate: Long = System.currentTimeMillis(),
    val odometer: Int,
    @ColumnInfo(name = "volume_liters_or_gallons")
    val volume: Double,
    @ColumnInfo(name = "total_cost_cents")
    val totalCostCents: Int,
    @ColumnInfo(name = "is_full_tank")
    val isFullTank: Boolean = true,
    @ColumnInfo(name = "calculated_mpg")
    val calculatedMpg: Double? = null,
    val notes: String? = null,
    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis(),
    @ColumnInfo(name = "updated_at")
    val updatedAt: Long = System.currentTimeMillis()
)
