"""
create_play_screenshots.py - Generates 4 professional 1080x2400 Google Play Store Screenshots
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1080
HEIGHT = 2400

# Fonts helper
def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf"
    ]
    for fn in font_names:
        if os.path.exists(fn):
            return ImageFont.truetype(fn, size)
    return ImageFont.load_default()

# Colors
BG_TOP = (11, 17, 24)
BG_BOTTOM = (6, 9, 14)
EMERALD = (0, 210, 106)
EMERALD_BG = (12, 38, 25)
WHITE = (255, 255, 255)
LIGHT_GRAY = (205, 215, 225)
MUTED_GRAY = (130, 145, 165)
DARK_CARD = (18, 25, 36)
DARK_CARD_BORDER = (35, 48, 68)
PHONE_BORDER = (45, 60, 80)
PHONE_BEZEL = (15, 20, 28)

def draw_gradient(draw, width, height, top_color, bot_color):
    for y in range(height):
        ratio = y / height
        r = int(top_color[0] * (1 - ratio) + bot_color[0] * ratio)
        g = int(top_color[1] * (1 - ratio) + bot_color[1] * ratio)
        b = int(top_color[2] * (1 - ratio) + bot_color[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def create_base_canvas(tag_text, title_text, subtitle_text):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_TOP)
    draw = ImageDraw.Draw(im)
    draw_gradient(draw, WIDTH, HEIGHT, BG_TOP, BG_BOTTOM)
    
    # Subtle ambient glow
    glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([WIDTH // 2 - 400, 200, WIDTH // 2 + 400, 800], fill=(0, 210, 106, 30))
    glow = glow.filter(ImageFilter.GaussianBlur(100))
    im.paste(glow, (0, 0), glow)
    
    draw = ImageDraw.Draw(im)
    
    # Tag Pill
    tag_font = get_font(26, bold=True)
    bbox = draw.textbbox((0, 0), tag_text, font=tag_font)
    tw = bbox[2] - bbox[0]
    pill_w = tw + 40
    pill_h = 44
    pill_x = (WIDTH - pill_w) // 2
    pill_y = 70
    draw.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + pill_h], radius=22, fill=EMERALD_BG, outline=EMERALD, width=2)
    draw.text((pill_x + 20, pill_y + 8), tag_text, fill=EMERALD, font=tag_font)
    
    # Main Title
    title_font = get_font(60, bold=True)
    title_lines = title_text.split("\n")
    ty = 135
    for line in title_lines:
        tbbox = draw.textbbox((0, 0), line, font=title_font)
        lw = tbbox[2] - tbbox[0]
        draw.text(((WIDTH - lw) // 2, ty), line, fill=WHITE, font=title_font)
        ty += 70
        
    # Subtitle
    sub_font = get_font(30, bold=False)
    sub_bbox = draw.textbbox((0, 0), subtitle_text, font=sub_font)
    sw = sub_bbox[2] - sub_bbox[0]
    draw.text(((WIDTH - sw) // 2, ty + 10), subtitle_text, fill=MUTED_GRAY, font=sub_font)
    
    return im

def draw_phone_frame(canvas):
    draw = ImageDraw.Draw(canvas)
    # Phone frame rectangle
    px1, py1, px2, py2 = 70, 430, WIDTH - 70, HEIGHT + 100
    # Outer bezel shadow & border
    draw.rounded_rectangle([px1 - 8, py1 - 8, px2 + 8, py2 + 8], radius=52, fill=(10, 14, 20), outline=PHONE_BORDER, width=4)
    # Inner phone screen
    draw.rounded_rectangle([px1, py1, px2, py2], radius=46, fill=(12, 17, 24))
    
    # Phone Status Bar
    time_font = get_font(26, bold=True)
    draw.text((px1 + 45, py1 + 24), "9:41", fill=WHITE, font=time_font)
    
    # Battery & signals
    draw.text((px2 - 130, py1 + 24), "5G  100%", fill=LIGHT_GRAY, font=get_font(24, bold=True))
    
    # Phone dynamic island / punchhole
    draw.rounded_rectangle([(WIDTH // 2) - 80, py1 + 20, (WIDTH // 2) + 80, py1 + 50], radius=15, fill=(0, 0, 0))
    
    # App Bar
    app_bar_y = py1 + 75
    # Logo
    if os.path.exists("assets/noin_logo_256.png"):
        logo = Image.open("assets/noin_logo_256.png").resize((48, 48), Image.Resampling.LANCZOS)
        canvas.paste(logo, (px1 + 40, app_bar_y), logo)
    
    draw.text((px1 + 100, app_bar_y + 8), "NOIN", fill=WHITE, font=get_font(32, bold=True))
    draw.text((px1 + 195, app_bar_y + 12), "GARAGE", fill=EMERALD, font=get_font(22, bold=True))
    
    # Right action icon: Pro badge
    draw.rounded_rectangle([px2 - 170, app_bar_y + 6, px2 - 40, app_bar_y + 44], radius=19, fill=EMERALD_BG, outline=EMERALD, width=2)
    draw.text((px2 - 150, app_bar_y + 12), "OFFLINE", fill=EMERALD, font=get_font(20, bold=True))
    
    return px1, py1 + 145, px2, py2

# SCREENSHOT 1: Multi-Vehicle Garage Overview
def generate_screen_1():
    canvas = create_base_canvas(
        tag_text="100% LOCAL & PRIVATE",
        title_text="YOUR GARAGE, ORGANIZED\nIN ONE LOGBOOK",
        subtitle_text="Track maintenance, mileage & health across all your vehicles."
    )
    px1, content_y, px2, py2 = draw_phone_frame(canvas)
    draw = ImageDraw.Draw(canvas)
    
    # Vehicle selector tabs
    tabs = ["2024 Tacoma TRD", "2021 Civic Sport", "1974 Bronco"]
    tx = px1 + 35
    for i, t in enumerate(tabs):
        active = (i == 0)
        t_font = get_font(22, bold=active)
        tb = draw.textbbox((0, 0), t, font=t_font)
        tw = tb[2] - tb[0]
        bg = (25, 36, 50) if active else (16, 22, 30)
        fg = WHITE if active else MUTED_GRAY
        border = EMERALD if active else DARK_CARD_BORDER
        draw.rounded_rectangle([tx, content_y, tx + tw + 34, content_y + 46], radius=23, fill=bg, outline=border, width=2 if active else 1)
        draw.text((tx + 17, content_y + 11), t, fill=fg, font=t_font)
        tx += tw + 48
    
    card_y = content_y + 65
    
    # Hero Car Card with Real Image
    card_w = (px2 - px1) - 70
    card_h = 440
    card_x = px1 + 35
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=24, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=2)
    
    if os.path.exists("assets/opt_tacoma_trd.jpg"):
        car_img = Image.open("assets/opt_tacoma_trd.jpg")
        car_w = card_w - 20
        car_h = 260
        car_img = car_img.resize((car_w, car_h), Image.Resampling.LANCZOS)
        # Rounded mask for car image
        mask = Image.new("L", (car_w, car_h), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.rounded_rectangle([0, 0, car_w, car_h], radius=18, fill=255)
        canvas.paste(car_img, (card_x + 10, card_y + 10), mask)
        
    # Badges on image
    draw.rounded_rectangle([card_x + 25, card_y + 25, card_x + 180, card_y + 65], radius=20, fill=(0, 0, 0, 180))
    draw.text((card_x + 40, card_y + 32), "TRD OFF-ROAD", fill=EMERALD, font=get_font(18, bold=True))
    
    # Vehicle Title & Mileage info
    draw.text((card_x + 25, card_y + 285), "2024 Toyota Tacoma TRD", fill=WHITE, font=get_font(30, bold=True))
    draw.text((card_x + 25, card_y + 325), "VIN: 3TMCZ5AN9PM08241 • 3.5L V6 4WD", fill=MUTED_GRAY, font=get_font(20))
    
    # Quick metrics row inside card
    draw.line([(card_x + 25, card_y + 365), (card_x + card_w - 25, card_y + 365)], fill=DARK_CARD_BORDER, width=1)
    
    draw.text((card_x + 30, card_y + 380), "CURRENT ODOMETER", fill=MUTED_GRAY, font=get_font(17, bold=True))
    draw.text((card_x + 30, card_y + 402), "32,450 mi", fill=WHITE, font=get_font(26, bold=True))
    
    draw.text((card_x + 320, card_y + 380), "STATUS", fill=MUTED_GRAY, font=get_font(17, bold=True))
    draw.text((card_x + 320, card_y + 402), "Optimal / Up to Date", fill=EMERALD, font=get_font(24, bold=True))
    
    draw.text((card_x + 630, card_y + 380), "TOTAL INVESTED", fill=MUTED_GRAY, font=get_font(17, bold=True))
    draw.text((card_x + 630, card_y + 402), "$1,280.40", fill=WHITE, font=get_font(26, bold=True))
    
    # Maintenance Schedule Row
    sched_y = card_y + card_h + 25
    draw.text((card_x, sched_y), "UPCOMING MAINTENANCE", fill=WHITE, font=get_font(24, bold=True))
    
    # Alert Box 1: Oil Change
    b1_y = sched_y + 40
    b_h = 105
    draw.rounded_rectangle([card_x, b1_y, card_x + card_w, b1_y + b_h], radius=18, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=2)
    draw.rounded_rectangle([card_x + 18, b1_y + 20, card_x + 80, b1_y + 82], radius=14, fill=EMERALD_BG)
    draw.text((card_x + 35, b1_y + 30), "OIL", fill=EMERALD, font=get_font(20, bold=True))
    draw.text((card_x + 105, b1_y + 22), "Synthetic Engine Oil & Filter", fill=WHITE, font=get_font(24, bold=True))
    draw.text((card_x + 105, b1_y + 58), "Target: 35,000 mi  (2,550 miles remaining)", fill=MUTED_GRAY, font=get_font(20))
    draw.rounded_rectangle([card_x + card_w - 180, b1_y + 30, card_x + card_w - 20, b1_y + 75], radius=12, fill=(20, 35, 26))
    draw.text((card_x + card_w - 165, b1_y + 40), "ON TRACK", fill=EMERALD, font=get_font(18, bold=True))
    
    # Alert Box 2: Tire Rotation
    b2_y = b1_y + b_h + 18
    draw.rounded_rectangle([card_x, b2_y, card_x + card_w, b2_y + b_h], radius=18, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=2)
    draw.rounded_rectangle([card_x + 18, b2_y + 20, card_x + 80, b2_y + 82], radius=14, fill=(35, 30, 18))
    draw.text((card_x + 30, b2_y + 30), "TIRE", fill=(255, 185, 40), font=get_font(18, bold=True))
    draw.text((card_x + 105, b2_y + 22), "4-Tire Cross Rotation", fill=WHITE, font=get_font(24, bold=True))
    draw.text((card_x + 105, b2_y + 58), "Due: Dec 15, 2026 or 35,000 mi", fill=MUTED_GRAY, font=get_font(20))
    draw.rounded_rectangle([card_x + card_w - 180, b2_y + 30, card_x + card_w - 20, b2_y + 75], radius=12, fill=(40, 32, 16))
    draw.text((card_x + card_w - 165, b2_y + 40), "SCHEDULED", fill=(255, 185, 40), font=get_font(18, bold=True))
    
    # Recent Service Records header
    rec_y = b2_y + b_h + 25
    draw.text((card_x, rec_y), "RECENT SERVICE RECORDS", fill=WHITE, font=get_font(24, bold=True))
    
    # Item 1
    r1_y = rec_y + 40
    draw.rounded_rectangle([card_x, r1_y, card_x + card_w, r1_y + 90], radius=16, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=1)
    draw.text((card_x + 25, r1_y + 18), "Cabin & Engine Air Filter Replacement", fill=WHITE, font=get_font(22, bold=True))
    draw.text((card_x + 25, r1_y + 52), "30,120 mi • Oct 14, 2026 • OEM Denso", fill=MUTED_GRAY, font=get_font(18))
    draw.text((card_x + card_w - 120, r1_y + 30), "$48.50", fill=EMERALD, font=get_font(24, bold=True))
    
    # Bottom Nav Bar
    draw_bottom_nav(canvas, px1, px2, py2, active_idx=0)
    
    canvas.save("assets/screenshots/screenshot_1_garage.png", quality=95)
    print("Screenshot 1 generated.")

# SCREENSHOT 2: Fast One-Tap Logging
def generate_screen_2():
    canvas = create_base_canvas(
        tag_text="FAST & FRICTIONLESS",
        title_text="ONE-TAP SERVICE LOGS\nRECORD IN SECONDS",
        subtitle_text="Dedicated service tiles, smart cost calculations & instant photo receipts."
    )
    px1, content_y, px2, py2 = draw_phone_frame(canvas)
    draw = ImageDraw.Draw(canvas)
    
    card_w = (px2 - px1) - 70
    card_x = px1 + 35
    
    draw.text((card_x, content_y + 10), "QUICK SERVICE LOG", fill=WHITE, font=get_font(26, bold=True))
    draw.text((card_x, content_y + 45), "Select service category for 2024 Toyota Tacoma", fill=MUTED_GRAY, font=get_font(20))
    
    # 4 Quick Service Tiles
    grid_y = content_y + 90
    tile_w = (card_w - 20) // 2
    tile_h = 135
    
    tiles = [
        ("OIL & FILTER", "Full Synthetic", EMERALD, True),
        ("TIRE ROTATION", "4-Corner Check", MUTED_GRAY, False),
        ("BRAKE SERVICE", "Pads & Rotors", MUTED_GRAY, False),
        ("BATTERY & ELECT.", "12V Test & Clean", MUTED_GRAY, False)
    ]
    
    for i, (title, sub, col, sel) in enumerate(tiles):
        col_x = card_x + (i % 2) * (tile_w + 20)
        row_y = grid_y + (i // 2) * (tile_h + 18)
        border_col = EMERALD if sel else DARK_CARD_BORDER
        fill_col = (20, 32, 26) if sel else DARK_CARD
        draw.rounded_rectangle([col_x, row_y, col_x + tile_w, row_y + tile_h], radius=20, fill=fill_col, outline=border_col, width=3 if sel else 1)
        draw.text((col_x + 25, row_y + 30), title, fill=WHITE if sel else LIGHT_GRAY, font=get_font(24, bold=True))
        draw.text((col_x + 25, row_y + 70), sub, fill=EMERALD if sel else MUTED_GRAY, font=get_font(19))
    
    # Form Details Container
    form_y = grid_y + 2 * tile_h + 45
    form_h = 750
    draw.rounded_rectangle([card_x, form_y, card_x + card_w, form_y + form_h], radius=24, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=2)
    
    fields = [
        ("Service Title", "Synthetic Oil Change & Filter Replacement"),
        ("Odometer Milestone", "32,450 miles"),
        ("Date Performed", "November 07, 2026"),
        ("Total Cost ($ USD)", "$68.50"),
        ("Service Facility / Performed By", "DIY / Home Garage"),
        ("Parts Used & Notes", "Mobil 1 Advanced Fuel Economy 0W-20, Toyota 04152-YZZA1")
    ]
    
    fy = form_y + 25
    for label, val in fields:
        draw.text((card_x + 30, fy), label.upper(), fill=MUTED_GRAY, font=get_font(16, bold=True))
        input_y = fy + 26
        draw.rounded_rectangle([card_x + 30, input_y, card_x + card_w - 30, input_y + 58], radius=14, fill=(13, 19, 28), outline=(32, 45, 62), width=1)
        draw.text((card_x + 48, input_y + 14), val, fill=WHITE, font=get_font(22, bold=False))
        fy += 105
        
    # Big Green Save Button
    btn_y = form_y + form_h + 35
    draw.rounded_rectangle([card_x, btn_y, card_x + card_w, btn_y + 80], radius=20, fill=EMERALD)
    draw.text((card_x + (card_w // 2) - 170, btn_y + 22), "SAVE RECORD OFFLINE", fill=(6, 9, 14), font=get_font(26, bold=True))
    
    # Bottom Nav Bar
    draw_bottom_nav(canvas, px1, px2, py2, active_idx=1)
    
    canvas.save("assets/screenshots/screenshot_2_logging.png", quality=95)
    print("Screenshot 2 generated.")

# SCREENSHOT 3: 4-Corner Tire Wear Telemetry
def generate_screen_3():
    canvas = create_base_canvas(
        tag_text="INNOVATIVE TELEMETRY",
        title_text="4-CORNER TIRE WEAR\nDEPTH & ROTATION LIFE",
        subtitle_text="Precise 32nds tread monitoring, rotation alerts & tire lifespan tracking."
    )
    px1, content_y, px2, py2 = draw_phone_frame(canvas)
    draw = ImageDraw.Draw(canvas)
    
    card_w = (px2 - px1) - 70
    card_x = px1 + 35
    
    draw.text((card_x, content_y + 10), "TIRE DIAGNOSTICS & TREAD DEPTH", fill=WHITE, font=get_font(26, bold=True))
    draw.text((card_x, content_y + 45), "Goodyear Wrangler Territory AT (265/70R17)", fill=MUTED_GRAY, font=get_font(20))
    
    # Vehicle Chassis Box
    diag_y = content_y + 90
    diag_h = 580
    draw.rounded_rectangle([card_x, diag_y, card_x + card_w, diag_y + diag_h], radius=24, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=2)
    
    # Draw chassis center line & axle markers
    cx = card_x + card_w // 2
    draw.line([(cx, diag_y + 60), (cx, diag_y + diag_h - 60)], fill=(32, 45, 62), width=3)
    draw.line([(card_x + 120, diag_y + 140), (card_x + card_w - 120, diag_y + 140)], fill=(32, 45, 62), width=2)
    draw.line([(card_x + 120, diag_y + 440), (card_x + card_w - 120, diag_y + 440)], fill=(32, 45, 62), width=2)
    
    # Central vehicle icon / indicator
    draw.rounded_rectangle([cx - 70, diag_y + 240, cx + 70, diag_y + 340], radius=16, fill=(15, 22, 32), outline=EMERALD, width=2)
    draw.text((cx - 48, diag_y + 270), "FRONT", fill=MUTED_GRAY, font=get_font(18, bold=True))
    draw.text((cx - 45, diag_y + 295), "DRIVE", fill=EMERALD, font=get_font(20, bold=True))
    
    # 4 Tire Boxes: FL, FR, RL, RR
    tires = [
        ("FRONT LEFT", "8 / 32 in", "78% Optimal", card_x + 40, diag_y + 65, EMERALD),
        ("FRONT RIGHT", "8 / 32 in", "78% Optimal", card_x + card_w - 280, diag_y + 65, EMERALD),
        ("REAR LEFT", "7 / 32 in", "68% Good", card_x + 40, diag_y + 365, (255, 185, 40)),
        ("REAR RIGHT", "7 / 32 in", "68% Good", card_x + card_w - 280, diag_y + 365, (255, 185, 40))
    ]
    
    for pos, depth, status, tx, ty, col in tires:
        draw.rounded_rectangle([tx, ty, tx + 240, ty + 145], radius=18, fill=(12, 17, 24), outline=col, width=2)
        draw.text((tx + 20, ty + 18), pos, fill=MUTED_GRAY, font=get_font(16, bold=True))
        draw.text((tx + 20, ty + 46), depth, fill=WHITE, font=get_font(30, bold=True))
        draw.text((tx + 20, ty + 95), status, fill=col, font=get_font(20, bold=True))
        
    # Analysis & Rotation Box
    rec_y = diag_y + diag_h + 30
    draw.rounded_rectangle([card_x, rec_y, card_x + card_w, rec_y + 200], radius=22, fill=DARK_CARD, outline=DARK_CARD_BORDER, width=2)
    draw.text((card_x + 30, rec_y + 25), "ROTATION RECOMMENDATION", fill=WHITE, font=get_font(22, bold=True))
    draw.text((card_x + 30, rec_y + 65), "Front tread depth is wearing faster than rear axle.", fill=MUTED_GRAY, font=get_font(20))
    draw.text((card_x + 30, rec_y + 98), "Recommended: Perform standard Forward Cross rotation in 2,550 miles.", fill=LIGHT_GRAY, font=get_font(20))
    
    # Progress Bar of Lifetime
    draw.text((card_x + 30, rec_y + 145), "Estimated Remaining Tire Life: 32,000 miles", fill=EMERALD, font=get_font(19, bold=True))
    
    # Lifetime summary card
    hist_y = rec_y + 230
    draw.rounded_rectangle([card_x, hist_y, card_x + card_w, hist_y + 130], radius=20, fill=(16, 24, 34), outline=DARK_CARD_BORDER, width=1)
    draw.text((card_x + 30, hist_y + 25), "Set Installed: June 2024 at 12,000 mi", fill=WHITE, font=get_font(22, bold=True))
    draw.text((card_x + 30, hist_y + 65), "Total Miles on Current Set: 20,450 miles  •  DOT Code: 1424", fill=MUTED_GRAY, font=get_font(19))
    
    # Bottom Nav Bar
    draw_bottom_nav(canvas, px1, px2, py2, active_idx=2)
    
    canvas.save("assets/screenshots/screenshot_3_tire_wear.png", quality=95)
    print("Screenshot 3 generated.")

# SCREENSHOT 4: Buyer-Ready Resale Dossier
def generate_screen_4():
    canvas = create_base_canvas(
        tag_text="MAXIMIZE RESALE VALUE",
        title_text="BUYER-READY PDF\nRESALE DOSSIER",
        subtitle_text="Export certified chronological records to prove vehicle care."
    )
    px1, content_y, px2, py2 = draw_phone_frame(canvas)
    draw = ImageDraw.Draw(canvas)
    
    card_w = (px2 - px1) - 70
    card_x = px1 + 35
    
    draw.text((card_x, content_y + 10), "RESALE SERVICE DOSSIER", fill=WHITE, font=get_font(26, bold=True))
    draw.text((card_x, content_y + 45), "Export tamper-proof PDF maintenance document", fill=MUTED_GRAY, font=get_font(20))
    
    # Document Mockup (White/Silver Paper Card)
    doc_y = content_y + 90
    doc_h = 820
    draw.rounded_rectangle([card_x, doc_y, card_x + card_w, doc_y + doc_h], radius=24, fill=(245, 248, 252), outline=(180, 195, 215), width=2)
    
    # Document Header with Noin Seal
    draw.text((card_x + 35, doc_y + 35), "NOIN CERTIFIED SERVICE DOSSIER", fill=(15, 23, 42), font=get_font(26, bold=True))
    draw.text((card_x + 35, doc_y + 70), "Comprehensive Chronological Vehicle Maintenance Record", fill=(80, 100, 120), font=get_font(19))
    
    # Top divider
    draw.line([(card_x + 35, doc_y + 105), (card_x + card_w - 35, doc_y + 105)], fill=(210, 222, 236), width=2)
    
    # Vehicle overview in document
    draw.text((card_x + 35, doc_y + 125), "VEHICLE DETAILS", fill=(80, 100, 120), font=get_font(16, bold=True))
    draw.text((card_x + 35, doc_y + 150), "2024 TOYOTA TACOMA TRD OFF-ROAD", fill=(10, 15, 25), font=get_font(24, bold=True))
    draw.text((card_x + 35, doc_y + 185), "VIN: 3TMCZ5AN9PM08241  •  Mileage: 32,450 mi  •  Garage Bay #1", fill=(60, 80, 100), font=get_font(18))
    
    # Summary Metrics Pills
    mp_y = doc_y + 225
    metrics = [
        ("Total Records", "14 Verified"),
        ("Total Investment", "$1,280.40"),
        ("Open Recalls", "0 (Clear)")
    ]
    mw = (card_w - 90) // 3
    for i, (mtitle, mval) in enumerate(metrics):
        mx = card_x + 35 + i * (mw + 10)
        draw.rounded_rectangle([mx, mp_y, mx + mw, mp_y + 80], radius=14, fill=(232, 239, 248), outline=(200, 215, 232), width=1)
        draw.text((mx + 18, mp_y + 14), mtitle, fill=(90, 110, 130), font=get_font(16, bold=True))
        draw.text((mx + 18, mp_y + 40), mval, fill=(15, 23, 42), font=get_font(22, bold=True))
        
    # Table Header
    th_y = mp_y + 105
    draw.rounded_rectangle([card_x + 35, th_y, card_x + card_w - 35, th_y + 45], radius=10, fill=(225, 233, 245))
    draw.text((card_x + 50, th_y + 12), "MILEAGE", fill=(70, 85, 105), font=get_font(16, bold=True))
    draw.text((card_x + 190, th_y + 12), "SERVICE PERFORMED", fill=(70, 85, 105), font=get_font(16, bold=True))
    draw.text((card_x + card_w - 180, th_y + 12), "COST", fill=(70, 85, 105), font=get_font(16, bold=True))
    
    # Table Rows
    rows = [
        ("32,450 mi", "Synthetic Oil Change & Filter (Mobil 1)", "$68.50"),
        ("30,120 mi", "Engine & Cabin Air Filter Replacement", "$48.50"),
        ("27,200 mi", "4-Tire Rotation & High-Speed Balance", "$40.00"),
        ("22,500 mi", "Front Brake Inspection & Clean", "$35.00"),
        ("17,100 mi", "Differential Fluid Service (75W-90)", "$95.00"),
        ("12,000 mi", "New Tire Set: Goodyear Wrangler AT", "$850.00")
    ]
    
    ry = th_y + 55
    for mi, desc, cost in rows:
        draw.text((card_x + 50, ry + 10), mi, fill=(15, 23, 42), font=get_font(18, bold=True))
        draw.text((card_x + 190, ry + 10), desc, fill=(30, 45, 65), font=get_font(18))
        draw.text((card_x + card_w - 180, ry + 10), cost, fill=(16, 120, 60), font=get_font(18, bold=True))
        draw.line([(card_x + 35, ry + 42), (card_x + card_w - 35, ry + 42)], fill=(230, 238, 246), width=1)
        ry += 48
        
    # Certification Badge at bottom of paper
    draw.rounded_rectangle([card_x + 35, doc_y + doc_h - 85, card_x + card_w - 35, doc_y + doc_h - 25], radius=12, fill=(235, 248, 240), outline=(160, 220, 185), width=1)
    draw.text((card_x + 55, doc_y + doc_h - 62), "VERIFIED LOCAL ARCHIVE • Generated via Noin for Android", fill=(16, 130, 70), font=get_font(17, bold=True))
    
    # Export / Share PDF Button
    btn_y = doc_y + doc_h + 30
    draw.rounded_rectangle([card_x, btn_y, card_x + card_w, btn_y + 80], radius=20, fill=EMERALD)
    draw.text((card_x + (card_w // 2) - 145, btn_y + 22), "EXPORT RESALE PDF", fill=(6, 9, 14), font=get_font(26, bold=True))
    
    # Bottom Nav Bar
    draw_bottom_nav(canvas, px1, px2, py2, active_idx=3)
    
    canvas.save("assets/screenshots/screenshot_4_dossier.png", quality=95)
    print("Screenshot 4 generated.")

def draw_bottom_nav(canvas, px1, px2, py2, active_idx=0):
    draw = ImageDraw.Draw(canvas)
    nav_y = py2 - 110
    draw.rounded_rectangle([px1, nav_y, px2, py2], radius=0, fill=(10, 15, 22))
    draw.line([(px1, nav_y), (px2, nav_y)], fill=DARK_CARD_BORDER, width=2)
    
    nav_items = ["Garage", "Log Service", "Tire Wear", "Dossier", "Settings"]
    item_w = (px2 - px1) // 5
    for i, item in enumerate(nav_items):
        ix = px1 + i * item_w
        active = (i == active_idx)
        col = EMERALD if active else MUTED_GRAY
        # Indicator bar if active
        if active:
            draw.rounded_rectangle([ix + (item_w // 2) - 20, nav_y + 8, ix + (item_w // 2) + 20, nav_y + 12], radius=2, fill=EMERALD)
        draw.text((ix + (item_w // 2) - 30, nav_y + 35), item, fill=col, font=get_font(20, bold=active))

if __name__ == "__main__":
    generate_screen_1()
    generate_screen_2()
    generate_screen_3()
    generate_screen_4()
    print("All 4 Google Play screenshots generated successfully.")
