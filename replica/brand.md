# 🏷️ Brand Architecture: Noin
## Project Title: Vehicle Maintenance App - Noin

> Offline-First Vehicle Maintenance & Resale Dossier for Android and Web.
> Built following the `replica-brand` protocol.

---

## 1. Selected Brand Identity & Positioning

* **Official Project Name:** Vehicle Maintenance App - Noin
* **Consumer Brand Name:** Noin
* **Core Brand Angle:** *"For vehicle owners and enthusiasts who hate subscription paywalls and losing years of records to cloud servers or abandoned apps, Noin provides a 100% offline, privacy-first maintenance logbook with local SQLite storage, custom car photography, and a buyer-ready PDF service dossier when it's time to sell."*

### Brand Logo Mark:
* **The Noin Gear & Vehicle Emblem:** An iconic 12-tooth mechanical precision gear cog encircling a front-facing automotive silhouette.
* **Symbolism:** Mechanical reliability, owner sovereignty, precision engineering, and vehicle care.
* **Colors:** Deep Obsidian (`#0F172A`), Pure White (`#FFFFFF`), Emerald Health (`#059669`), and Slate Neutral (`#64748B`).
* **Asset Location:** `assets/noin_logo.png` (1024x1024 Master) and `assets/noin_logo_256.png` (Optimized 256x256 Web & App Icon).

---

## 2. Palette & Design Tokens

Existing vehicle apps (Drivvo, Simply Auto, Fuelly) drown in generic corporate electric blues (`#0066cc`, `#2563eb`).
**Noin** adopts a clean **Daylight Minimalist & Obsidian Engine** aesthetic:
* Architectural Canvas: `#F8FAFC`
* Elevated Surface: `#FFFFFF`
* Typography & Contrast Accent: `#0F172A` (Obsidian)
* Mechanical Muted: `#475569` / `#64748B` (Slate)
* Positive Status & Verified Logs: `#059669` (Emerald)

### Contrast Check Results (`contrast.py`):
```text
  AAA   17.06:1  text                     on bg                   
  AAA   17.85:1  text                     on surface              
  AAA   17.85:1  text                     on surface-card         
  AAA   16.30:1  text                     on surface-elevated     
  AAA    7.24:1  text-muted               on bg                   
  AAA    7.58:1  text-muted               on surface              
  AAA    7.58:1  text-muted               on surface-card         
  AAA   17.85:1  on-accent                on accent               
  AAA   17.06:1  accent                   on bg                   large
  AAA    4.83:1  on-danger                on danger               large
  AA     3.77:1  on-success               on success              large
  PASS   4.55:1  border-input             on bg                   ui

  12 pairs, 0 failing AA (All Passed)
```

---

## 3. Brand Voice & Tone

* **Honest & Direct:** Never disguise upsells or use deceptive dark patterns.
* **Mechanical & Precise:** Speaks like a seasoned master mechanic who values documentation, torque specs, and clean maintenance ledgers.
* **Sovereign & Local-First:** Your garage data stays on your physical phone. No tracking, no data brokers, no cloud ransom.
