package noin.vehiclemaintenance.data.local

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import noin.vehiclemaintenance.data.model.FuelLog
import noin.vehiclemaintenance.data.model.Reminder
import noin.vehiclemaintenance.data.model.ServiceLog
import noin.vehiclemaintenance.data.model.TreadLog
import noin.vehiclemaintenance.data.model.Vehicle

@Database(
    entities = [Vehicle::class, ServiceLog::class, Reminder::class, FuelLog::class, TreadLog::class],
    version = 2,
    exportSchema = false
)
abstract class NoinDatabase : RoomDatabase() {
    abstract fun vehicleDao(): VehicleDao
    abstract fun serviceLogDao(): ServiceLogDao
    abstract fun reminderDao(): ReminderDao
    abstract fun fuelLogDao(): FuelLogDao
    abstract fun treadLogDao(): TreadLogDao

    companion object {
        @Volatile
        private var INSTANCE: NoinDatabase? = null

        fun getDatabase(context: Context): NoinDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    NoinDatabase::class.java,
                    "noin.db"
                ).fallbackToDestructiveMigration().build()
                INSTANCE = instance
                instance
            }
        }
    }
}
