"""
Embedded Base64 Data URIs for Noin - Vehicle Maintainence App Imagery & Branding.
Domain: noin.in
Guarantees 100% reliable rendering across all sandboxed webviews, iframes, and local file schemes.
"""

import base64
import os

ASSETS_DIR = r"d:\Project01\assets"

def get_base64_data_uri(filename, mime_type=None):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("ascii")
    if not mime_type:
        mime_type = "image/png" if filename.lower().endswith(".png") else "image/jpeg"
    return f"data:{mime_type};base64,{b64}"

TACOMA_DATA_URI = get_base64_data_uri("opt_tacoma_trd.jpg")
BRONCO_DATA_URI = get_base64_data_uri("opt_classic_bronco.jpg")
CIVIC_DATA_URI = get_base64_data_uri("opt_civic_sport.jpg")
HERO_GARAGE_DATA_URI = get_base64_data_uri("opt_hero_garage.jpg")
NOIN_LOGO_DATA_URI = get_base64_data_uri("noin_logo_256.png")
NOIN_LOGO_MASTER_URI = get_base64_data_uri("noin_logo.png")

# Backwards compatibility aliases
MOTORA_LOGO_DATA_URI = NOIN_LOGO_DATA_URI
MOTORA_LOGO_MASTER_URI = NOIN_LOGO_MASTER_URI

if __name__ == "__main__":
    print(f"Tacoma URI length: {len(TACOMA_DATA_URI)}")
    print(f"Bronco URI length: {len(BRONCO_DATA_URI)}")
    print(f"Civic URI length: {len(CIVIC_DATA_URI)}")
    print(f"Hero Garage URI length: {len(HERO_GARAGE_DATA_URI)}")
    print(f"Noin Logo URI length: {len(NOIN_LOGO_DATA_URI)}")
