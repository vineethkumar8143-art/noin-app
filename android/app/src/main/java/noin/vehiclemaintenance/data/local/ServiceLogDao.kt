package noin.vehiclemaintenance.data.local

import androidx.room.*
import noin.vehiclemaintenance.data.model.ServiceLog
import kotlinx.coroutines.flow.Flow

@Dao
interface ServiceLogDao {
    @Query("SELECT * FROM service_logs WHERE vehicle_id = :vehicleId ORDER BY service_date DESC, odometer DESC")
    fun getLogsForVehicle(vehicleId: String): Flow<List<ServiceLog>>

    @Query("SELECT * FROM service_logs WHERE vehicle_id = :vehicleId ORDER BY service_date DESC")
    suspend fun getLogsForVehicleDirect(vehicleId: String): List<ServiceLog>

    @Query("SELECT * FROM service_logs WHERE id = :id LIMIT 1")
    fun getLogById(id: String): Flow<ServiceLog?>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertLog(log: ServiceLog)

    @Update
    suspend fun updateLog(log: ServiceLog)

    @Delete
    suspend fun deleteLog(log: ServiceLog)

    @Query("SELECT SUM(cost_cents) FROM service_logs WHERE vehicle_id = :vehicleId")
    fun getTotalCostForVehicle(vehicleId: String): Flow<Int?>
}
