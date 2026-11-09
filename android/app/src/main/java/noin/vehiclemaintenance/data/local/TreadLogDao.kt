package noin.vehiclemaintenance.data.local

import androidx.room.*
import noin.vehiclemaintenance.data.model.TreadLog
import kotlinx.coroutines.flow.Flow

@Dao
interface TreadLogDao {
    @Query("SELECT * FROM tread_logs WHERE vehicle_id = :vehicleId ORDER BY measured_date DESC, odometer DESC")
    fun getTreadLogsForVehicle(vehicleId: String): Flow<List<TreadLog>>

    @Query("SELECT * FROM tread_logs WHERE vehicle_id = :vehicleId ORDER BY measured_date DESC LIMIT 1")
    fun getLatestTreadLog(vehicleId: String): Flow<TreadLog?>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertTreadLog(log: TreadLog)

    @Update
    suspend fun updateTreadLog(log: TreadLog)

    @Delete
    suspend fun deleteTreadLog(log: TreadLog)
}
