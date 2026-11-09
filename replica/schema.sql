-- Noin Database Schema (Room SQLite / SQLite 3.35+)
-- Project: Vehicle Maintenance App - Noin
-- Offline-First, Zero Cloud Hosting Cost, 100% On-Device

-- 1. VEHICLES TABLE
CREATE TABLE IF NOT EXISTS vehicles (
    id TEXT PRIMARY KEY NOT NULL,             -- UUID v4
    name TEXT NOT NULL,                       -- e.g. "Silver Daily", "Project 240Z"
    make TEXT NOT NULL,                       -- e.g. "Toyota", "Ford"
    model TEXT NOT NULL,                      -- e.g. "Tacoma", "Mustang"
    year INTEGER NOT NULL,                    -- e.g. 2018
    vin TEXT,                                 -- Optional! (Pre-1981 / Classics / Motorcycles)
    license_plate TEXT,                       -- Optional
    current_odometer INTEGER NOT NULL DEFAULT 0, -- In miles or km
    odometer_unit TEXT NOT NULL DEFAULT 'mi' CHECK (odometer_unit IN ('mi', 'km')),
    fuel_unit TEXT NOT NULL DEFAULT 'gal' CHECK (fuel_unit IN ('gal', 'L')),
    currency_code TEXT NOT NULL DEFAULT 'USD',-- ISO 4217 code
    is_archived INTEGER NOT NULL DEFAULT 0,   -- 0 = active, 1 = sold/archived
    created_at INTEGER NOT NULL,              -- Epoch timestamp (ms)
    updated_at INTEGER NOT NULL               -- Epoch timestamp (ms)
);

CREATE INDEX IF NOT EXISTS idx_vehicles_archived ON vehicles (is_archived, updated_at DESC);

-- 2. SERVICE LOGS TABLE
CREATE TABLE IF NOT EXISTS service_logs (
    id TEXT PRIMARY KEY NOT NULL,             -- UUID v4
    vehicle_id TEXT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
    service_type TEXT NOT NULL,               -- e.g. 'oil_change', 'tire_rotation', 'brakes', 'battery', 'custom'
    title TEXT NOT NULL,                      -- Display title e.g. "Full Synthetic 5W-30 & Filter"
    odometer INTEGER NOT NULL,                -- Odometer reading at service
    cost_cents INTEGER NOT NULL DEFAULT 0,    -- Cost in lowest currency denominator (e.g. $45.50 -> 4550)
    service_date INTEGER NOT NULL,            -- Epoch timestamp (ms) of service
    service_provider TEXT,                    -- "DIY" or shop name e.g. "Firestone", "Home Garage"
    part_numbers TEXT,                        -- e.g. "Fram PH7317, Mobil1 5W-30 (5qt)"
    notes TEXT,                               -- Detailed mechanic notes
    receipt_image_path TEXT,                  -- Local file path to scanned receipt image
    created_at INTEGER NOT NULL,              -- Epoch timestamp (ms)
    updated_at INTEGER NOT NULL               -- Epoch timestamp (ms)
);

CREATE INDEX IF NOT EXISTS idx_service_logs_vehicle ON service_logs (vehicle_id, service_date DESC);
CREATE INDEX IF NOT EXISTS idx_service_logs_type ON service_logs (service_type);

-- 3. MAINTENANCE REMINDERS TABLE
CREATE TABLE IF NOT EXISTS reminders (
    id TEXT PRIMARY KEY NOT NULL,             -- UUID v4
    vehicle_id TEXT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
    service_type TEXT NOT NULL,               -- 'oil_change', 'tire_rotation', etc.
    title TEXT NOT NULL,                      -- e.g. "Next Oil & Filter Change"
    due_odometer INTEGER,                     -- Odometer milestone (e.g. 85000)
    due_date INTEGER,                         -- Epoch timestamp (ms) milestone
    interval_miles INTEGER,                   -- Repeating interval e.g. 5000
    interval_months INTEGER,                  -- Repeating interval e.g. 6
    is_dismissed INTEGER NOT NULL DEFAULT 0,  -- 0 = active, 1 = dismissed
    last_notified_at INTEGER,                 -- Timestamp of last system alert sent
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_reminders_vehicle ON reminders (vehicle_id, is_dismissed);
CREATE INDEX IF NOT EXISTS idx_reminders_due_date ON reminders (due_date);

-- 4. FUEL LOGS TABLE
CREATE TABLE IF NOT EXISTS fuel_logs (
    id TEXT PRIMARY KEY NOT NULL,             -- UUID v4
    vehicle_id TEXT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
    fuel_date INTEGER NOT NULL,               -- Epoch timestamp (ms)
    odometer INTEGER NOT NULL,                -- Odometer reading at fill-up
    volume_liters_or_gallons REAL NOT NULL,   -- e.g. 12.45
    total_cost_cents INTEGER NOT NULL,        -- e.g. 4250 ($42.50)
    is_full_tank INTEGER NOT NULL DEFAULT 1,  -- 1 = full, 0 = partial fill
    calculated_mpg REAL,                      -- Calculated efficiency (stored for quick graph rendering)
    notes TEXT,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_fuel_logs_vehicle ON fuel_logs (vehicle_id, fuel_date DESC);

-- 5. TIRE TREAD DEPTH LOGS TABLE
CREATE TABLE IF NOT EXISTS tread_logs (
    id TEXT PRIMARY KEY NOT NULL,             -- UUID v4
    vehicle_id TEXT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
    measured_date INTEGER NOT NULL,           -- Epoch timestamp (ms)
    odometer INTEGER NOT NULL,                -- Odometer reading at measurement
    fl_32nds INTEGER NOT NULL,                -- Front Left tread depth in 32nds of an inch (e.g. 8)
    fr_32nds INTEGER NOT NULL,                -- Front Right tread depth in 32nds of an inch (e.g. 8)
    rl_32nds INTEGER NOT NULL,                -- Rear Left tread depth in 32nds of an inch (e.g. 7)
    rr_32nds INTEGER NOT NULL,                -- Rear Right tread depth in 32nds of an inch (e.g. 7)
    condition_rating TEXT NOT NULL,           -- 'good' (>=7), 'warning' (4-6), 'critical' (<=3)
    notes TEXT,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_tread_logs_vehicle ON tread_logs (vehicle_id, measured_date DESC);
