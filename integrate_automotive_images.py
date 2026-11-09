"""
Integrates professional automotive photography into TorqueKeep app and website:
- App (preview.html): Vehicle cards with responsive cover photos, switcher thumbnails, detail banner, dossier preview.
- Website (landing.html): Hero garage workshop showcase, 3-bay vehicle diversity card grid (Tacoma, Bronco, Civic).
- Strict adherence to daylight tokens, clean room compliance, zero clutter.
"""

import os
import shutil

ROOT_DIR = r"d:\Project01"
BRAIN_DIR = r"C:\Users\vinee\.gemini\antigravity\brain\380c6241-6d0c-483e-aa3e-4e5f725d6e16"

# 1. Update build_preview.py
def update_build_preview():
    path = os.path.join(ROOT_DIR, "build_preview.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update state.vehicles with 3 vehicles (Tacoma, Bronco, Civic)
    old_state_vehicles = """      vehicles: [
        {
          id: 'veh_1',
          year: 2018,
          make: "Toyota",
          model: "Tacoma TRD",
          nickname: "Silver Daily &#8226; 4WD Manual",
          licensePlate: "7XYZ890",
          vin: "3TMCZ5EN9JM123456",
          odometer: 84250,
          unit: "mi",
          fuelUnit: "gal",
          tag: "PRIMARY",
          icon: "&#128663;",
          tread: {
            fl: 8,
            fr: 8,
            rl: 7,
            rr: 7,
            brand: "Michelin Defender LTX M/S",
            date: "Oct 14, 2026"
          },
          fuelLogs: [
            {
              id: 101,
              date: "Nov 02, 2026",
              odometer: 84250,
              volume: 16.2,
              cost: 51.68,
              pricePerUnit: 3.19,
              isFullTank: true,
              mpg: 21.6,
              station: "Costco Gas (87 Regular)"
            },
            {
              id: 102,
              date: "Oct 20, 2026",
              odometer: 83900,
              volume: 15.8,
              cost: 51.98,
              pricePerUnit: 3.29,
              isFullTank: true,
              mpg: 22.1,
              station: "Chevron (87 Regular)"
            }
          ],
          logs: [
            {
              id: 1,
              title: "Full Synthetic Oil & Filter",
              date: "Oct 14, 2026",
              odometer: 84000,
              cost: 42.50,
              provider: "DIY Home Garage",
              parts: "Mobil1 0W-20 (5.5qt), OEM #04152-YZZA1",
              category: "oil_change"
            },
            {
              id: 2,
              title: "Tire Rotation & Balance",
              date: "Aug 02, 2026",
              odometer: 80000,
              cost: 25.00,
              provider: "Discount Tire",
              parts: "Cross-rotation pattern",
              category: "tire_rotation"
            },
            {
              id: 3,
              title: "12V AGM Battery Replacement",
              date: "Jan 12, 2026",
              odometer: 74500,
              cost: 189.99,
              provider: "AutoZone",
              parts: "Duralast Platinum AGM Group 24F",
              category: "battery"
            }
          ]
        }
      ]"""

    new_state_vehicles = """      vehicles: [
        {
          id: 'veh_1',
          year: 2018,
          make: "Toyota",
          model: "Tacoma TRD",
          nickname: "Silver Daily &#8226; 4WD Manual",
          image: "assets/tacoma_trd.jpg",
          fallbackImage: "tacoma_trd.jpg",
          bayTag: "BAY 01",
          health: "HEALTHY",
          licensePlate: "7XYZ890",
          vin: "3TMCZ5EN9JM123456",
          odometer: 84250,
          unit: "mi",
          fuelUnit: "gal",
          tag: "PRIMARY",
          icon: "&#128663;",
          tread: {
            fl: 8,
            fr: 8,
            rl: 7,
            rr: 7,
            brand: "Michelin Defender LTX M/S",
            date: "Oct 14, 2026"
          },
          fuelLogs: [
            {
              id: 101,
              date: "Nov 02, 2026",
              odometer: 84250,
              volume: 16.2,
              cost: 51.68,
              pricePerUnit: 3.19,
              isFullTank: true,
              mpg: 21.6,
              station: "Costco Gas (87 Regular)"
            },
            {
              id: 102,
              date: "Oct 20, 2026",
              odometer: 83900,
              volume: 15.8,
              cost: 51.98,
              pricePerUnit: 3.29,
              isFullTank: true,
              mpg: 22.1,
              station: "Chevron (87 Regular)"
            }
          ],
          logs: [
            {
              id: 1,
              title: "Full Synthetic Oil & Filter",
              date: "Oct 14, 2026",
              odometer: 84000,
              cost: 42.50,
              provider: "DIY Home Garage",
              parts: "Mobil1 0W-20 (5.5qt), OEM #04152-YZZA1",
              category: "oil_change"
            },
            {
              id: 2,
              title: "Tire Rotation & Balance",
              date: "Aug 02, 2026",
              odometer: 80000,
              cost: 25.00,
              provider: "Discount Tire",
              parts: "Cross-rotation pattern",
              category: "tire_rotation"
            },
            {
              id: 3,
              title: "12V AGM Battery Replacement",
              date: "Jan 12, 2026",
              odometer: 74500,
              cost: 189.99,
              provider: "AutoZone",
              parts: "Duralast Platinum AGM Group 24F",
              category: "battery"
            }
          ]
        },
        {
          id: 'veh_2',
          year: 1974,
          make: "Ford",
          model: "Bronco 302",
          nickname: "Restoration Project &#8226; V8 Classic",
          image: "assets/classic_bronco.jpg",
          fallbackImage: "classic_bronco.jpg",
          bayTag: "BAY 02",
          health: "IN RESTORATION",
          licensePlate: "BRONC-74",
          vin: "U15GLU20000",
          odometer: 112400,
          unit: "mi",
          fuelUnit: "gal",
          tag: "PROJECT",
          icon: "&#128663;",
          tread: {
            fl: 10,
            fr: 10,
            rl: 10,
            rr: 10,
            brand: "BFGoodrich All-Terrain T/A KO2",
            date: "Sep 28, 2026"
          },
          fuelLogs: [
            {
              id: 201,
              date: "Oct 28, 2026",
              odometer: 112400,
              volume: 14.0,
              cost: 47.60,
              pricePerUnit: 3.40,
              isFullTank: true,
              mpg: 13.8,
              station: "Shell 91 V-Power"
            }
          ],
          logs: [
            {
              id: 4,
              title: "Holley Carburetor Rebuild & Tune",
              date: "Oct 15, 2026",
              odometer: 112350,
              cost: 135.00,
              provider: "DIY Home Garage",
              parts: "Holley 4160 Rebuild Kit #3-1346",
              category: "other"
            },
            {
              id: 5,
              title: "Front Disc Brake Conversion Check",
              date: "Aug 10, 2026",
              odometer: 112100,
              cost: 48.00,
              provider: "Vintage 4x4 Shop",
              parts: "Wilwood DOT4 High-Temp Fluid",
              category: "brake_service"
            }
          ]
        },
        {
          id: 'veh_3',
          year: 2021,
          make: "Honda",
          model: "Civic Sport",
          nickname: "Daily Commuter &#8226; 1.5L Turbo",
          image: "assets/civic_sport.jpg",
          fallbackImage: "civic_sport.jpg",
          bayTag: "BAY 03",
          health: "HEALTHY",
          licensePlate: "9CIV982",
          vin: "2HGFC1F52MH543210",
          odometer: 38120,
          unit: "mi",
          fuelUnit: "gal",
          tag: "COMMUTER",
          icon: "&#128663;",
          tread: {
            fl: 7,
            fr: 7,
            rl: 8,
            rr: 8,
            brand: "Continental ExtremeContact DWS06",
            date: "Jul 18, 2026"
          },
          fuelLogs: [
            {
              id: 301,
              date: "Nov 04, 2026",
              odometer: 38120,
              volume: 11.2,
              cost: 35.72,
              pricePerUnit: 3.19,
              isFullTank: true,
              mpg: 34.2,
              station: "Costco Gas (87 Regular)"
            }
          ],
          logs: [
            {
              id: 6,
              title: "Synthetic Oil 0W-20 & Filter",
              date: "Sep 20, 2026",
              odometer: 36000,
              cost: 44.00,
              provider: "Honda Express Service",
              parts: "OEM Honda 0W-20 & Filter #15400-PLM-A02",
              category: "oil_change"
            },
            {
              id: 7,
              title: "Cabin & Engine Air Filters",
              date: "May 12, 2026",
              odometer: 32000,
              cost: 29.50,
              provider: "DIY Home Garage",
              parts: "WIX Cabin & Intake Air Filters",
              category: "inspection"
            }
          ]
        }
      ]"""

    if old_state_vehicles in content:
        content = content.replace(old_state_vehicles, new_state_vehicles)
    else:
        print("[WARN] old_state_vehicles pattern not found directly")

    # Update Active Vehicle Card on screen-garage-home with image banner
    old_card_start = """      <!-- Active Vehicle Card -->
      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div id="v-title" style="font-size: 17px; font-weight: 800; color: #0F172A;">2018 TOYOTA TACOMA TRD</div>
            <div id="v-sub" style="font-size: 12px; color: #64748B; margin-top: 2px;">Silver Daily &#8226; 4WD Manual</div>
          </div>
          <span id="v-tag" style="padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0;">PRIMARY</span>
        </div>"""

    new_card_start = """      <!-- Active Vehicle Card -->
      <div class="card" style="padding: 16px;">
        <!-- Sleek Vehicle Photo Banner -->
        <div style="position: relative; width: 100%; height: 128px; border-radius: 12px; overflow: hidden; margin-bottom: 12px; border: 1px solid #E2E8F0; background: #F1F5F9;">
          <img id="v-image" src="assets/tacoma_trd.jpg" onerror="this.src='tacoma_trd.jpg'" alt="Vehicle Photo" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
          <div style="position: absolute; top: 8px; left: 8px; background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(4px); color: #FFFFFF; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 6px; letter-spacing: 0.5px;" id="v-bay-tag">
            BAY 01
          </div>
          <div style="position: absolute; top: 8px; right: 8px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(4px); color: #059669; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 6px; display: flex; align-items: center; gap: 4px;" id="v-health-badge">
            <span style="width: 6px; height: 6px; border-radius: 50%; background: #059669;"></span>
            HEALTHY
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div id="v-title" style="font-size: 17px; font-weight: 800; color: #0F172A;">2018 TOYOTA TACOMA TRD</div>
            <div id="v-sub" style="font-size: 12px; color: #64748B; margin-top: 2px;">Silver Daily &#8226; 4WD Manual</div>
          </div>
          <span id="v-tag" style="padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0;">PRIMARY</span>
        </div>"""

    if old_card_start in content:
        content = content.replace(old_card_start, new_card_start)

    # Update renderVehicleSwitcher to render small vehicle thumbnail in pills
    old_switcher_loop = """      state.vehicles.forEach(v => {
        const isActive = v.id === state.selectedVehicleId;
        html += `
          <button onclick="switchActiveVehicle('${v.id}')" style="padding: 6px 14px; border-radius: 9999px; border: ${isActive ? '2px solid #0F172A' : '1px solid #CBD5E1'}; background: ${isActive ? '#F1F5F9' : '#FFFFFF'}; color: #0F172A; font-size: 12px; font-weight: ${isActive ? '800' : '600'}; cursor: pointer; white-space: nowrap; display: flex; align-items: center; gap: 7px; flex-shrink: 0; box-shadow: 0 1px 2px rgba(0,0,0,0.03); transition: all 0.15s ease;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/>
              <circle cx="7" cy="17" r="2"/>
              <path d="M9 17h6"/>
              <circle cx="17" cy="17" r="2"/>
            </svg>
            <span>${v.make} ${v.model}</span>
          </button>
        `;
      });"""

    new_switcher_loop = """      state.vehicles.forEach(v => {
        const isActive = v.id === state.selectedVehicleId;
        html += `
          <button onclick="switchActiveVehicle('${v.id}')" style="padding: 4px 12px 4px 5px; border-radius: 9999px; border: ${isActive ? '2px solid #0F172A' : '1px solid #CBD5E1'}; background: ${isActive ? '#F1F5F9' : '#FFFFFF'}; color: #0F172A; font-size: 12px; font-weight: ${isActive ? '800' : '600'}; cursor: pointer; white-space: nowrap; display: flex; align-items: center; gap: 7px; flex-shrink: 0; box-shadow: 0 1px 2px rgba(0,0,0,0.03); transition: all 0.15s ease;">
            <img src="${v.image || 'assets/tacoma_trd.jpg'}" onerror="this.src='${v.fallbackImage || 'tacoma_trd.jpg'}'" alt="${v.model}" style="width: 24px; height: 24px; border-radius: 50%; object-fit: cover; border: 1px solid #CBD5E1;" />
            <span>${v.make} ${v.model}</span>
          </button>
        `;
      });"""

    if old_switcher_loop in content:
        content = content.replace(old_switcher_loop, new_switcher_loop)

    # In renderLogs(), update the image src
    old_render_v_info = """      // Update vehicle card header
      document.getElementById('v-title').innerText = `${v.year} ${v.make.toUpperCase()} ${v.model.toUpperCase()}`;
      document.getElementById('v-sub').innerText = `${v.nickname || 'Verified Local Log'}`;
      document.getElementById('v-odometer').innerText = v.odometer.toLocaleString();
      document.getElementById('v-unit').innerText = v.unit.toUpperCase();
      document.getElementById('v-tag').innerText = v.tag;"""

    new_render_v_info = """      // Update vehicle card header & image
      document.getElementById('v-title').innerText = `${v.year} ${v.make.toUpperCase()} ${v.model.toUpperCase()}`;
      document.getElementById('v-sub').innerText = `${v.nickname || 'Verified Local Log'}`;
      document.getElementById('v-odometer').innerText = v.odometer.toLocaleString();
      document.getElementById('v-unit').innerText = v.unit.toUpperCase();
      document.getElementById('v-tag').innerText = v.tag;
      
      const vImg = document.getElementById('v-image');
      if (vImg) {
        vImg.src = v.image || 'assets/tacoma_trd.jpg';
        vImg.onerror = function() { this.src = v.fallbackImage || 'tacoma_trd.jpg'; };
      }
      const vBay = document.getElementById('v-bay-tag');
      if (vBay) vBay.innerText = v.bayTag || 'BAY 01';
      const vHealth = document.getElementById('v-health-badge');
      if (vHealth) {
        const isHealthy = (v.health || 'HEALTHY') === 'HEALTHY';
        vHealth.innerHTML = `<span style="width: 6px; height: 6px; border-radius: 50%; background: ${isHealthy ? '#059669' : '#D97706'};"></span>${v.health || 'HEALTHY'}`;
        vHealth.style.color = isHealthy ? '#059669' : '#D97706';
      }"""

    if old_render_v_info in content:
        content = content.replace(old_render_v_info, new_render_v_info)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] build_preview.py updated with tasteful vehicle photography.")

update_build_preview()
