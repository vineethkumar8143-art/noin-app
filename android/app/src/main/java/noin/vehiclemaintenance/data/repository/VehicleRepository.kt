package noin.vehiclemaintenance.data.repository

import noin.vehiclemaintenance.data.local.FuelLogDao
import noin.vehiclemaintenance.data.local.ReminderDao
import noin.vehiclemaintenance.data.local.ServiceLogDao
import noin.vehiclemaintenance.data.local.TreadLogDao
import noin.vehiclemaintenance.data.local.VehicleDao
import noin.vehiclemaintenance.data.model.FuelLog
import noin.vehiclemaintenance.data.model.Reminder
import noin.vehiclemaintenance.data.model.ServiceLog
import noin.vehiclemaintenance.data.model.TreadLog
import noin.vehiclemaintenance.data.model.Vehicle
import kotlinx.coroutines.flow.Flow

class VehicleRepository(
    private val vehicleDao: VehicleDao,
    private val serviceLogDao: ServiceLogDao,
    private val reminderDao: ReminderDao,
    private val fuelLogDao: FuelLogDao? = null,
    private val treadLogDao: TreadLogDao? = null
) {
    // Vehicles
    fun getAllVehicles(): Flow<List<Vehicle>> = vehicleDao.getAllActiveVehicles()
    fun getVehicle(id: String): Flow<Vehicle?> = vehicleDao.getVehicleById(id)
    suspend fun getVehicleDirect(id: String): Vehicle? = vehicleDao.getVehicleByIdDirect(id)
    suspend fun saveVehicle(vehicle: Vehicle) = vehicleDao.insertVehicle(vehicle)
    suspend fun deleteVehicle(vehicle: Vehicle) = vehicleDao.deleteVehicle(vehicle)

    // Service Logs
    fun getLogsForVehicle(vehicleId: String): Flow<List<ServiceLog>> = serviceLogDao.getLogsForVehicle(vehicleId)
    suspend fun getLogsForVehicleDirect(vehicleId: String): List<ServiceLog> = serviceLogDao.getLogsForVehicleDirect(vehicleId)
    fun getTotalCost(vehicleId: String): Flow<Int?> = serviceLogDao.getTotalCostForVehicle(vehicleId)
    
    suspend fun logService(log: ServiceLog) {
        serviceLogDao.insertLog(log)
        // Auto-update vehicle odometer if this service odometer is higher
        val vehicle = vehicleDao.getVehicleByIdDirect(log.vehicleId)
        if (vehicle != null && log.odometer > vehicle.currentOdometer) {
            vehicleDao.updateOdometer(log.vehicleId, log.odometer)
        }
    }

    suspend fun deleteLog(log: ServiceLog) = serviceLogDao.deleteLog(log)

    // Fuel Logs
    fun getFuelLogsForVehicle(vehicleId: String): Flow<List<FuelLog>>? = fuelLogDao?.getFuelLogsForVehicle(vehicleId)
    suspend fun getFuelLogsForVehicleDirect(vehicleId: String): List<FuelLog> = fuelLogDao?.getFuelLogsForVehicleDirect(vehicleId) ?: emptyList()
    fun getTotalFuelCost(vehicleId: String): Flow<Int?>? = fuelLogDao?.getTotalFuelCostForVehicle(vehicleId)
    fun getAverageMpg(vehicleId: String): Flow<Double?>? = fuelLogDao?.getAverageMpgForVehicle(vehicleId)

    suspend fun logFuel(log: FuelLog) {
        if (fuelLogDao == null) return
        val previousLog = fuelLogDao.getLatestFuelLog(log.vehicleId)
        val calculatedMpg = if (previousLog != null && log.odometer > previousLog.odometer && log.volume > 0) {
            (log.odometer - previousLog.odometer) / log.volume
        } else {
            null
        }
        val finalLog = log.copy(calculatedMpg = calculatedMpg)
        fuelLogDao.insertFuelLog(finalLog)

        val vehicle = vehicleDao.getVehicleByIdDirect(log.vehicleId)
        if (vehicle != null && log.odometer > vehicle.currentOdometer) {
            vehicleDao.updateOdometer(log.vehicleId, log.odometer)
        }
    }

    suspend fun deleteFuelLog(log: FuelLog) = fuelLogDao?.deleteFuelLog(log)

    // Tire Tread Logs
    fun getTreadLogsForVehicle(vehicleId: String): Flow<List<TreadLog>>? = treadLogDao?.getTreadLogsForVehicle(vehicleId)
    fun getLatestTreadLog(vehicleId: String): Flow<TreadLog?>? = treadLogDao?.getLatestTreadLog(vehicleId)
    suspend fun logTread(log: TreadLog) {
        if (treadLogDao == null) return
        treadLogDao.insertTreadLog(log)
        val vehicle = vehicleDao.getVehicleByIdDirect(log.vehicleId)
        if (vehicle != null && log.odometer > vehicle.currentOdometer) {
            vehicleDao.updateOdometer(log.vehicleId, log.odometer)
        }
    }

    // Reminders
    fun getActiveReminders(vehicleId: String): Flow<List<Reminder>> = reminderDao.getActiveRemindersForVehicle(vehicleId)
    suspend fun saveReminder(reminder: Reminder) = reminderDao.insertReminder(reminder)
    suspend fun dismissReminder(id: String) = reminderDao.dismissReminder(id)
}
