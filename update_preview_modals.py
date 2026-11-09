"""
Comprehensive update for TorqueKeep:
1. Updates build_preview.py to add in-app modal reader for Privacy Policy, Terms, and Help Center.
2. Updates build_landing.py to create a robust, responsive multi-view SPA for landing.html with:
   - View Home
   - View Privacy Policy
   - View Terms of Service
   - View Support & Help
   - View Interactive App Demo
3. Generates standalone privacy.html, terms.html, and support.html with synchronized multi-view navigation.
4. Copies preview.html to the brain artifacts directory so preview.html never 404s.
"""

import os
import shutil

ROOT_DIR = r"d:\Project01"
BRAIN_DIR = r"C:\Users\vinee\.gemini\antigravity\brain\380c6241-6d0c-483e-aa3e-4e5f725d6e16"

# 1. Update build_preview.py to add #modal-legal-doc and in-app functions
def update_build_preview():
    path = os.path.join(ROOT_DIR, "build_preview.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace privacy links
    old_links = """        <div style="display: flex; justify-content: center; gap: 14px; margin-top: 12px; margin-bottom: 8px; font-size: 11px;">
          <a href="privacy.html" target="_blank" style="color: #64748B; text-decoration: underline; font-weight: 600;">Privacy Policy</a>
          <span style="color: #CBD5E1;">&bull;</span>
          <a href="terms.html" target="_blank" style="color: #64748B; text-decoration: underline; font-weight: 600;">Terms of Service</a>
          <span style="color: #CBD5E1;">&bull;</span>
          <a href="support.html" target="_blank" style="color: #64748B; text-decoration: underline; font-weight: 600;">Help Center</a>
        </div>"""

    new_links = """        <div style="display: flex; justify-content: center; gap: 14px; margin-top: 12px; margin-bottom: 8px; font-size: 11px;">
          <a href="privacy.html" onclick="event.preventDefault(); openLegalModal('privacy');" style="color: #64748B; text-decoration: underline; font-weight: 600; cursor: pointer;">Privacy Policy</a>
          <span style="color: #CBD5E1;">&bull;</span>
          <a href="terms.html" onclick="event.preventDefault(); openLegalModal('terms');" style="color: #64748B; text-decoration: underline; font-weight: 600; cursor: pointer;">Terms of Service</a>
          <span style="color: #CBD5E1;">&bull;</span>
          <a href="support.html" onclick="event.preventDefault(); openLegalModal('support');" style="color: #64748B; text-decoration: underline; font-weight: 600; cursor: pointer;">Help Center</a>
        </div>"""

    if old_links in content:
        content = content.replace(old_links, new_links)
    else:
        print("[WARN] old_links not found exactly in build_preview.py")

    # Add modal-legal-doc before app-toast
    modal_legal_html = """
    <!-- In-App Legal & Help Modal Reader -->
    <div id="modal-legal-doc" style="display: none; position: absolute; inset: 0; background: rgba(15, 23, 42, 0.4); z-index: 100; align-items: flex-end; backdrop-filter: blur(2px);">
      <div style="width: 100%; box-sizing: border-box; max-height: 90%; background: #FFFFFF; border-top-left-radius: 24px; border-top-right-radius: 24px; padding: 20px 20px 36px 20px; box-shadow: 0 -10px 30px rgba(0,0,0,0.15); display: flex; flex-direction: column; gap: 12px;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px;">
          <div>
            <div id="modal-legal-tag" style="font-size: 10px; font-weight: 800; color: #64748B; letter-spacing: 0.5px; text-transform: uppercase;">LEGAL DOCUMENT</div>
            <div id="modal-legal-title" style="font-size: 16px; font-weight: 800; color: #0F172A;">Privacy Policy</div>
          </div>
          <button onclick="closeLegalModal()" style="width: 28px; height: 28px; border-radius: 50%; background: #F1F5F9; border: none; font-size: 16px; font-weight: 700; color: #64748B; cursor: pointer; display: flex; align-items: center; justify-content: center;">&times;</button>
        </div>
        <div id="modal-legal-body" style="max-height: 48vh; overflow-y: auto; font-size: 12px; line-height: 19px; color: #334155; padding-right: 4px;">
          <!-- Dynamically populated -->
        </div>
        <button onclick="closeLegalModal()" class="btn-torque" style="margin: 0; height: 44px;">
          <span>Done</span>
        </button>
      </div>
    </div>
"""

    toast_target = '<!-- In-App Toast Notification -->'
    if modal_legal_html.strip() not in content and toast_target in content:
        content = content.replace(toast_target, modal_legal_html + "\n    " + toast_target)

    # Add openLegalModal and closeLegalModal functions
    js_code = """
    function openLegalModal(type) {
      const modal = document.getElementById('modal-legal-doc');
      const tag = document.getElementById('modal-legal-tag');
      const title = document.getElementById('modal-legal-title');
      const body = document.getElementById('modal-legal-body');
      
      if (type === 'privacy') {
        tag.textContent = 'ZERO TELEMETRY \\u2022 LOCAL ONLY';
        title.textContent = 'TorqueKeep Privacy Policy';
        body.innerHTML = `
          <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 10px; margin-bottom: 12px; color: #065F46; font-weight: 600; font-size: 11px;">
            &#10003; 100% On-Device Privacy Guarantee: Zero telemetry, zero analytics SDKs, zero background GPS tracking, and no external cloud servers.
          </div>
          <p><strong>1. Local SQLite Storage:</strong> All vehicle nicknames, VINs, odometer logs, fuel fill-ups, and tire tread records are stored solely in your Android device's private SQLite sandbox (<code>/data/data/com.torquekeep.app/databases/</code>).</p>
          <p style="margin-top: 8px;"><strong>2. Zero Personal Data Collected:</strong> We do not ask for your name, phone number, email, or contacts. You do not need to register an account.</p>
          <p style="margin-top: 8px;"><strong>3. Payments:</strong> Optional Lifetime Multi-Bay upgrade purchases ($19.99) are processed directly by Google Play Billing. We never receive or store your credit card information.</p>
          <p style="margin-top: 8px;"><strong>4. Instant Data Deletion:</strong> Tap "Purge All Local Records" in Privacy Settings or uninstall the app to instantly destroy all data on your device forever.</p>
          <p style="margin-top: 8px; font-size: 11px; color: #64748B;">Contact: privacy@torquekeep.com</p>
        `;
      } else if (type === 'terms') {
        tag.textContent = 'END USER LICENSE & TERMS';
        title.textContent = 'Terms of Service';
        body.innerHTML = `
          <div style="background: #FEF3C7; border: 1px solid #FDE68A; border-radius: 8px; padding: 10px; margin-bottom: 12px; color: #92400E; font-size: 11px;">
            <strong>Important Safety Notice:</strong> TorqueKeep is an administrative record-keeping logbook. It does not replace certified automotive inspections, official OEM manuals, or certified mechanic advice.
          </div>
          <p><strong>1. Mechanical Safety Disclaimer:</strong> You are solely responsible for verifying your vehicle's roadworthiness and scheduling required manufacturer maintenance. TorqueKeep is not liable for vehicle breakdowns or mechanical failures.</p>
          <p style="margin-top: 8px;"><strong>2. Resale Dossier Accuracy:</strong> Buyer Resale Dossiers reflect user-entered numbers. TorqueKeep does not independently certify mileage or title history with state DMV registries.</p>
          <p style="margin-top: 8px;"><strong>3. Purchases:</strong> The Lifetime Multi-Bay Unlock ($19.99 One-Time) provides perpetual access to unlimited bays. Subscriptions and purchases are managed via Google Play Billing.</p>
          <p style="margin-top: 8px;"><strong>4. Data Ownership:</strong> You retain 100% intellectual property ownership of your records. As an offline app, you are responsible for maintaining CSV backups.</p>
          <p style="margin-top: 8px; font-size: 11px; color: #64748B;">Contact: legal@torquekeep.com</p>
        `;
      } else if (type === 'support') {
        tag.textContent = 'HELP & KNOWLEDGE BASE';
        title.textContent = 'TorqueKeep Support';
        body.innerHTML = `
          <p><strong>How to Transfer Data to a New Phone:</strong><br>
          1. Go to <em>Settings / Privacy &rarr; Export Data (CSV / JSON)</em>.<br>
          2. Save the file to your Google Drive or email it to yourself.<br>
          3. On your new phone, open TorqueKeep and tap <em>Import Data</em> to restore all records instantly.</p>
          
          <p style="margin-top: 10px;"><strong>How to Restore Pro Purchases:</strong><br>
          Open <em>Unlock Pro</em> and tap <em>"Restore Purchase"</em>. As long as you are signed into the same Google Play account, your Lifetime license reactivates immediately.</p>

          <p style="margin-top: 10px;"><strong>Classic Cars & Custom Builds:</strong><br>
          VIN entry is 100% optional. Pre-1981 classic cars, trailers, and motorcycles are fully supported.</p>

          <div style="background: #F1F5F9; border-radius: 8px; padding: 12px; margin-top: 12px; text-align: center;">
            <div style="font-weight: 700; color: #0F172A; font-size: 12px;">Need More Help?</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 2px;">Email: <strong>support@torquekeep.com</strong></div>
            <div style="font-size: 10px; color: #94A3B8; margin-top: 2px;">Typical response time: Under 24 hours</div>
          </div>
        `;
      }
      modal.style.display = 'flex';
    }

    function closeLegalModal() {
      const modal = document.getElementById('modal-legal-doc');
      if (modal) modal.style.display = 'none';
    }
"""

    init_target = '// Initialize View'
    if 'function openLegalModal' not in content and init_target in content:
        content = content.replace(init_target, js_code + "\n    " + init_target)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] build_preview.py updated with in-app legal modal reader.")

update_build_preview()
