package in.noin.vehiclemaintenance.data.local

import androidx.room.*
import in.noin.vehiclemaintenance.data.model.Vehicle
import kotlinx.coroutines.flow.Flow

@Dao
interface VehicleDao {
    @Query("SELECT * FROM vehicles WHERE is_archived = 0 ORDER BY updated_at DESC")
    fun getAllActiveVehicles(): Flow<List<Vehicle>>

    @Query("SELECT * FROM vehicles WHERE id = :id LIMIT 1")
    fun getVehicleById(id: String): Flow<Vehicle?>

    @Query("SELECT * FROM vehicles WHERE id = :id LIMIT 1")
    suspend fun getVehicleByIdDirect(id: String): Vehicle?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertVehicle(vehicle: Vehicle)

    @Update
    suspend fun updateVehicle(vehicle: Vehicle)

    @Query("UPDATE vehicles SET current_odometer = :odometer, updated_at = :timestamp WHERE id = :vehicleId")
    suspend fun updateOdometer(vehicleId: String, odometer: Int, timestamp: Long = System.currentTimeMillis())

    @Delete
    suspend fun deleteVehicle(vehicle: Vehicle)
}
