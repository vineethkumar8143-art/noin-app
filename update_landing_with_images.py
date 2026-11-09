"""
Updates build_complete_landing.py to integrate real automotive imagery into landing.html.
"""

import os

path = r"d:\Project01\build_complete_landing.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Mockup Left Column to include Tacoma Photo
old_mockup_left = """            <div class="mockup-left">
              <div class="mockup-vehicle-header">
                <div>
                  <div class="mockup-car-title">2018 Toyota Tacoma TRD</div>
                  <div class="mockup-car-sub">Bay 01 &bull; 84,250 Miles</div>
                </div>
                <span style="font-size: 11px; font-weight: 800; background: #ECFDF5; color: #059669; padding: 4px 8px; border-radius: 6px;">HEALTHY</span>
              </div>"""

new_mockup_left = """            <div class="mockup-left">
              <!-- Real Vehicle Photo Banner -->
              <div style="position: relative; width: 100%; height: 135px; border-radius: 12px; overflow: hidden; margin-bottom: 14px; border: 1px solid #E2E8F0; background: #F1F5F9;">
                <img src="assets/tacoma_trd.jpg" onerror="this.src='tacoma_trd.jpg'" alt="2018 Toyota Tacoma TRD" style="width: 100%; height: 100%; object-fit: cover;" />
                <div style="position: absolute; bottom: 8px; left: 8px; background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(4px); color: white; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 6px; letter-spacing: 0.5px;">BAY 01 &bull; 4WD TRD</div>
                <div style="position: absolute; bottom: 8px; right: 8px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(4px); color: #059669; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 6px;">&bull; HEALTHY</div>
              </div>

              <div class="mockup-vehicle-header">
                <div>
                  <div class="mockup-car-title">2018 Toyota Tacoma TRD</div>
                  <div class="mockup-car-sub">Silver Daily &bull; 4WD Manual &bull; 84,250 Miles</div>
                </div>
              </div>"""

if old_mockup_left in content:
    content = content.replace(old_mockup_left, new_mockup_left)
else:
    print("[WARN] old_mockup_left not found")

# 2. Add Editorial Workshop Banner below mockup
old_mockup_end = """          </div>
        </div>
      </div>
    </section>

    <!-- The Problem Section -->"""

new_mockup_end = """          </div>
        </div>

        <!-- Editorial Workshop Banner -->
        <div style="margin-top: 48px; border-radius: 20px; overflow: hidden; position: relative; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.04);">
          <img src="assets/hero_garage.jpg" onerror="this.src='hero_garage.jpg'" alt="Clean Modern Garage Workshop" style="width: 100%; height: 260px; object-fit: cover; display: block;" />
          <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(15, 23, 42, 0.88) 0%, rgba(15, 23, 42, 0.15) 60%); display: flex; align-items: flex-end; padding: 24px 32px;">
            <div style="color: white; text-align: left;">
              <span style="font-size: 10px; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; background: rgba(255, 255, 255, 0.2); padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.3);">THE TORQUEKEEP STANDARD</span>
              <h3 style="font-size: 20px; font-weight: 800; margin-top: 6px; color: white;">Precision Care for Real Garages. Zero Cloud Hostage.</h3>
              <p style="font-size: 13px; color: #CBD5E1; margin-top: 4px; max-width: 640px;">Whether it's your daily driver, a weekend 4x4 trail rig, or a ground-up classic rebuild, TorqueKeep gives you permanent custody over every receipt, part number, and odometer mile.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- The Problem Section -->"""

if old_mockup_end in content:
    content = content.replace(old_mockup_end, new_mockup_end)
else:
    print("[WARN] old_mockup_end not found")

# 3. Add 3-Car Multi-Bay Diversity Section before Features
old_features_start = """    <!-- Core Features Grid -->
    <section id="features" style="background: white; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">"""

new_features_start = """    <!-- 3-Car Diversity Section -->
    <section style="background: white; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 70px 0;">
      <div class="container">
        <div class="section-head" style="margin-bottom: 40px;">
          <span class="badge"><span class="badge-dot"></span> Multi-Vehicle Garage Management</span>
          <h2>Built for Whatever Sits in Your Bay</h2>
          <p>From modern commuter hybrids to vintage carburetor classics and heavy-duty 4x4s.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
          <!-- Card 1: Daily Commuter -->
          <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 18px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div style="height: 160px; overflow: hidden; background: #F1F5F9;">
              <img src="assets/civic_sport.jpg" onerror="this.src='civic_sport.jpg'" alt="2021 Honda Civic Sport" style="width: 100%; height: 100%; object-fit: cover;" />
            </div>
            <div style="padding: 20px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 10px; font-weight: 800; color: #0284C7; background: #E0F2FE; padding: 2px 8px; border-radius: 4px;">DAILY COMMUTER</span>
                <span style="font-size: 12px; font-weight: 700; color: var(--text);">34.2 MPG</span>
              </div>
              <h3 style="font-size: 17px; font-weight: 800; color: var(--text); margin-bottom: 4px;">2021 Honda Civic Sport</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;">Track commute fuel economy, synthetic 0W-20 intervals, and tire wear without monthly subscriptions.</p>
              <div style="font-size: 11px; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 4px;">
                &#10003; 38,120 Miles &bull; Next Oil: 42,000
              </div>
            </div>
          </div>

          <!-- Card 2: 4x4 Truck -->
          <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 18px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div style="height: 160px; overflow: hidden; background: #F1F5F9;">
              <img src="assets/tacoma_trd.jpg" onerror="this.src='tacoma_trd.jpg'" alt="2018 Toyota Tacoma TRD 4x4" style="width: 100%; height: 100%; object-fit: cover;" />
            </div>
            <div style="padding: 20px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 10px; font-weight: 800; color: #059669; background: #ECFDF5; padding: 2px 8px; border-radius: 4px;">4WD &amp; TOWING</span>
                <span style="font-size: 12px; font-weight: 700; color: var(--text);">4-Corner Tread</span>
              </div>
              <h3 style="font-size: 17px; font-weight: 800; color: var(--text); margin-bottom: 4px;">2018 Toyota Tacoma TRD</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;">4-corner chassis tire tread depth monitoring, differential fluid records, and DIY oil filter tracking.</p>
              <div style="font-size: 11px; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 4px;">
                &#10003; 84,250 Miles &bull; Resale Dossier Ready
              </div>
            </div>
          </div>

          <!-- Card 3: Classic Project -->
          <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 18px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.03);">
            <div style="height: 160px; overflow: hidden; background: #F1F5F9;">
              <img src="assets/classic_bronco.jpg" onerror="this.src='classic_bronco.jpg'" alt="1974 Ford Bronco 302 Classic" style="width: 100%; height: 100%; object-fit: cover;" />
            </div>
            <div style="padding: 20px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 10px; font-weight: 800; color: #D97706; background: #FEF3C7; padding: 2px 8px; border-radius: 4px;">CLASSIC &bull; OPTIONAL VIN</span>
                <span style="font-size: 12px; font-weight: 700; color: var(--text);">V8 Project</span>
              </div>
              <h3 style="font-size: 17px; font-weight: 800; color: var(--text); margin-bottom: 4px;">1974 Ford Bronco 302</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;">Pre-1981 classic support with zero forced 17-digit VIN barriers. Document carb tuning, conversions, and receipts.</p>
              <div style="font-size: 11px; font-weight: 700; color: #D97706; display: flex; align-items: center; gap: 4px;">
                &#10003; 112,400 Miles &bull; Restoration in Progress
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Features Grid -->
    <section id="features" style="background: var(--bg); border-bottom: 1px solid var(--border);">"""

if old_features_start in content:
    content = content.replace(old_features_start, new_features_start)
else:
    print("[WARN] old_features_start not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] build_complete_landing.py updated with automotive imagery sections.")
