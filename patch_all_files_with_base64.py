"""
Patches build_preview.py and build_complete_landing.py to inject self-contained Base64 Data URIs.
Guarantees 100% reliable image loading in sandboxed IDE artifact viewports, offline file:// schemes, and remote static hosts.
"""

import os
from embedded_assets import TACOMA_DATA_URI, BRONCO_DATA_URI, CIVIC_DATA_URI, HERO_GARAGE_DATA_URI

ROOT_DIR = r"d:\Project01"

# 1. Update build_preview.py
def patch_build_preview():
    path = os.path.join(ROOT_DIR, "build_preview.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add import
    import_target = "import os\nimport sys"
    import_replacement = "import os\nimport sys\nfrom embedded_assets import TACOMA_DATA_URI, BRONCO_DATA_URI, CIVIC_DATA_URI, HERO_GARAGE_DATA_URI"
    if "from embedded_assets import" not in content and import_target in content:
        content = content.replace(import_target, import_replacement)

    # In HTML_CONTENT, replace asset path references
    content = content.replace('image: "assets/tacoma_trd.jpg"', f'image: "{TACOMA_DATA_URI}"')
    content = content.replace('fallbackImage: "tacoma_trd.jpg"', f'fallbackImage: "{TACOMA_DATA_URI}"')
    content = content.replace('image: "assets/classic_bronco.jpg"', f'image: "{BRONCO_DATA_URI}"')
    content = content.replace('fallbackImage: "classic_bronco.jpg"', f'fallbackImage: "{BRONCO_DATA_URI}"')
    content = content.replace('image: "assets/civic_sport.jpg"', f'image: "{CIVIC_DATA_URI}"')
    content = content.replace('fallbackImage: "civic_sport.jpg"', f'fallbackImage: "{CIVIC_DATA_URI}"')
    content = content.replace('src="assets/tacoma_trd.jpg" onerror="this.src=\'tacoma_trd.jpg\'"', f'src="{TACOMA_DATA_URI}"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] build_preview.py patched with embedded base64 data URIs.")

# 2. Update build_complete_landing.py
def patch_build_landing():
    path = os.path.join(ROOT_DIR, "build_complete_landing.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add import
    import_target = "import os\nimport shutil"
    import_replacement = "import os\nimport shutil\nfrom embedded_assets import TACOMA_DATA_URI, BRONCO_DATA_URI, CIVIC_DATA_URI, HERO_GARAGE_DATA_URI"
    if "from embedded_assets import" not in content and import_target in content:
        content = content.replace(import_target, import_replacement)

    # Replace in landing generator
    content = content.replace('src="assets/tacoma_trd.jpg" onerror="this.src=\'tacoma_trd.jpg\'"', f'src="{TACOMA_DATA_URI}"')
    content = content.replace('src="assets/hero_garage.jpg" onerror="this.src=\'hero_garage.jpg\'"', f'src="{HERO_GARAGE_DATA_URI}"')
    content = content.replace('src="assets/civic_sport.jpg" onerror="this.src=\'civic_sport.jpg\'"', f'src="{CIVIC_DATA_URI}"')
    content = content.replace('src="assets/classic_bronco.jpg" onerror="this.src=\'classic_bronco.jpg\'"', f'src="{BRONCO_DATA_URI}"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] build_complete_landing.py patched with embedded base64 data URIs.")

if __name__ == "__main__":
    patch_build_preview()
    patch_build_landing()
