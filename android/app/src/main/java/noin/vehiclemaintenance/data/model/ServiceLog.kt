package noin.vehiclemaintenance.data.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey
import java.util.UUID

@Entity(
    tableName = "service_logs",
    foreignKeys = [
        ForeignKey(
            entity = Vehicle::class,
            parentColumns = ["id"],
            childColumns = ["vehicle_id"],
            onDelete = ForeignKey.CASCADE
        )
    ],
    indices = [
        Index(value = ["vehicle_id", "service_date"]),
        Index(value = ["service_type"])
    ]
)
data class ServiceLog(
    @PrimaryKey
    val id: String = UUID.randomUUID().toString(),
    @ColumnInfo(name = "vehicle_id")
    val vehicleId: String,
    @ColumnInfo(name = "service_type")
    val serviceType: String, // "oil_change", "tire_rotation", "brakes", "battery", "custom"
    val title: String,
    val odometer: Int,
    @ColumnInfo(name = "cost_cents")
    val costCents: Int = 0,
    @ColumnInfo(name = "service_date")
    val serviceDate: Long = System.currentTimeMillis(),
    @ColumnInfo(name = "service_provider")
    val serviceProvider: String? = "DIY",
    @ColumnInfo(name = "part_numbers")
    val partNumbers: String? = null,
    val notes: String? = null,
    @ColumnInfo(name = "receipt_image_path")
    val receiptImagePath: String? = null,
    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis(),
    @ColumnInfo(name = "updated_at")
    val updatedAt: Long = System.currentTimeMillis()
)
