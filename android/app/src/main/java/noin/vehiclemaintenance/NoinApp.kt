package noin.vehiclemaintenance

import android.app.Application
import noin.vehiclemaintenance.data.local.NoinDatabase
import noin.vehiclemaintenance.data.repository.VehicleRepository

class NoinApp : Application() {
    val database by lazy { NoinDatabase.getDatabase(this) }
    val repository by lazy {
        VehicleRepository(
            vehicleDao = database.vehicleDao(),
            serviceLogDao = database.serviceLogDao(),
            reminderDao = database.reminderDao(),
            fuelLogDao = database.fuelLogDao(),
            treadLogDao = database.treadLogDao()
        )
    }
}
