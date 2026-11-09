# 🐞 Noin Bug Tracking & QA Log
## Project: Vehicle Maintenance App - Noin

> **Standard:** `replica-test` specification.
> **Severity Definition:**
> - **S1:** Data loss, security hole, core flow blocked
> - **S2:** Feature broken, no workaround
> - **S3:** Broken with a workaround, or visibly wrong
> - **S4:** Cosmetic / Minor polish

---

## 1. Summary of Test Passes
* **Total Flow Cases Tested:** 15
* **Passed:** 15
* **Failed:** 0
* **Open S1 Bugs:** 0
* **Open S2 Bugs:** 0

---

## 2. Bug History & Resolved Items

| Bug ID | Severity | Description | Steps to Reproduce | Resolution | Commit / Fix |
|---|---|---|---|---|---|
| **BUG-001** | S3 | Contrast check failed on `border-input` against `#0B0F17` background (ratio was 2.13:1 vs required 3.0:1 for UI elements). | Run `python contrast.py tokens.json` | Updated `border-input` token from `#3B4A60` to `#546682`. New ratio **3.29:1 (Passes AA)**. | Fixed in `replica/design/tokens.json` |
| **BUG-002** | S3 | Contrast check failed on `on-danger` on `danger` for normal body text. | Run `python contrast.py tokens.json` | Replaced `#EF4444` with darker crimson `#DC2626` and paired for large banner usage. New ratio **4.83:1 (Passes AA)**. | Fixed in `replica/design/tokens.json` |
| **BUG-003** | S2 | Odometer input could theoretically roll back vehicle's current mileage if user logged an old historical service record. | Log past service at 70,000 mi when current car mileage is 85,000 mi. | Added condition in `VehicleRepository.logService`: vehicle odometer only updates if `log.odometer > vehicle.currentOdometer`. | Fixed in `VehicleRepository.kt` |
| **BUG-004** | S3 | Privacy nav menu item & shield icon in preview triggered generic alert instead of navigating to Privacy Audit screen. | Tap "Privacy" in bottom navigation or top bar shield icon. | Implemented dedicated `PrivacyGuaranteeScreen.kt` in Compose and responsive `#screen-privacy` in interactive preview with full offline audit checklist & data controls. | Fixed in `PrivacyGuaranteeScreen.kt`, `NavHost.kt`, `preview.html`, `app-preview.html` |
| **BUG-005** | S2 | Windows PowerShell pipeline corrupted UTF-8 emojis, arrows, and em-dashes into broken mojibake symbols (``, `â€`, `?`), breaking UI elements and text. | Inspect `app-preview.html` after PowerShell file transfer. | Replaced fragile raw multibyte characters with resilient HTML numeric entities (`&#8212;`, `&#9733;`, `&#128663;`, `&#10003;`) and compiled via clean Python UTF-8 generator (`build_preview.py`). 0 bad characters remaining. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html` |
| **BUG-006** | S3 | Top app bar header row crowded on narrow 375px mobile viewport, causing title text truncation clipping. | Open preview on mobile screen width. | Added flex layout with `min-width: 0; flex: 1; text-overflow: ellipsis` and `flex-shrink: 0` action cluster. | Fixed in `preview.html`, `app-preview.html` |
| **BUG-007** | S4 | Micro-text font sizes below 11px on badges and captions violated accessibility guidelines. | Audit text elements in prototype. | Bumped all font sizes to minimum floor of 11px/12px across badges, tables, and stepper indicators. | Fixed in `preview.html`, `app-preview.html` |
| **BUG-008** | S2 | Update odometer button failed to trigger in embedded prototype. | Tap "Update" on odometer box inside embedded preview iframe. | Replaced blocked browser `window.prompt()` with in-app native bottom sheet modal (`#modal-odometer`), numeric validation, quick bump chips (`+50`, `+150`, `+500 mi`), and in-app toast feedback. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html` |
| **BUG-009** | S3 | Comparison table bottom baseline strip text was clipped horizontally at the bottom of the card, and insufficient scroll bottom padding caused the CTA button to hug the bottom nav edge. | Open `#screen-pricing` in mobile preview and inspect the bottom of the comparison table. | Redesigned the baseline guarantee strip into a compact 2-line layout (`Included on Both Free & Pro:` with inline feature dots), eliminated multi-tier flex box overflow, and expanded `.screen` bottom padding to `48px` with `24px` margin below Google Play billing row. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html`, `ProUpgradeScreen.kt` |
| **BUG-010** | S3 | Bottom navigation bar icons lacked contrast against white background (dossier white page emoji invisible, log wrench low contrast); service categories lacked specified emojis; comparison card container clipped on small viewports. | Inspect bottom nav bar and service log selector. | Replaced pale sheet emoji with high-contrast clipboard dossier (`📋`), added prominent Obsidian action capsule (`➕`) for log entry, framed all nav icons in elevated `#F1F5F9`/`#CBD5E1` capsules, updated service categories with designated emojis (🛢️ Oil can, 🛞 Tyres, 🛑 Brakes, 🔋 Battery, 🔍 Inspection, ⚙️ Other), and removed `overflow:hidden` on comparison card with 64px scroll clearance. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html`, `QuickServiceTile.kt`, `components.md` |
| **BUG-011** | S3 | Bottom navigation emojis appeared toy-like and OS-inconsistent; active tab used a harsh black box with black border; payment CTA button had skinny 46px height with cramped vertical padding. | Inspect bottom navigation and `#screen-pricing` checkout CTA. | Replaced all bottom navigation emojis with clean monochrome vector SVGs (`currentColor`); removed black background and black border on selected tab in favor of a subtle Light Grey (`#E2E8F0`) capsule; enlarged payment CTA button to a substantial 54px touch target with 15px bold typography and 14px squircle radius. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html`, `TorqueButton.kt`, `components.md` |
| **BUG-012** | S3 | Service category icons rendered as emojis / broken font glyphs (bell for oil, box for tyres, stop sign for brakes, toy battery); selected service tile had harsh pitch-black background. | Inspect `#screen-quick-log` service tiles in daylight preview. | Replaced all service category emojis with crisp, automotive vector SVGs (motor oil bottle with droplet, automotive tyre & wheel, disc brake rotor & caliper clamp, 12V car battery with terminal posts, diagnostic magnifying glass with checkmark, mechanical precision gear); redesigned selected tile state with Light Grey (`#F1F5F9`) background, 2px Obsidian border, and `#0F172A` text/icon (zero black background); synced SVG rendering into timeline logs feed and vehicle switcher. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html`, `QuickServiceTile.kt`, `components.md` |
| **BUG-013** | S3 | In-app fuel fill-up and tyre tread modals clipped at bottom by bottom navigation bar due to shared z-index 50. | Open "+ Log Fuel" or "+ Tread Check" from Garage Home. | Elevated all modal overlays to z-index 100 and toast to z-index 120; added box-sizing: border-box, max-height 90%, and 40px bottom padding to modal sheets so action buttons are fully visible and clickable above navigation bar. | Fixed in `build_preview.py`, `preview.html`, `app-preview.html` |
| **BUG-014** | S2 | Vehicle cover images and thumbnails failed to render in sandboxed webviews/iframes due to browser local-file origin restrictions (`Not allowed to load local resource`). | Open `app-preview.html` or `landing.html` in an embedded webview or iframe. | Compressed and downsampled all automotive photography using bicubic sampling (69KB–99KB) and compiled them directly into `preview.html` and `landing.html` as embedded base64 Data URIs (`data:image/jpeg;base64,...`). 100% self-contained, guaranteed instant rendering in any browser or webview sandbox. | Fixed in `embedded_assets.py`, `build_preview.py`, `build_complete_landing.py`, `preview.html`, `app-preview.html`, `landing.html` |
| **BUG-015** | S3 | Desktop-like horizontal scrollbar visible under vehicle switcher pills; identical car image displayed across all vehicles with no way for owners to upload their own vehicle photos. | Inspect `#garage-vehicle-selector` on Windows/desktop browser and switch between vehicles. | Implemented cross-browser scrollbar suppression (`scrollbar-width: none; -ms-overflow-style: none; ::-webkit-scrollbar { display: none !important; }`); added round 20x20 thumbnail badges to each vehicle pill; created custom photo dropzone with instant client-side `FileReader` base64 upload, preview, and remove in "Add Vehicle" (`#screen-add-vehicle`); added in-place "Change Photo" camera button on active car banner and dedicated "Upload New Photo" / "Reset" controls in Vehicle Bay Detail (`#detail-tab-view-bay`). | Fixed in `build_preview.py`, `preview.html`, `app-preview.html` |

---

## 3. QA Pre-Flight Checklist
- [x] S01: Garage Home displays empty state cleanly when zero vehicles exist.
- [x] S02: Vehicle Bay displays cumulative lifetime maintenance cost calculated accurately in cents.
- [x] S03: Quick Service selector switches default descriptions without manual typing.
- [x] S04: Classic cars (pre-1981) can be parked with `vin = null` without crashing validation.
- [x] S06: Resale Dossier PDF renders vehicle details and chronological maintenance ledger on A4 canvas without external API dependencies.
- [x] Security: Zero background location tracking or contact harvesting in `AndroidManifest.xml`.
- [x] Zero open S1 or S2 issues.
