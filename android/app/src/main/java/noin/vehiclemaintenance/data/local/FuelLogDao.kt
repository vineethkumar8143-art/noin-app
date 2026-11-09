package noin.vehiclemaintenance.data.local

import androidx.room.*
import noin.vehiclemaintenance.data.model.FuelLog
import kotlinx.coroutines.flow.Flow

@Dao
interface FuelLogDao {
    @Query("SELECT * FROM fuel_logs WHERE vehicle_id = :vehicleId ORDER BY fuel_date DESC, odometer DESC")
    fun getFuelLogsForVehicle(vehicleId: String): Flow<List<FuelLog>>

    @Query("SELECT * FROM fuel_logs WHERE vehicle_id = :vehicleId ORDER BY odometer DESC LIMIT 1")
    suspend fun getLatestFuelLog(vehicleId: String): FuelLog?

    @Query("SELECT * FROM fuel_logs WHERE vehicle_id = :vehicleId ORDER BY fuel_date DESC")
    suspend fun getFuelLogsForVehicleDirect(vehicleId: String): List<FuelLog>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertFuelLog(log: FuelLog)

    @Update
    suspend fun updateFuelLog(log: FuelLog)

    @Delete
    suspend fun deleteFuelLog(log: FuelLog)

    @Query("SELECT SUM(total_cost_cents) FROM fuel_logs WHERE vehicle_id = :vehicleId")
    fun getTotalFuelCostForVehicle(vehicleId: String): Flow<Int?>

    @Query("SELECT AVG(calculated_mpg) FROM fuel_logs WHERE vehicle_id = :vehicleId AND calculated_mpg IS NOT NULL")
    fun getAverageMpgForVehicle(vehicleId: String): Flow<Double?>
}
