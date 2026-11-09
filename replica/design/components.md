# 📐 Component Specifications: Noin Design System (Daylight Edition)
## Project: Vehicle Maintenance App - Noin

> **Design Tenet:** Clean daylight legibility, minimal visual noise, generous breathing room, and mechanical clarity.
> Adheres strictly to the Core Principles of Design: high signal-to-noise ratio, clear visual hierarchy, thumb-friendly touch targets (min 48dp), and WCAG AAA compliance.
> Built natively for Jetpack Compose Material 3 & Web Preview.

---

## 1. Core Principles of Design (Clutter-Free Architecture)

1. **Signal over Noise:** Removed decorative demo boxes, loud banners, and duplicate callouts. The user's vehicle status, current mileage, and service records take center stage.
2. **Daylight Clean Aesthetics:** Pure white surface cards (`#FFFFFF`) sitting on a clean architectural off-white canvas (`#F8FAFC`), paired with deep obsidian typography (`#0F172A`) for maximum readability in direct sunlight.
3. **Restrained Accent Palette:** Obsidian black (`#0F172A`) for primary actions, emerald (`#059669`) for positive maintenance health checks, and neutral slate (`#64748B`) for secondary metadata.
4. **Focused Header Bar:** Features the iconic Noin gear-and-car emblem badge, vehicle title, clean status pill, and single `+` entry action.

---

## 2. Core Component Specifications

### C00: Noin Brand Emblem (Logo Mark)
* **Role:** Official application icon, brand signature, and navbar mark.
* **Visual Elements:**
  * Outer: 12-tooth mechanical gear cog symbolising engineering precision, maintenance craftsmanship, and durability.
  * Inner: Enclosed circle framing a crisp automotive silhouette (front-facing vehicle with headlights, windscreen, and tyres).
  * Colorway: High-contrast white silhouette on deep obsidian (`#0F172A`) badge squircle, or monochrome on light backgrounds.
* **Sizes & Applications:**
  * Small (Navbar / Header): 28x28dp or 32x32dp squircle with 8dp radius.
  * Medium (Cards / Modals): 48x48dp squircle with 12dp radius.
  * Large (Splash / Onboarding / App Icon): 80x80dp squircle with 20dp radius.
* **Used on:** Top App Bar, Onboarding Screen, Resale Dossier Header & Watermark, Privacy Audit Screen, Landing Page, Legal Pages, App Icon.

---

### C01: Odometer Display Widget
* **Role:** Primary vehicle odometer reading and unit indicator.
* **Specs:**
  * Background: Clean elevated surface (`#F8FAFC`) with subtle hairline border (`#E2E8F0`).
  * Typography: JetBrains Mono, size 28sp, weight 800 (Bold), color `text` (`#0F172A`).
  * Unit Label: Bold 12sp uppercase, color `text-muted` (`#64748B`).
  * Quick Edit Button: 48x48dp touch target, opens instant prompt to update mileage.
* **States:** Default, Hover, Pressed.
* **Used on:** S01 (Garage Home), S02 (Vehicle Bay).

---

### C02: Quick Service Tile (Grid Selector)
* **Role:** 1-tap maintenance category buttons for frictionless logging.
* **Vector Icons (Monochrome SVGs, currentColor, 22x22dp):**
  * `Oil & Filter`: Motor oil bottle with drop vector SVG
  * `Tyres`: Automotive wheel & tyre with spokes vector SVG
  * `Brakes`: Disc brake rotor & caliper clamp vector SVG
  * `Battery`: 12V automotive battery with top terminal posts (+ / -) vector SVG
  * `Inspection`: Diagnostic magnifying glass with checklist checkmark vector SVG
  * `Other`: Mechanical precision gear vector SVG
* **Specs & State Design:**
  * Inactive / Default: Pure white `#FFFFFF` surface, 1.5px Slate border (`#CBD5E1`), Slate `#64748B` icon and label.
  * Selected State: **Light Grey** (`#F1F5F9`) background, 2px Obsidian (`#0F172A`) border, bold Obsidian `#0F172A` label & vector stroke (17.85:1 AAA contrast). Never pitch-black.
  * Hover / Focus: Off-white elevation (`#F8FAFC`) with subtle slate border.
  * Container Radius: 12dp squircle with centered icon & typography.
* **Used on:** S03 (Quick Log Entry), S01 & S02 (Timeline Service Record Icons).

---

### C03: Service Record Item (Timeline Card)
* **Components:**
  * Left Icon: Service category icon inside a clean rounded container (`#F1F5F9`).
  * Center Column: Service title (bold 13sp `#0F172A`), date & provider (11sp `#64748B`), and part numbers.
  * Right Column: Cost in bold tabular numbers (14sp `#0F172A`), odometer milestone (11sp `#64748B`).
* **Specs:**
  * Background: `#FFFFFF` with 1px hairline border (`#E2E8F0`) and 12dp radius.
* **Used on:** S01 (Garage Home), S02 (Vehicle Bay).

---

### C04: Primary Action Button (NoinButton)
* **Specs:**
  * Background: Solid Obsidian (`#0F172A`).
  * Text: 15sp bold (`#FFFFFF`), letter-spacing 0.3px.
  * Touch target: Height 54dp (substantial, thumb-friendly), full width or auto, 14dp squircle radius.
  * Elevation: Soft focus shadow `0 4px 14px rgba(15, 23, 42, 0.18)`.
  * Active/Tap: `transform: scale(0.98)` tactile response.

---

### C05: Minimalist Vector Bottom Navigation Bar
* **Specs:**
  * Background: Pure white `#FFFFFF` with top border `#E2E8F0`.
  * Height: 64dp with generous thumb spacing.
  * Vector Icons: Monochrome SVG vectors (Garage car, Dossier ledger, Log plus, Privacy shield) instead of OS emojis.
  * Inactive State: Transparent capsule, Slate `#64748B` stroke and typography.
  * Selected/Active State: Light Grey (`#E2E8F0`) capsule with deep Obsidian `#0F172A` stroke and bold `#0F172A` typography. Zero black background or outline.
  * High-Contrast Roles:
    * **Garage:** 🚗 High-contrast automobile
    * **Dossier:** 📋 Clipboard ledger (replaces pale white sheet for maximum contrast on light background)
    * **Log Service:** ➕ Solid Obsidian center action badge with bold white plus (17.85:1 AAA contrast)
    * **Privacy:** 🛡️ Contrast shield
  * Label Typography: 11sp bold, dark slate `#475569` (7.24:1 AAA contrast) when inactive, `#0F172A` when active.

---

### C06: High-Clarity Plan Comparison Matrix
* **Role:** Unambiguous, instant side-by-side comparison of Free Tier vs Pro Tier.
* **Specs:**
  * Container: `#FFFFFF` card, 1px `#E2E8F0` border, 14dp radius, subtle drop shadow.
  * Header Bar: `#F8FAFC` background with 1px bottom border `#E2E8F0`.
  * Pro Tier Badge: Solid Obsidian `#0F172A` with `#FFFFFF` text (10sp / Black).
  * Feature Differentiators:
    * Garage Bays: `1 Vehicle` vs `Unlimited` (Emerald `#047857` on `#ECFDF5` pill, WCAG 5.2:1 AA).
    * Resale Dossier: `1-Page Basic` vs `Multi-Page A4` (Elevated `#F1F5F9` pill).
    * Receipt Photos: `Manual log` vs `Unlimited` (Emerald pill).
  * Baseline Guarantees Strip:
    * Compact footer bar (`#F8FAFC`) with top hairline divider (`#E2E8F0`).
    * Bold emerald checkmark `✓` (`#059669`) with clear title: `Included on Both Free & Pro:`.
    * Concise, high-signal single-line subtitle: `100% Offline SQLite • Zero Ads & Trackers • Full CSV/JSON Export`.
    * Guaranteed zero vertical clipping or overflow issues across all device viewports.
* **Used on:** S04 (Pro Upgrade Screen / In-App Purchase Flow).
