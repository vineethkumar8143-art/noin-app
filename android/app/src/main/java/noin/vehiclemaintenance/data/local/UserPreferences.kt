package noin.vehiclemaintenance.data.local

import android.content.Context
import android.content.SharedPreferences
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class UserPreferences(context: Context) {
    private val prefs: SharedPreferences = context.getSharedPreferences("noin_prefs", Context.MODE_PRIVATE)

    private val _isProUnlocked = MutableStateFlow(prefs.getBoolean(KEY_PRO_UNLOCKED, false))
    val isProUnlocked: StateFlow<Boolean> = _isProUnlocked.asStateFlow()

    private val _isOnboardingCompleted = MutableStateFlow(prefs.getBoolean(KEY_ONBOARDING_COMPLETED, false))
    val isOnboardingCompleted: StateFlow<Boolean> = _isOnboardingCompleted.asStateFlow()

    fun setProUnlocked(unlocked: Boolean) {
        prefs.edit().putBoolean(KEY_PRO_UNLOCKED, unlocked).apply()
        _isProUnlocked.value = unlocked
    }

    fun setOnboardingCompleted(completed: Boolean) {
        prefs.edit().putBoolean(KEY_ONBOARDING_COMPLETED, completed).apply()
        _isOnboardingCompleted.value = completed
    }

    companion object {
        private const val KEY_PRO_UNLOCKED = "key_pro_unlocked"
        private const val KEY_ONBOARDING_COMPLETED = "key_onboarding_completed"
    }
}
