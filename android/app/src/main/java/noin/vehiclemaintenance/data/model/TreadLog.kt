package noin.vehiclemaintenance.data.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey
import java.util.UUID

@Entity(
    tableName = "tread_logs",
    foreignKeys = [
        ForeignKey(
            entity = Vehicle::class,
            parentColumns = ["id"],
            childColumns = ["vehicle_id"],
            onDelete = ForeignKey.CASCADE
        )
    ],
    indices = [
        Index(value = ["vehicle_id", "measured_date"])
    ]
)
data class TreadLog(
    @PrimaryKey
    val id: String = UUID.randomUUID().toString(),
    @ColumnInfo(name = "vehicle_id")
    val vehicleId: String,
    @ColumnInfo(name = "measured_date")
    val measuredDate: Long = System.currentTimeMillis(),
    val odometer: Int,
    @ColumnInfo(name = "fl_32nds")
    val fl32nds: Int, // Front Left (e.g. 8)
    @ColumnInfo(name = "fr_32nds")
    val fr32nds: Int, // Front Right (e.g. 8)
    @ColumnInfo(name = "rl_32nds")
    val rl32nds: Int, // Rear Left (e.g. 7)
    @ColumnInfo(name = "rr_32nds")
    val rr32nds: Int, // Rear Right (e.g. 7)
    @ColumnInfo(name = "condition_rating")
    val conditionRating: String, // "good", "warning", "critical"
    val notes: String? = null,
    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis(),
    @ColumnInfo(name = "updated_at")
    val updatedAt: Long = System.currentTimeMillis()
)
