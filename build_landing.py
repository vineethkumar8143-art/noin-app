"""
Builds the standalone, responsive, high-converting product landing page for TorqueKeep.
Adheres strictly to tokens.json daylight theme and replica-launch principles.
"""

import os

LANDING_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TorqueKeep — Offline Vehicle Logbook & Buyer Resale Dossier</title>
  <meta name="description" content="The privacy-first, 100% offline vehicle maintenance logbook and service tracker for Android. Zero subscriptions, zero telemetry, buyer-ready PDF dossiers.">
  <style>
    :root {
      --bg: #F8FAFC;
      --surface: #FFFFFF;
      --surface-card: #FFFFFF;
      --surface-elevated: #F1F5F9;
      --border: #E2E8F0;
      --border-focus: #94A3B8;
      --text: #0F172A;
      --text-muted: #64748B;
      --text-subtle: #94A3B8;
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

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-family);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    /* Container & Layout */
    .container {
      max-width: 1140px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Navbar */
    .navbar {
      background: rgba(255, 255, 255, 0.9);
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
      height: 72px;
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
      gap: 32px;
      list-style: none;
    }
    .nav-links a {
      text-decoration: none;
      color: var(--text-muted);
      font-size: 14px;
      font-weight: 600;
      transition: color 0.15s ease;
    }
    .nav-links a:hover {
      color: var(--text);
    }
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 24px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
      border: 1px solid transparent;
    }
    .btn-primary {
      background: var(--accent);
      color: var(--on-accent);
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
    }
    .btn-primary:hover {
      background: var(--accent-hover);
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(15, 23, 42, 0.16);
    }
    .btn-secondary {
      background: var(--surface);
      color: var(--text);
      border-color: var(--border);
    }
    .btn-secondary:hover {
      background: var(--surface-elevated);
    }

    /* Hero Section */
    .hero {
      padding: 96px 0 64px 0;
      text-align: center;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      background: #F1F5F9;
      color: #334155;
      border: 1px solid #CBD5E1;
      margin-bottom: 24px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--success);
    }
    .hero h1 {
      font-size: 52px;
      line-height: 1.15;
      letter-spacing: -0.03em;
      font-weight: 900;
      color: var(--text);
      max-width: 860px;
      margin: 0 auto 20px auto;
    }
    .hero p {
      font-size: 19px;
      color: var(--text-muted);
      max-width: 680px;
      margin: 0 auto 36px auto;
      line-height: 1.6;
    }
    .hero-cta-cluster {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin-bottom: 56px;
    }
    .trust-strip {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 28px;
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .trust-item {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Hero Product Mockup */
    .hero-mockup-wrap {
      margin-top: 48px;
      position: relative;
    }
    .mockup-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 24px;
      box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.1);
      padding: 32px;
      max-width: 900px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 32px;
      text-align: left;
    }
    .mockup-left {
      background: #F8FAFC;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
    }
    .mockup-vehicle-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
    }
    .mockup-car-title {
      font-size: 18px;
      font-weight: 800;
      color: var(--text);
    }
    .mockup-car-sub {
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .mockup-stat-box {
      background: white;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 16px;
    }
    .mockup-stat-label {
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.05em;
    }
    .mockup-stat-val {
      font-size: 26px;
      font-weight: 900;
      color: var(--text);
      letter-spacing: -0.02em;
    }
    .mockup-tiles-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .mockup-tile {
      background: white;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 8px;
      text-align: center;
      font-size: 11px;
      font-weight: 700;
      color: var(--text);
    }
    .mockup-tile svg {
      display: block;
      margin: 0 auto 4px auto;
      width: 18px;
      height: 18px;
    }
    .mockup-right {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .mockup-right h3 {
      font-size: 24px;
      font-weight: 800;
      margin-bottom: 12px;
      color: var(--text);
      line-height: 1.3;
    }
    .mockup-right p {
      font-size: 15px;
      color: var(--text-muted);
      margin-bottom: 24px;
    }
    .feature-bullet {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 14px;
      font-size: 14px;
      color: var(--text);
    }
    .feature-bullet svg {
      width: 20px;
      height: 20px;
      color: var(--success);
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* Section Styles */
    section {
      padding: 80px 0;
    }
    .section-head {
      text-align: center;
      max-width: 680px;
      margin: 0 auto 56px auto;
    }
    .section-head h2 {
      font-size: 36px;
      font-weight: 900;
      letter-spacing: -0.02em;
      color: var(--text);
      margin-bottom: 16px;
    }
    .section-head p {
      font-size: 17px;
      color: var(--text-muted);
    }

    /* The Problem Section */
    .problem-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .problem-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 28px;
      position: relative;
    }
    .problem-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: #FEE2E2;
      color: var(--danger);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
    }
    .problem-card h3 {
      font-size: 18px;
      font-weight: 800;
      margin-bottom: 10px;
      color: var(--text);
    }
    .problem-card p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* How It Works */
    .steps-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
      position: relative;
    }
    .step-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 32px;
      text-align: left;
    }
    .step-num {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: var(--accent);
      color: white;
      font-weight: 800;
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
    }
    .step-card h3 {
      font-size: 19px;
      font-weight: 800;
      margin-bottom: 10px;
    }
    .step-card p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Core Features Grid */
    .features-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }
    .feat-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 32px;
      display: flex;
      gap: 20px;
    }
    .feat-icon-box {
      width: 50px;
      height: 50px;
      border-radius: 14px;
      background: #F1F5F9;
      color: var(--accent);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .feat-card h3 {
      font-size: 18px;
      font-weight: 800;
      margin-bottom: 8px;
    }
    .feat-card p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Pricing Section */
    .pricing-table-wrap {
      max-width: 840px;
      margin: 0 auto;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 24px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
      overflow: hidden;
    }
    .pricing-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
    .pricing-col {
      padding: 40px;
    }
    .pricing-col.pro {
      background: #F8FAFC;
      border-left: 1px solid var(--border);
      position: relative;
    }
    .pricing-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 800;
      background: var(--accent);
      color: white;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 16px;
    }
    .plan-title {
      font-size: 22px;
      font-weight: 800;
      margin-bottom: 8px;
    }
    .plan-price {
      font-size: 42px;
      font-weight: 900;
      letter-spacing: -0.03em;
      margin-bottom: 6px;
    }
    .plan-price span {
      font-size: 16px;
      font-weight: 600;
      color: var(--text-muted);
    }
    .plan-desc {
      font-size: 14px;
      color: var(--text-muted);
      margin-bottom: 28px;
      min-height: 42px;
    }
    .plan-features {
      list-style: none;
      margin-bottom: 32px;
    }
    .plan-features li {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 14px;
      margin-bottom: 12px;
      color: var(--text);
    }
    .plan-features li svg {
      width: 18px;
      height: 18px;
      color: var(--success);
      flex-shrink: 0;
    }

    /* FAQ */
    .faq-grid {
      max-width: 780px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .faq-item {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
    }
    .faq-item h4 {
      font-size: 17px;
      font-weight: 800;
      margin-bottom: 10px;
      color: var(--text);
    }
    .faq-item p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Final CTA */
    .cta-banner {
      background: var(--accent);
      color: white;
      border-radius: 28px;
      padding: 64px 32px;
      text-align: center;
      margin: 64px 0 96px 0;
    }
    .cta-banner h2 {
      font-size: 38px;
      font-weight: 900;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
    }
    .cta-banner p {
      font-size: 18px;
      color: #94A3B8;
      max-width: 600px;
      margin: 0 auto 36px auto;
    }
    .cta-banner .btn-light {
      background: white;
      color: var(--accent);
      padding: 14px 32px;
      font-size: 16px;
      font-weight: 800;
    }
    .cta-banner .btn-light:hover {
      background: #F1F5F9;
      transform: translateY(-1px);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border);
      background: var(--surface);
      padding: 48px 0;
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
      gap: 24px;
    }
    .footer-links a {
      color: var(--text-muted);
      text-decoration: none;
    }
    .footer-links a:hover {
      color: var(--text);
    }

    /* Responsive */
    @media (max-width: 900px) {
      .mockup-card, .problem-grid, .steps-grid, .features-grid, .pricing-grid {
        grid-template-columns: 1fr;
      }
      .hero h1 { font-size: 36px; }
      .nav-links { display: none; }
      .pricing-col.pro { border-left: none; border-top: 1px solid var(--border); }
    }
  </style>
</head>
<body>

  <!-- Navigation -->
  <header class="navbar">
    <div class="container nav-inner">
      <a href="#" class="brand">
        <div class="brand-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>
          </svg>
        </div>
        <span>TorqueKeep</span>
      </a>
      <ul class="nav-links">
        <li><a href="#problem">Why TorqueKeep</a></li>
        <li><a href="#how-it-works">How It Works</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="support.html">Support</a></li>
      </ul>
      <a href="#pricing" class="btn btn-primary">Get TorqueKeep Free</a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="badge">
        <span class="badge-dot"></span>
        100% Offline-First Architecture &bull; No Forced Accounts
      </div>
      <h1>Your Garage. Your Records.<br>Zero Subscriptions.</h1>
      <p>
        The privacy-first vehicle maintenance logbook and service tracker that lives on your phone,
        not in an abandoned cloud server. Generate buyer-ready PDF dossiers anytime.
      </p>
      <div class="hero-cta-cluster">
        <a href="#pricing" class="btn btn-primary" style="padding: 14px 32px; font-size: 16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="7 10 12 15 17 10"/>
            <line x1="12" y1="15" x2="12" y2="3"/>
          </svg>
          Download for Android
        </a>
        <a href="preview.html" class="btn btn-secondary" style="padding: 14px 28px; font-size: 16px;" target="_blank">
          Live Interactive Demo &rarr;
        </a>
      </div>
      <div class="trust-strip">
        <div class="trust-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Zero Ads or Trackers
        </div>
        <div class="trust-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          Instant CSV & PDF Export
        </div>
        <div class="trust-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          One-Time Lifetime Option
        </div>
      </div>

      <!-- Hero Product Mockup -->
      <div class="hero-mockup-wrap">
        <div class="mockup-card">
          <div class="mockup-left">
            <div class="mockup-vehicle-header">
              <div>
                <div class="mockup-car-title">2018 Toyota Tacoma TRD</div>
                <div class="mockup-car-sub">Bay 01 &bull; 84,250 Miles</div>
              </div>
              <span style="font-size: 11px; font-weight: 800; background: #ECFDF5; color: #059669; padding: 4px 8px; border-radius: 6px;">HEALTHY</span>
            </div>
            <div class="mockup-stat-box">
              <div class="mockup-stat-label">Total Documented Care</div>
              <div class="mockup-stat-val">$1,842.50</div>
            </div>
            <div style="font-size: 11px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 8px;">1-Tap Service Logging</div>
            <div class="mockup-tiles-grid">
              <div class="mockup-tile" style="border: 2px solid var(--accent); background: #F1F5F9;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 8h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z"/></svg>
                Oil & Filter
              </div>
              <div class="mockup-tile">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/></svg>
                Tyres
              </div>
              <div class="mockup-tile">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="8"/></svg>
                Brakes
              </div>
              <div class="mockup-tile">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="6" width="16" height="13" rx="2"/></svg>
                Battery
              </div>
              <div class="mockup-tile">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/></svg>
                Inspection
              </div>
              <div class="mockup-tile">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4"/></svg>
                Other
              </div>
            </div>
          </div>
          <div class="mockup-right">
            <h3>Built for Garage Hands, Not Silicon Valley Algorithms</h3>
            <p>
              Most vehicle apps make you log into cloud accounts, bombard you with full-screen video ads, and charge yearly subscriptions just to record an oil change.
            </p>
            <div class="feature-bullet">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>48dp Touch Targets:</strong> Easy to tap with greasy or gloved fingers in the garage bay.</span>
            </div>
            <div class="feature-bullet">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>1-Click Buyer Resale Dossier:</strong> Print or email an immaculate A4 proof-of-care history when selling.</span>
            </div>
            <div class="feature-bullet">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Classic & Project Friendly:</strong> Works for pre-1981 cars, trailers, and motorcycles without 17-digit VINs.</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- The Problem Section -->
  <section id="problem" style="background: white; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
    <div class="container">
      <div class="section-head">
        <h2>What's Wrong With Today's Car Apps</h2>
        <p>You paid for your car. You shouldn't have to rent your own maintenance records.</p>
      </div>
      <div class="problem-grid">
        <div class="problem-card">
          <div class="problem-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3>The $40/Year Subscription Trap</h3>
          <p>
            Legacy apps charge $30&ndash;$45 every single year just to calculate fuel economy and notify you when tires need rotation. Stop renting utility tools.
          </p>
        </div>
        <div class="problem-card">
          <div class="problem-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          </div>
          <h3>Hostage Service Data</h3>
          <p>
            When cloud startups get acquired or abandon their servers, years of oil changes, parts receipts, and warranty proof disappear without warning.
          </p>
        </div>
        <div class="problem-card">
          <div class="problem-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l22 22M16.72 11.06A10.94 10.94 0 0 1 19 12.55M5 12.55a10.94 10.94 0 0 1 5.17-2.39M10.71 5.05A16 16 0 0 1 22.56 9M1.42 9a15.91 15.91 0 0 1 4.7-2.88"/></svg>
          </div>
          <h3>Telemetry & Telemarketing</h3>
          <p>
            Many automotive apps harvest your driving habits, mileage, and location to resell to insurance brokers. TorqueKeep makes zero outbound network requests.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- How It Works -->
  <section id="how-it-works">
    <div class="container">
      <div class="section-head">
        <h2>Three Steps to Permanent Vehicle Records</h2>
        <p>Built for speed and simplicity. Log maintenance in under 10 seconds.</p>
      </div>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-num">1</div>
          <h3>Park Your Vehicle</h3>
          <p>
            Add your daily driver, project truck, or classic motorcycle in seconds. Units switch seamlessly between Miles/Gallons and Kilometers/Litres.
          </p>
        </div>
        <div class="step-card">
          <div class="step-num">2</div>
          <h3>Log Service in 1-Tap</h3>
          <p>
            Select from dedicated automotive service categories: Oil, Brakes, Tires, Battery, Inspection. Record odometer, costs, and part numbers instantly.
          </p>
        </div>
        <div class="step-card">
          <div class="step-num">3</div>
          <h3>Hand Over the Dossier</h3>
          <p>
            When selling your car, generate a clean, watermarked Buyer Resale Dossier PDF directly on your device. Justify top-dollar asking price with proof.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Features Grid -->
  <section id="features" style="background: white; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
    <div class="container">
      <div class="section-head">
        <h2>Engineered for Demanding Vehicle Owners</h2>
        <p>Every feature solves a specific real-world owner frustration.</p>
      </div>
      <div class="features-grid">
        <div class="feat-card">
          <div class="feat-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div>
            <h3>100% Offline SQLite Architecture</h3>
            <p>All records live exclusively in an encrypted Room SQLite database on your device. Works deep inside metal shop bays and off-grid mountain trails.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2"/></svg>
          </div>
          <div>
            <h3>4-Corner Tire Tread Diagnostic</h3>
            <p>Visual chassis map tracks Front-Left, Front-Right, Rear-Left, and Rear-Right tread depth in 32nds of an inch. Alerts you before dangerous uneven wear strikes.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div>
            <h3>Buyer Resale Dossier Synthesis</h3>
            <p>Generate clean, high-resolution A4 PDFs with chronological service ledgers, cumulative investment totals, and verification stamps directly via Android canvas.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
          </div>
          <div>
            <h3>Zero Data Lock-in (CSV & JSON)</h3>
            <p>Your records belong to you forever. Export your entire vehicle maintenance history to universal CSV or JSON spreadsheets at any time with 1 tap.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Transparent Pricing -->
  <section id="pricing">
    <div class="container">
      <div class="section-head">
        <h2>Honest, Transparent Pricing</h2>
        <p>No bait-and-switch trials. No forced recurring credit card charges.</p>
      </div>
      <div class="pricing-table-wrap">
        <div class="pricing-grid">
          <!-- Free Tier -->
          <div class="pricing-col">
            <span class="pricing-badge" style="background: #E2E8F0; color: #334155;">Free Forever</span>
            <div class="plan-title">Garage Bay Free</div>
            <div class="plan-price">$0 <span>/ forever</span></div>
            <div class="plan-desc">Everything an individual car owner needs to track their primary daily driver for life.</div>
            <ul class="plan-features">
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> 1 Full Vehicle Bay</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Unlimited Service Logs</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Real-Time Fuel Economy & Tread Gauges</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> 1-Page Basic PDF Summary</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Universal CSV & JSON Data Export</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Zero Ads or Telemetry Trackers</li>
            </ul>
            <a href="preview.html" class="btn btn-secondary" style="width: 100%;" target="_blank">Start Free</a>
          </div>

          <!-- Pro Tier -->
          <div class="pricing-col pro">
            <span class="pricing-badge">Most Popular</span>
            <div class="plan-title">Multi-Bay Lifetime</div>
            <div class="plan-price">$19.99 <span>one-time</span></div>
            <div class="plan-desc">For households with multiple vehicles, DIY enthusiasts, and project car restorers.</div>
            <ul class="plan-features">
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> <strong>Unlimited Vehicle Bays</strong></li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Multi-Page A4 Resale Dossier with Watermarks</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Unlimited High-Res Receipt Attachments</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Automatic Google Drive Backup Sync</li>
              <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> <strong>Pay Once &bull; Own Forever</strong> (Or $2.99/mo flex)</li>
            </ul>
            <a href="preview.html" class="btn btn-primary" style="width: 100%;" target="_blank">Unlock Lifetime Pro</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section id="faq" style="background: white; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
    <div class="container">
      <div class="section-head">
        <h2>Frequently Asked Questions</h2>
        <p>Clear answers with zero corporate runaround.</p>
      </div>
      <div class="faq-grid">
        <div class="faq-item">
          <h4>Will my data disappear if the developer shuts down or stops updating?</h4>
          <p>
            No. TorqueKeep is built on a 100% offline-first architecture. All records are stored directly inside a local SQLite database on your phone. Even if our app was removed from the store, your installed copy continues functioning forever. You can also export your raw CSV/JSON records at any time.
          </p>
        </div>
        <div class="faq-item">
          <h4>Can I track classic cars or motorcycles without a 17-digit VIN?</h4>
          <p>
            Yes! Unlike legacy corporate apps that enforce rigid VIN decoding, the VIN field in TorqueKeep is 100% optional. You can park pre-1981 classic cars, vintage hot rods, custom track cars, trailers, and motorcycles without errors.
          </p>
        </div>
        <div class="faq-item">
          <h4>Does TorqueKeep drain battery in the background?</h4>
          <p>
            No. TorqueKeep has zero continuous background GPS polling or telemetry listeners. Reminders are handled by Android's native system alarm framework once daily, consuming 0.0% noticeable battery.
          </p>
        </div>
        <div class="faq-item">
          <h4>Can I import my records from other apps?</h4>
          <p>
            Yes. TorqueKeep includes a standard CSV importer that maps date, odometer, service category, notes, and costs so you can migrate from spreadsheets or legacy trackers in seconds.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Final CTA -->
  <div class="container">
    <div class="cta-banner">
      <h2>Take Ownership of Your Vehicle Records Today</h2>
      <p>
        Join thousands of drivers, mechanics, and car enthusiasts who keep their vehicle records offline, permanent, and subscription-free.
      </p>
      <div style="display: flex; justify-content: center; gap: 16px;">
        <a href="preview.html" class="btn btn-light" target="_blank">Launch App Preview</a>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container footer-inner">
      <div>
        <strong>TorqueKeep</strong> &mdash; Built with clean room engineering. Offline vehicle maintenance & resale dossiers.
      </div>
      <div class="footer-links">
        <a href="#pricing">Pricing</a>
        <a href="#faq">FAQ</a>
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
        <a href="support.html">Support</a>
        <a href="preview.html" target="_blank">App Prototype</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""

def main():
    root_path = r"d:\Project01\landing.html"
    brain_path = r"C:\Users\vinee\.gemini\antigravity\brain\380c6241-6d0c-483e-aa3e-4e5f725d6e16\landing.html"
    
    with open(root_path, "w", encoding="utf-8") as f:
        f.write(LANDING_HTML)
    print(f"[OK] Generated: {root_path} ({len(LANDING_HTML)} bytes)")

    with open(brain_path, "w", encoding="utf-8") as f:
        f.write(LANDING_HTML)
    print(f"[OK] Generated: {brain_path} ({len(LANDING_HTML)} bytes)")

if __name__ == "__main__":
    main()
