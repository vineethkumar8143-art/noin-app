package noin.vehiclemaintenance.data.local

import androidx.room.*
import noin.vehiclemaintenance.data.model.Reminder
import kotlinx.coroutines.flow.Flow

@Dao
interface ReminderDao {
    @Query("SELECT * FROM reminders WHERE vehicle_id = :vehicleId AND is_dismissed = 0 ORDER BY due_date ASC, due_odometer ASC")
    fun getActiveRemindersForVehicle(vehicleId: String): Flow<List<Reminder>>

    @Query("SELECT * FROM reminders WHERE is_dismissed = 0")
    suspend fun getAllPendingRemindersDirect(): List<Reminder>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertReminder(reminder: Reminder)

    @Update
    suspend fun updateReminder(reminder: Reminder)

    @Query("UPDATE reminders SET is_dismissed = 1, updated_at = :timestamp WHERE id = :id")
    suspend fun dismissReminder(id: String, timestamp: Long = System.currentTimeMillis())

    @Delete
    suspend fun deleteReminder(reminder: Reminder)
}
