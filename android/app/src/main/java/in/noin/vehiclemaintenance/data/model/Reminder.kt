package in.noin.vehiclemaintenance.data.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey
import java.util.UUID

@Entity(
    tableName = "reminders",
    foreignKeys = [
        ForeignKey(
            entity = Vehicle::class,
            parentColumns = ["id"],
            childColumns = ["vehicle_id"],
            onDelete = ForeignKey.CASCADE
        )
    ],
    indices = [
        Index(value = ["vehicle_id", "is_dismissed"]),
        Index(value = ["due_date"])
    ]
)
data class Reminder(
    @PrimaryKey
    val id: String = UUID.randomUUID().toString(),
    @ColumnInfo(name = "vehicle_id")
    val vehicleId: String,
    @ColumnInfo(name = "service_type")
    val serviceType: String,
    val title: String,
    @ColumnInfo(name = "due_odometer")
    val dueOdometer: Int? = null,
    @ColumnInfo(name = "due_date")
    val dueDate: Long? = null,
    @ColumnInfo(name = "interval_miles")
    val intervalMiles: Int? = null,
    @ColumnInfo(name = "interval_months")
    val intervalMonths: Int? = null,
    @ColumnInfo(name = "is_dismissed")
    val isDismissed: Boolean = false,
    @ColumnInfo(name = "last_notified_at")
    val lastNotifiedAt: Long? = null,
    @ColumnInfo(name = "created_at")
    val createdAt: Long = System.currentTimeMillis(),
    @ColumnInfo(name = "updated_at")
    val updatedAt: Long = System.currentTimeMillis()
)
