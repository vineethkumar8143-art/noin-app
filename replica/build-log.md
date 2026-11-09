# 🔨 Build Log: Noin Android Application
## Project: Vehicle Maintenance App - Noin

| Screen / Component | Date | Status | Notes / Key Technical Decisions |
|---|---|---|---|
| **Project Setup & Gradle** | 2026-11-07 | Done | Gradle Version Catalog (`libs.versions.toml`), Kotlin 2.0.21, AGP 8.7.2, Room 2.6.1, Jetpack Compose Material 3. Target SDK 35, Min SDK 26. |
| **Room SQLite DB Layer** | 2026-11-07 | Done | `Vehicle`, `ServiceLog`, and `Reminder` entities with cascading foreign keys and indexes. Reactive `Flow` queries in DAOs. Zero server dependency ($0/mo cost). |
| **Design System & Primitives** | 2026-11-07 | Done | Implemented `OdometerWidget`, `QuickServiceTile`, `ServiceRecordItem`, `MaintenanceStatusBanner`, and `TorqueButton` in Compose adhering strictly to `tokens.json`. |
| **S01: Garage Home Screen** | 2026-11-07 | Done | `GarageHomeScreen.kt` with live vehicle cards, empty states, odometer summary, and one-tap "+ Log Service" navigation. |
| **S02: Vehicle Bay Detail** | 2026-11-07 | Done | `VehicleDetailBayScreen.kt` featuring cumulative cost statistics, odometer readout, and chronological timeline with part numbers. |
| **S03: Quick Log Entry** | 2026-11-07 | Done | `QuickLogEntryScreen.kt` featuring 1-tap service category tiles, auto-updating vehicle odometer, and DIY/part number inputs. |
| **S04: Add Vehicle Bay** | 2026-11-07 | Done | `AddVehicleScreen.kt` with optional VIN field (solves pre-1981 classic car complaint) and unit selectors (`mi`/`km`). |
| **S06: Resale Dossier Export** | 2026-11-07 | Done | `DossierExportScreen.kt` + `DossierPdfGenerator.kt` drawing multi-column PDF via native Android `PdfDocument` and sharing via `FileProvider`. |
| **Navigation & App Lifecycle** | 2026-11-07 | Done | `NavHost.kt`, `MainActivity.kt`, and `TorqueKeepApp.kt` wiring repository and navigation graph together. |
| **S05: Privacy Guarantee & Audit** | 2026-11-07 | Done | `PrivacyGuaranteeScreen.kt` with zero-permission verification, 1-tap local data purge, and raw export. |
| **S07: User Onboarding Carousel** | 2026-11-07 | Done | `OnboardingScreen.kt` featuring 3-step value carousel (local-first data ownership, 1-tap logging, buyer resale dossier). |
| **S08: Pricing & Pro Upgrade Bay** | 2026-11-07 | Done | `ProUpgradeScreen.kt` featuring $19.99 Lifetime anchor, $2.99/mo flex pass, full comparison matrix, and Google Play Billing hooks. |
| **Local Preferences & State** | 2026-11-07 | Done | `UserPreferences.kt` providing reactive `StateFlow` flags for Pro unlock and Onboarding status. |
| **Interactive Preview Shell** | 2026-11-07 | Done | `preview.html` and brain artifact `app-preview.html` updated with full onboarding stepper, Pro checkout simulation, and dynamic badge state. |
| **Fuel Expense Tracking** | 2026-11-07 | Done | Added `FuelLog` Room entity, `FuelLogDao`, modal `#modal-fuel-log`, real-time $/gal calculation, automatic MPG calculation on odometer progression, and fuel ledger feed. |
| **4-Point Tire Tread Gauge** | 2026-11-07 | Done | Added `TreadLog` Room entity, `TreadLogDao`, modal `#modal-tread-log`, interactive 4-corner chassis schematic (FL, FR, RL, RR), wear progress bars, and rotation safety alerts. |
| **Vehicle Bay Configuration** | 2026-11-07 | Done | Custom nickname, license plate, VIN, and unit switcher (mi/km, gal/L) with instant single-bay JSON/CSV export. |
| **Automotive Photography Integration** | 2026-11-07 | Done | Generated 16:9 photorealistic editorial imagery for Tacoma TRD (4x4), Classic Bronco 302 (Vintage V8), Civic Sport (Commuter), and Workshop Hero Bay. Tastefully integrated into mobile vehicle cards, switcher pills, and landing page diversity showcase without cluttering data readouts or touch targets. |
| **BUG-014: Base64 Asset Embedding** | 2026-11-07 | Done | Compressed images 10x using high-quality bicubic sampling and compiled them into standalone base64 Data URIs (`embedded_assets.py`). Resolved sandbox webview image loading block. |
| **Marketing & Copy Refinement** | 2026-11-07 | Done | Updated website main heading copy to exactly "Vehicle Maintenance App", eliminated misleading claims of "zero subscriptions", transparently highlighting the generous free tier alongside the honest $19.99 one-time lifetime plan. Synced across landing page, legal hub, app prototype, and listing metadata. |
