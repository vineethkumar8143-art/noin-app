# 🧪 Noin Master Test Plan
## Project: Vehicle Maintenance App - Noin

> **Scope:** End-to-end verification of all core flows, offline Room SQLite queries, data integrity, PDF dossier generation, and edge cases.
> **Standard:** `replica-test` specification.

---

## 1. Flow Matrix & Test Cases

### Flow 1: Vehicle Onboarding (Park Vehicle)
* **F01-H1 (Happy Path - Modern Car):**
  * Steps: Tap "+ Park Vehicle", enter Year `2021`, Make `Toyota`, Model `Rav4`, Odometer `35,000 mi`, VIN `2T3C1RFV5MC...`. Tap "Park in Garage Bay".
  * Expected: New card appears on Garage Home with `35,000 MI`, status `All scheduled maintenance is up to date`.
* **F01-H2 (Happy Path - Classic Car / Pre-1981 / No VIN):**
  * Steps: Enter Year `1969`, Make `Ford`, Model `Mustang`, leave VIN blank. Tap "Park in Garage Bay".
  * Expected: Card successfully created without validation error. Solves the #1 complaint of existing apps blocking classic cars.
* **F01-E1 (Edge Case - High Mileage Odometer):**
  * Steps: Enter Odometer `999,999`.
  * Expected: Formats cleanly with commas (`999,999 MI`) without clipping layout.
* **F01-E2 (Edge Case - Trailing/Leading Whitespace):**
  * Steps: Enter Make `  Honda  `, Model `  Civic  `.
  * Expected: Database trims values to `Honda` and `Civic`.
* **F01-N1 (Negative Case - Missing Required Fields):**
  * Steps: Leave Make and Model blank.
  * Expected: "Park in Garage Bay" button remains disabled; cannot submit empty form.

---

### Flow 2: Quick Service Entry (Log Service)
* **F02-H1 (Happy Path - Quick Tile Logging):**
  * Steps: From Garage Home, tap "+ Log Service" on active vehicle. Select `Oil & Filter` tile, verify prefilled title `"Full Synthetic Oil & Filter"`. Enter Odometer `85,000`, Cost `$45.50`. Tap "Save Service Record".
  * Expected: Record saved to `service_logs`. Vehicle odometer automatically advances from previous reading to `85,000 mi`.
* **F02-E1 (Edge Case - Lower Odometer Than Current):**
  * Steps: Current vehicle odometer is `85,000`. User logs a past historical receipt at `80,000 mi`.
  * Expected: Service record is successfully logged at `80,000 mi`, but vehicle's current odometer remains `85,000 mi` (does not roll back).
* **F02-E2 (Edge Case - Decimal Costs & Cent Conversion):**
  * Steps: Enter Cost `45.99`.
  * Expected: Stored cleanly as `4599` integer cents in Room DB, preventing floating-point rounding errors.
* **F02-N1 (Negative Case - Non-Numeric Odometer Input):**
  * Steps: Paste text `"abc"` into odometer field.
  * Expected: Number filter discards invalid non-digit characters.

---

### Flow 3: Buyer Resale Dossier Generation
* **F03-H1 (Happy Path - Generate PDF):**
  * Steps: From Vehicle Detail Bay, tap PDF icon. Review summary metrics. Tap "Export & Share Dossier (PDF)".
  * Expected: Native `PdfDocument` generates multi-column A4 document with vehicle header, service history, and total investment. Android native share sheet opens via `FileProvider`.
* **F03-E1 (Edge Case - Empty Service History):**
  * Steps: Create brand new vehicle with 0 service logs. Navigate to Dossier screen.
  * Expected: Export button is disabled; displays guidance message prompting user to log at least one service record.
* **F03-E2 (Edge Case - Long Part Numbers & Notes):**
  * Steps: Log service with part numbers exceeding 50 characters (e.g., `Mobil1 5W-30 (5qt) + OEM Filter 15400-PLM-A02 + Crush Washer`).
  * Expected: PDF text truncates gracefully or line-wraps without overlapping adjacent columns.

---

### Flow 4: Offline Resilience & Privacy Guarantee
* **F04-H1 (Happy Path - Airplane Mode Operation):**
  * Steps: Enable Airplane Mode (no WiFi, no cellular). Perform vehicle creation, service logging, and PDF generation.
  * Expected: App operates at 100% full capacity. Zero network error dialogs. Zero latency.
* **F04-N1 (Negative Case - Zero Shady Permissions):**
  * Steps: Check app permissions in Android Settings.
  * Expected: Only standard `POST_NOTIFICATIONS` (Android 13+). Zero requests for GPS location, camera roll access, contacts, or phone state.

---

## 2. Test Execution Checklist

| Test ID | Flow | Description | Method | Status |
|---|---|---|---|---|
| **F01-H1** | Onboarding | Modern car with VIN | Unit / Logic Test | **PASS** |
| **F01-H2** | Onboarding | Classic car pre-1981 (Null VIN) | Unit / Logic Test | **PASS** |
| **F01-E1** | Onboarding | 999,999 High mileage formatting | NumberFormat Check | **PASS** |
| **F01-N1** | Onboarding | Blank input validation | UI Logic Check | **PASS** |
| **F02-H1** | Service Log | Quick tile + auto odometer advance | Repository Test | **PASS** |
| **F02-E1** | Service Log | Past record doesn't roll back odo | Logic Test | **PASS** |
| **F02-E2** | Service Log | Float to Integer cent accuracy | Currency Unit Test | **PASS** |
| **F03-H1** | Dossier | PDF creation & FileProvider URI | PDF Engine Test | **PASS** |
| **F03-E1** | Dossier | Empty history disables export | UI State Check | **PASS** |
| **F04-H1** | Resilience | 100% offline functionality | Architectural Check| **PASS** |
| **F04-H2** | Privacy | Privacy Guarantee navigation, audit list & data purge | UI & State Check | **PASS** |
| **F04-N1** | Privacy | Zero shady permissions (no location, no contacts) | Manifest Security Audit | **PASS** |
