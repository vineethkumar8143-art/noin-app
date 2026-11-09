"""
Generates comprehensive legal, privacy, and support pages for TorqueKeep:
- privacy.html: Complete Google Play & App Store compliant 100% offline privacy policy.
- terms.html: Terms of Service with mechanic disclaimer, data ownership, and Google Play billing terms.
- support.html: Help center, backup tutorials, transfer guides, and contact channels.
Adheres strictly to daylight design system and clean room principles.
"""

import os

COMMON_HEAD = """
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%230F172A'><path d='M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83'/></svg>">
  <style>
    :root {
      --bg: #F8FAFC;
      --surface: #FFFFFF;
      --surface-elevated: #F1F5F9;
      --border: #E2E8F0;
      --border-focus: #94A3B8;
      --text: #0F172A;
      --text-muted: #64748B;
      --accent: #0F172A;
      --accent-hover: #1E293B;
      --on-accent: #FFFFFF;
      --success: #059669;
      --success-light: #ECFDF5;
      --warning: #D97706;
      --warning-light: #FEF3C7;
      --danger: #DC2626;
      --danger-light: #FEE2E2;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-family);
      line-height: 1.65;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Navbar */
    .navbar {
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 70px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text);
      font-weight: 800;
      font-size: 20px;
      letter-spacing: -0.02em;
    }
    .brand-icon {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: var(--accent);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 24px;
      list-style: none;
    }
    .nav-links a {
      text-decoration: none;
      color: var(--text-muted);
      font-size: 14px;
      font-weight: 600;
      transition: color 0.15s ease;
    }
    .nav-links a:hover, .nav-links a.active {
      color: var(--text);
    }
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
      border: 1px solid transparent;
    }
    .btn-primary {
      background: var(--accent);
      color: var(--on-accent);
    }
    .btn-primary:hover {
      background: var(--accent-hover);
    }

    /* Content Layout */
    .page-header {
      padding: 64px 0 32px 0;
      border-bottom: 1px solid var(--border);
      margin-bottom: 40px;
    }
    .meta-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      background: #F1F5F9;
      color: #334155;
      border: 1px solid #CBD5E1;
      margin-bottom: 16px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .page-title {
      font-size: 38px;
      font-weight: 900;
      letter-spacing: -0.02em;
      color: var(--text);
      margin-bottom: 12px;
    }
    .page-subhead {
      font-size: 16px;
      color: var(--text-muted);
    }

    /* Article Body */
    .legal-content {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 44px;
      margin-bottom: 64px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
    }
    .legal-section {
      margin-bottom: 36px;
    }
    .legal-section:last-child {
      margin-bottom: 0;
    }
    .legal-section h2 {
      font-size: 20px;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--surface-elevated);
    }
    .legal-section h3 {
      font-size: 16px;
      font-weight: 700;
      color: var(--text);
      margin: 18px 0 8px 0;
    }
    .legal-section p {
      font-size: 15px;
      color: #334155;
      margin-bottom: 14px;
      line-height: 1.7;
    }
    .legal-section ul, .legal-section ol {
      margin-left: 24px;
      margin-bottom: 16px;
    }
    .legal-section li {
      font-size: 15px;
      color: #334155;
      margin-bottom: 8px;
      line-height: 1.6;
    }
    
    /* Callout & Highlights */
    .callout {
      background: var(--surface-elevated);
      border-left: 4px solid var(--accent);
      padding: 16px 20px;
      border-radius: 0 12px 12px 0;
      margin: 20px 0;
    }
    .callout-success {
      background: var(--success-light);
      border-left-color: var(--success);
    }
    .callout-success p {
      color: #065F46;
      font-weight: 600;
    }
    .callout-warning {
      background: var(--warning-light);
      border-left-color: var(--warning);
    }
    .callout-warning p {
      color: #92400E;
    }

    /* Table */
    .data-table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 14px;
    }
    .data-table th, .data-table td {
      border: 1px solid var(--border);
      padding: 12px 16px;
      text-align: left;
    }
    .data-table th {
      background: var(--surface-elevated);
      font-weight: 700;
      color: var(--text);
    }

    /* FAQ accordion for Support */
    .support-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 16px;
    }
    .support-card h3 {
      font-size: 17px;
      font-weight: 800;
      margin-bottom: 8px;
    }
    .support-card p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Contact Box */
    .contact-box {
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      border-radius: 16px;
      padding: 32px;
      text-align: center;
      margin-top: 36px;
    }
    .contact-box h3 {
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 8px;
    }
    .contact-box p {
      font-size: 15px;
      color: var(--text-muted);
      margin-bottom: 20px;
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border);
      background: var(--surface);
      padding: 40px 0;
      font-size: 13px;
      color: var(--text-muted);
    }
    .footer-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .footer-links {
      display: flex;
      gap: 20px;
    }
    .footer-links a {
      color: var(--text-muted);
      text-decoration: none;
    }
    .footer-links a:hover {
      color: var(--text);
    }

    @media (max-width: 768px) {
      .legal-content { padding: 24px; }
      .page-title { font-size: 28px; }
      .nav-links { display: none; }
      .footer-inner { flex-direction: column; gap: 16px; text-align: center; }
    }
  </style>
"""

PRIVACY_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Privacy Policy &bull; TorqueKeep</title>
  <meta name="description" content="TorqueKeep Privacy Policy: 100% offline-first architecture, zero analytics trackers, zero telemetry, and complete on-device data sovereignty.">
  {COMMON_HEAD}
</head>
<body>

  <!-- Navigation -->
  <header class="navbar">
    <div class="container nav-inner">
      <a href="landing.html" class="brand">
        <div class="brand-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
          </svg>
        </div>
        <span>TorqueKeep</span>
      </a>
      <ul class="nav-links">
        <li><a href="landing.html">Home</a></li>
        <li><a href="privacy.html" class="active">Privacy</a></li>
        <li><a href="terms.html">Terms</a></li>
        <li><a href="support.html">Support</a></li>
      </ul>
      <a href="landing.html#pricing" class="btn btn-primary">Get App</a>
    </div>
  </header>

  <div class="container">
    <div class="page-header">
      <div class="meta-tag">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>
        Last Updated: November 7, 2026 &bull; Effective Immediately
      </div>
      <h1 class="page-title">TorqueKeep Privacy Policy</h1>
      <p class="page-subhead">Our core promise is simple: Your vehicle records belong to you, live exclusively on your device, and never touch our servers.</p>
    </div>

    <div class="legal-content">

      <div class="callout callout-success">
        <p>&#10003; <strong>Zero-Knowledge Guarantee:</strong> TorqueKeep does not require account creation, does not collect telemetry, contains zero third-party advertising SDKs, and does not upload your records to any remote cloud.</p>
      </div>

      <div class="legal-section">
        <h2>1. Architecture & Core Principles</h2>
        <p>
          TorqueKeep (&ldquo;we,&rdquo; &ldquo;our,&rdquo; or &ldquo;the application&rdquo;) is an Android mobile application engineered around a strict <strong>offline-first, zero-telemetry architecture</strong>. Unlike conventional automotive apps that require registration, store your driving habits in central cloud databases, or monetize via behavioural advertising networks, TorqueKeep operates autonomously on your smartphone.
        </p>
        <p>
          The application has <strong>no centralized user database</strong>. We do not maintain servers that log your name, email address, IP address, vehicle identification numbers (VIN), or service histories.
        </p>
      </div>

      <div class="legal-section">
        <h2>2. Information We Store Locally on Your Device</h2>
        <p>When you use TorqueKeep, all information you input is stored exclusively inside an encrypted local Room SQLite database in your device's isolated application sandbox (<code>/data/data/com.torquekeep.app/databases/</code>):</p>
        <ul>
          <li><strong>Vehicle Attributes:</strong> Vehicle nickname, year, make, model, initial odometer reading, distance unit preference (miles vs. kilometers), and optional VIN.</li>
          <li><strong>Service & Maintenance Logs:</strong> Date of service, odometer reading at service, service category (e.g., Oil, Tires, Brakes), cost amount in cents, part numbers, and user notes.</li>
          <li><strong>Fuel Fill-Up Records:</strong> Fuel volume in gallons or liters, total cost, odometer at pump, unit fuel price, and optional fuel station brand name.</li>
          <li><strong>Tire Tread Measurements:</strong> 4-point tire tread depth readings (Front-Left, Front-Right, Rear-Left, Rear-Right in 32nds of an inch or millimeters).</li>
          <li><strong>Pro Status Flag:</strong> A single boolean cryptographic token stored in Android SharedPreferences confirming Lifetime Pro or Flex subscription validity via Google Play Billing.</li>
        </ul>
      </div>

      <div class="legal-section">
        <h2>3. Information We Never Collect or Access</h2>
        <p>TorqueKeep purposefully eliminates telemetry. We do <strong>not</strong> collect, request, or transmit:</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>Data Category</th>
              <th>Collection Status</th>
              <th>Technical Explanation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>GPS & Geolocation</strong></td>
              <td>Zero Collection</td>
              <td>No location permissions (<code>ACCESS_FINE_LOCATION</code>) requested in <code>AndroidManifest.xml</code>.</td>
            </tr>
            <tr>
              <td><strong>Contact Lists & Address Books</strong></td>
              <td>Zero Collection</td>
              <td>TorqueKeep does not inspect your device contacts or phonebook.</td>
            </tr>
            <tr>
              <td><strong>Camera & Media Files</strong></td>
              <td>Local Only</td>
              <td>Receipt photos are selected strictly via Android Photo Picker and stored locally on your device filesystem.</td>
            </tr>
            <tr>
              <td><strong>Ad Identifiers (GAID / IDFA)</strong></td>
              <td>Zero Collection</td>
              <td>Zero ad-monetization or tracking SDKs are compiled into the binary.</td>
            </tr>
            <tr>
              <td><strong>Analytics & Crash Tracking</strong></td>
              <td>Zero Collection</td>
              <td>No Firebase Analytics, Mixpanel, Adjust, or third-party event trackers.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="legal-section">
        <h2>4. Third-Party Services & Payment Processing</h2>
        <p>
          TorqueKeep minimizes external touchpoints to only what is strictly necessary to process licensing:
        </p>
        <ul>
          <li>
            <strong>Google Play In-App Billing:</strong> When purchasing the optional Lifetime Multi-Bay upgrade ($19.99) or Flex subscription, the financial transaction is handled exclusively by Google Play (Google LLC). Your credit card details, billing address, and financial tokens are processed by Google under the <a href="https://policies.google.com/privacy" target="_blank" rel="noopener" style="color: var(--text); font-weight: 700;">Google Privacy Policy</a>. We never receive or store your payment details.
          </li>
          <li>
            <strong>Optional Google Drive / Cloud Backup:</strong> If you explicitly choose to backup your exported database archive to Google Drive or another storage provider, transmission occurs through Android's system-level Storage Access Framework (SAF). We do not operate an intermediary cloud proxy.
          </li>
        </ul>
      </div>

      <div class="legal-section">
        <h2>5. Your Data Control & Instant Deletion Rights</h2>
        <p>You maintain 100% custody of your automotive records at all times:</p>
        <ul>
          <li><strong>Universal Raw Export:</strong> You can export your full maintenance ledger to universal <code>.csv</code> or <code>.json</code> format at any time with a single tap in Settings.</li>
          <li><strong>Resale Dossier Generation:</strong> You can generate a self-contained PDF document directly on your device canvas without transmitting data to an external PDF conversion API.</li>
          <li><strong>One-Tap Database Purge:</strong> The in-app Privacy Guarantee screen provides an immediate &ldquo;Purge All Local Data&rdquo; button that physically drops and wipes all SQLite tables.</li>
          <li><strong>Application Uninstallation:</strong> Uninstalling the TorqueKeep application from your Android device permanently destroys all local SQLite files and attachments.</li>
        </ul>
      </div>

      <div class="legal-section">
        <h2>6. Children's Privacy</h2>
        <p>
          TorqueKeep is rated for General Audiences (Everyone 3+). We do not knowingly solicit or collect information from children under 13 years of age (or under 16 in applicable European jurisdictions), as our software collects no personal information from any user regardless of age.
        </p>
      </div>

      <div class="legal-section">
        <h2>7. Policy Changes & Updates</h2>
        <p>
          Because TorqueKeep relies on an offline architecture, any future modifications to how data is handled would require an explicit app update. If any architectural change ever impacts privacy, this policy will be revised, and noticeable release notes will be highlighted on the Google Play Store update log.
        </p>
      </div>

      <div class="legal-section">
        <h2>8. Contact Information</h2>
        <p>
          If you have questions, inquiries, or feedback regarding this Privacy Policy or our offline-first architecture, please contact:
        </p>
        <p>
          <strong>TorqueKeep Privacy Team</strong><br>
          Email: <a href="mailto:privacy@torquekeep.com" style="color: var(--text); font-weight: 700;">privacy@torquekeep.com</a><br>
          Website: <a href="https://torquekeep.com" style="color: var(--text); font-weight: 700;">torquekeep.com</a>
        </p>
      </div>

    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container footer-inner">
      <div>
        <strong>TorqueKeep</strong> &mdash; 100% Offline Vehicle Maintenance & Buyer Resale Dossier.
      </div>
      <div class="footer-links">
        <a href="landing.html">Home</a>
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
        <a href="support.html">Support</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""

TERMS_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Terms of Service &bull; TorqueKeep</title>
  <meta name="description" content="TorqueKeep Terms of Service: End-user license, disclaimer of mechanical warranties, and Google Play purchase terms.">
  {COMMON_HEAD}
</head>
<body>

  <!-- Navigation -->
  <header class="navbar">
    <div class="container nav-inner">
      <a href="landing.html" class="brand">
        <div class="brand-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
          </svg>
        </div>
        <span>TorqueKeep</span>
      </a>
      <ul class="nav-links">
        <li><a href="landing.html">Home</a></li>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="terms.html" class="active">Terms</a></li>
        <li><a href="support.html">Support</a></li>
      </ul>
      <a href="landing.html#pricing" class="btn btn-primary">Get App</a>
    </div>
  </header>

  <div class="container">
    <div class="page-header">
      <div class="meta-tag">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        Effective Date: November 7, 2026
      </div>
      <h1 class="page-title">TorqueKeep Terms of Service</h1>
      <p class="page-subhead">Please read these terms carefully before downloading, installing, or using the TorqueKeep application.</p>
    </div>

    <div class="legal-content">

      <div class="legal-section">
        <h2>1. Acceptance of Terms</h2>
        <p>
          By downloading, installing, accessing, or using the TorqueKeep mobile application, website, or associated documentation (&ldquo;the Service&rdquo;), you agree to be legally bound by these Terms of Service (&ldquo;Terms&rdquo;). If you do not agree to all terms and conditions set forth herein, do not install or use the Service.
        </p>
      </div>

      <div class="legal-section">
        <h2>2. License Grant & Scope of Use</h2>
        <p>
          Subject to these Terms, TorqueKeep grants you a non-exclusive, non-transferable, revocable, personal license to install and run the application on Android devices that you own or control, solely for personal or legitimate garage vehicle record-keeping purposes.
        </p>
        <p>
          You agree not to reverse-engineer, decompile, disassemble, or derive source code from compiled application binaries, except to the extent permitted by mandatory statutory law.
        </p>
      </div>

      <div class="legal-section">
        <h2>3. Mechanical & Automotive Safety Disclaimer</h2>
        <div class="callout callout-warning">
          <p><strong>IMPORTANT AUTOMOTIVE DISCLAIMER:</strong> TorqueKeep is an administrative record-keeping tool. It is not an onboard diagnostic scanner, professional mechanical inspection system, or substitute for your vehicle manufacturer's official Owner's Manual or certified technician guidance.</p>
        </div>
        <p>
          The application provides estimated fuel economy, tire tread depth tracking, and scheduled maintenance reminders based strictly on user-entered numerical values and intervals. TorqueKeep does not verify the physical mechanical condition, roadworthiness, brake safety, or tire integrity of any vehicle.
        </p>
        <p>
          You are solely responsible for ensuring your vehicle is operated safely and serviced according to OEM guidelines and statutory road safety requirements. Under no circumstances shall TorqueKeep be liable for vehicle mechanical breakdowns, part failures, accidents, personal injuries, or roadside damage.
        </p>
      </div>

      <div class="legal-section">
        <h2>4. Buyer Resale Dossier Disclaimer</h2>
        <p>
          TorqueKeep enables users to generate printable &ldquo;Buyer Resale Dossier&rdquo; PDF reports summarizing their vehicle maintenance history. You acknowledge and represent that all data, odometer entries, dates, and repair costs input into the application are accurate and true.
        </p>
        <p>
          TorqueKeep does not certify, stamp, or independently inspect vehicle records against state DMV, police, or title registries. If you use a generated dossier to facilitate a private vehicle sale, you alone bear sole legal responsibility for the representations made to prospective buyers.
        </p>
      </div>

      <div class="legal-section">
        <h2>5. Purchases, Billing & Refunds</h2>
        <p>
          TorqueKeep offers both a Free Tier (1 vehicle bay with core logging, fuel tracking, tire diagnostics, and raw data export) and an optional Pro Tier (Multi-Bay Lifetime or Flex):
        </p>
        <ul>
          <li><strong>One-Time Lifetime Unlock ($19.99 USD):</strong> Grants permanent, lifetime access to unlimited vehicle bays, multi-page watermarked PDF dossiers, and priority support. No recurring billing.</li>
          <li><strong>Monthly Flex Pass ($2.99/mo USD):</strong> A recurring monthly subscription billed through Google Play Billing. You may cancel at any time via your Google Play account settings.</li>
          <li><strong>Payment Processing:</strong> All in-app purchases and subscriptions are processed by Google Play. Refund eligibility, tax assessment, and dispute resolution are governed by Google Play's standard terms of purchase.</li>
        </ul>
      </div>

      <div class="legal-section">
        <h2>6. Data Ownership & Local Custody</h2>
        <p>
          You retain 100% intellectual property ownership of all vehicle data, notes, and maintenance entries recorded in TorqueKeep. Because the application operates offline without centralized cloud hosting, <strong>you are solely responsible for creating periodic backups</strong> using the built-in CSV/JSON export tools. TorqueKeep cannot recover data lost due to device damage, factory resets, or local uninstallation.
        </p>
      </div>

      <div class="legal-section">
        <h2>7. Limitation of Liability</h2>
        <p>
          TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT SHALL TORQUEKEEP, ITS CREATORS, OR CONTRIBUTORS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE, OR CONSEQUENTIAL DAMAGES (INCLUDING LOSS OF DATA, LOSS OF VEHICLE VALUE, ENGINE DAMAGE, OR LOSS OF PROFITS) ARISING OUT OF OR IN CONNECTION WITH THE USE OR INABILITY TO USE THE APPLICATION, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
        </p>
      </div>

      <div class="legal-section">
        <h2>8. Contact & Legal Inquiries</h2>
        <p>
          For questions regarding these Terms of Service, please contact:
        </p>
        <p>
          <strong>TorqueKeep Legal Department</strong><br>
          Email: <a href="mailto:legal@torquekeep.com" style="color: var(--text); font-weight: 700;">legal@torquekeep.com</a>
        </p>
      </div>

    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container footer-inner">
      <div>
        <strong>TorqueKeep</strong> &mdash; 100% Offline Vehicle Maintenance & Buyer Resale Dossier.
      </div>
      <div class="footer-links">
        <a href="landing.html">Home</a>
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
        <a href="support.html">Support</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""

SUPPORT_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Help Center & Support &bull; TorqueKeep</title>
  <meta name="description" content="TorqueKeep Support: FAQs, data export and transfer tutorials, Google Play purchase restoration, and direct contact channels.">
  {COMMON_HEAD}
</head>
<body>

  <!-- Navigation -->
  <header class="navbar">
    <div class="container nav-inner">
      <a href="landing.html" class="brand">
        <div class="brand-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
          </svg>
        </div>
        <span>TorqueKeep</span>
      </a>
      <ul class="nav-links">
        <li><a href="landing.html">Home</a></li>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="terms.html">Terms</a></li>
        <li><a href="support.html" class="active">Support</a></li>
      </ul>
      <a href="landing.html#pricing" class="btn btn-primary">Get App</a>
    </div>
  </header>

  <div class="container">
    <div class="page-header">
      <div class="meta-tag">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        TorqueKeep Knowledge Base
      </div>
      <h1 class="page-title">How Can We Help You?</h1>
      <p class="page-subhead">Explore step-by-step guides, troubleshooting instructions, or get in touch with our team.</p>
    </div>

    <!-- Frequently Asked Questions -->
    <div style="margin-bottom: 48px;">
      <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Frequently Answered Guides</h2>

      <div class="support-card">
        <h3>How do I transfer my vehicle records to a new Android phone?</h3>
        <p>
          Because TorqueKeep is 100% offline, your records are not stored on our servers. To transfer to a new device:<br>
          1. On your old phone, go to <strong>Settings / Privacy &rarr; Export Data (CSV / JSON)</strong>.<br>
          2. Save the file to your Google Drive, SD card, or email it to yourself.<br>
          3. On your new phone, install TorqueKeep and tap <strong>Settings &rarr; Import Data</strong>, then select your exported file. All bays, logs, and fuel entries will restore in seconds.
        </p>
      </div>

      <div class="support-card">
        <h3>I purchased the Lifetime Pro Upgrade. How do I restore it on my new phone?</h3>
        <p>
          Google Play automatically tracks your purchases. Ensure you are signed into the same Google account on your new device, open TorqueKeep, navigate to <strong>Garage &rarr; Unlock Pro</strong>, and tap <strong>&ldquo;Restore Purchase&rdquo;</strong>. The app will query the Google Play Billing client and immediately activate your Pro license.
        </p>
      </div>

      <div class="support-card">
        <h3>How does the 4-Corner Tire Tread Diagnostic work?</h3>
        <p>
          Under any vehicle bay, tap <strong>&ldquo;+ Tread Check&rdquo;</strong>. The interactive schematic maps Front-Left, Front-Right, Rear-Left, and Rear-Right wheels. Enter tread depth in 32nds of an inch (standard US gauge) or millimeters. If the application detects an uneven variance greater than 3/32&Prime; between tires, it automatically highlights a tire rotation warning to protect tire longevity.
        </p>
      </div>

      <div class="support-card">
        <h3>Can I track motorcycles, trailers, or classic cars without a 17-digit VIN?</h3>
        <p>
          Yes! The VIN field is 100% optional in TorqueKeep. Pre-1981 classic cars, vintage project trucks, motorcycles, and race cars can be added with zero errors or validation warnings.
        </p>
      </div>

      <div class="support-card">
        <h3>How do I print or share the Buyer Resale Dossier?</h3>
        <p>
          Tap the <strong>&ldquo;Dossier&rdquo;</strong> tab in the bottom navigation. Verify your car's details and tap <strong>&ldquo;Generate PDF Dossier&rdquo;</strong>. TorqueKeep compiles a vector A4 PDF using native Android rendering. You can immediately share it via WhatsApp, email it to an interested buyer, or print it directly via any Android-compatible printer.
        </p>
      </div>

      <div class="support-card">
        <h3>Does TorqueKeep ever share or sell my vehicle data?</h3>
        <p>
          Never. TorqueKeep makes zero outbound network requests and has zero tracking SDKs. Your records stay encrypted on your device and are never transmitted to insurance agencies, data brokers, or advertisers.
        </p>
      </div>
    </div>

    <!-- Contact Box -->
    <div class="contact-box">
      <h3>Still Have Questions or Found a Bug?</h3>
      <p>We are a dedicated garage software team. Email us with details and we'll reply promptly.</p>
      <a href="mailto:support@torquekeep.com" class="btn btn-primary" style="padding: 12px 28px; font-size: 15px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        Contact support@torquekeep.com
      </a>
      <div style="margin-top: 14px; font-size: 12px; color: var(--text-muted);">
        Typical response time: Under 24 hours &bull; Include your Android OS version & phone model for technical queries.
      </div>
    </div>

    <div style="height: 64px;"></div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container footer-inner">
      <div>
        <strong>TorqueKeep</strong> &mdash; 100% Offline Vehicle Maintenance & Buyer Resale Dossier.
      </div>
      <div class="footer-links">
        <a href="landing.html">Home</a>
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
        <a href="support.html">Support</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""

def main():
    pages = [
        ("privacy.html", PRIVACY_HTML),
        ("terms.html", TERMS_HTML),
        ("support.html", SUPPORT_HTML),
    ]

    brain_dir = r"C:\Users\vinee\.gemini\antigravity\brain\380c6241-6d0c-483e-aa3e-4e5f725d6e16"
    root_dir = r"d:\Project01"

    for filename, content in pages:
        # Write to root
        root_path = os.path.join(root_dir, filename)
        with open(root_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated: {root_path} ({len(content)} bytes)")

        # Write to brain artifacts
        brain_path = os.path.join(brain_dir, filename)
        with open(brain_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Generated: {brain_path} ({len(content)} bytes)")

if __name__ == "__main__":
    main()
