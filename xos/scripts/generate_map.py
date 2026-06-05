#!/usr/bin/env python3
"""
Xos world-map generator.

Produces an equirectangular, hex-gridded world map in the style of the user's
reference image: tan continents with province borders, blue hex ocean, a full
graticule (150W..150E / 60N..60S / EQ), and the 20 founding capitals.

Geography follows the Xos design docs: a western continental group
(Aurelia / Kessara / Murunga) and an eastern, more fragmented group
(Voskar / Zhang-Lu / Itzalan), the lone southern continent Thulven, and the
island belt of the Sunder. Climate is assigned by latitude + continentality.

Run:  python3 scripts/generate_map.py
Out:  xos-world-map.png  (and a climate-tinted variant)
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1600, 800            # 2:1 equirectangular
MASTER_SEED = 6060          # ties the map to a reproducible world seed
TARGET_LAND = 0.33          # fraction of surface that is land (~Earth-like 1/3)

rng = np.random.default_rng(MASTER_SEED)

# ----------------------------------------------------------------------------- coords
def lonlat_to_xy(lon, lat):
    x = (lon + 180.0) / 360.0 * W
    y = (90.0 - lat) / 180.0 * H
    return x, y

# pixel-grid latitude (for climate) and longitude
yy, xx = np.mgrid[0:H, 0:W]
LAT = 90.0 - (yy / H) * 180.0
LON = (xx / W) * 360.0 - 180.0
ABSLAT = np.abs(LAT)

# ----------------------------------------------------------------------------- noise
def fractal_noise(base_cells, octaves, seed):
    """Smooth fractal value noise in [0,1] via upsampled random grids."""
    r = np.random.default_rng(seed)
    field = np.zeros((H, W), np.float32)
    amp, total = 1.0, 0.0
    cells = base_cells
    for o in range(octaves):
        cy = max(2, round(cells * H / W))
        g = r.random((cy, cells)).astype(np.float32)
        layer = np.asarray(
            Image.fromarray((g * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR),
            np.float32) / 255.0
        field += amp * layer
        total += amp
        amp *= 0.5
        cells *= 2
    return field / total

# ----------------------------------------------------------------------------- continents
# (lat, lon, lat_sigma, lon_sigma, amplitude) gaussian land "bumps"
BUMPS = [
    # --- Western group ---
    (52, -98, 15, 20, 1.05),   # Aurelia (temperate north)
    (60, -150, 13, 16, 0.85),  # Aurelia NW reach / islands
    (26, -86, 14, 19, 1.05),   # Kessara (subtropical)
    (-10, -80, 18, 19, 1.05),  # Murunga (equatorial)
    (16, -103, 16, 12, 0.6),   # western bridge
    (-2, -120, 12, 14, 0.55),  # far-western islands
    # --- Eastern group ---
    (53, 108, 15, 27, 1.05),   # Voskar (boreal north, broad)
    (29, 112, 13, 17, 1.0),    # Zhang-Lu (subtropical->temperate)
    (-13, 124, 13, 15, 0.9),   # Itzalan (tropical highland)
    (-6, 145, 14, 18, 0.55),   # eastern archipelago seed
    (40, 150, 12, 14, 0.6),    # eastern NE islands
    # --- Sunder island belt (between the groups) ---
    (1, 62, 9, 16, 0.5),
    # --- Thulven (southern continent) ---
    (-60, 22, 12, 30, 0.95),
    (-62, -22, 10, 20, 0.7),
]

base = np.zeros((H, W), np.float32)
for lat0, lon0, slat, slon, amp in BUMPS:
    # wrap longitude distance
    dlon = (LON - lon0 + 180) % 360 - 180
    base += amp * np.exp(-(((LAT - lat0) / slat) ** 2 + (dlon / slon) ** 2))

# polar ocean bias (keep the very poles watery / icy, not big land)
base *= np.clip(1.0 - (ABSLAT - 72) / 18, 0.15, 1.0)

# perturb coastlines + spawn islands
coast = fractal_noise(6, 5, MASTER_SEED + 1)
fine  = fractal_noise(16, 4, MASTER_SEED + 2)
field = base + 0.72 * (coast - 0.5) + 0.40 * (fine - 0.5)

# threshold at the percentile that yields a bit above TARGET (carving follows)
thr = np.percentile(field, 100 * (1 - (TARGET_LAND + 0.05)))
land = field > thr

# clean tiny single-pixel noise a touch
land_img = Image.fromarray((land * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(3))
land = np.asarray(land_img) > 127

# carve inland seas / great lakes into deep interiors (the reference's blue patches)
_lmA = np.asarray(Image.fromarray((land*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(12)),
                  np.float32) / 255.0
lake_noise = fractal_noise(9, 4, MASTER_SEED + 7)
deep_interior = land & (_lmA > 0.55)
if deep_interior.any():
    cut = np.percentile(lake_noise[deep_interior], 22)
    land &= ~(deep_interior & (lake_noise < cut))

print(f"land fraction = {land.mean():.3f}")

# ----------------------------------------------------------------------------- continentality
lm = Image.fromarray((land * 255).astype(np.uint8))
interior = np.asarray(lm.filter(ImageFilter.GaussianBlur(14)), np.float32) / 255.0  # ~1 deep inland
coastnear = np.asarray(lm.filter(ImageFilter.GaussianBlur(7)), np.float32) / 255.0   # ocean shallowness

# ----------------------------------------------------------------------------- climate colors
TAN = np.array([224, 208, 158], np.float32)
def blend(c):  # keep the reference's tan feel: 55% tan + 45% climate hue
    return 0.55 * TAN + 0.45 * np.array(c, np.float32)

C_ICE      = blend([236, 242, 245])
C_BOREAL   = blend([150, 172, 138])
C_TEMPER   = blend([150, 182, 112])
C_MEDCOAST = blend([186, 192, 110])
C_DESERT   = blend([232, 210, 150])
C_SAVANNA  = blend([196, 198, 120])
C_TROPICAL = blend([108, 166, 92])
C_HIGHLAND = blend([182, 170, 150])

land_rgb = np.zeros((H, W, 3), np.float32)
def paintsel(mask, color):
    land_rgb[mask] = color

a = ABSLAT
trop = a < 23
subt = (a >= 23) & (a < 35)
temp = (a >= 35) & (a < 55)
bore = (a >= 55) & (a < 70)
ice  = a >= 70

dry = interior > 0.78  # deep interior -> arid

paintsel(ice, C_ICE)
paintsel(bore, C_BOREAL)
paintsel(temp, C_TEMPER)
paintsel(subt & ~dry, C_MEDCOAST)
paintsel(subt & dry, C_DESERT)
paintsel(trop & ~dry, C_TROPICAL)
paintsel(trop & dry, C_SAVANNA)

# Itzalan highland spine (eastern tropical, west side) + Q'an plateau
itz = trop & (LON > 108) & (LON < 132) & (LAT < -3) & (LAT > -26) & (interior > 0.5)
paintsel(itz, C_HIGHLAND)

# ----------------------------------------------------------------------------- province borders (Voronoi over land)
land_idx = np.argwhere(land)
K = 78
seed_pts = land_idx[rng.choice(len(land_idx), K, replace=False)]
best = np.full((H, W), 1e18, np.float32)
who = np.full((H, W), -1, np.int32)
for i, (py, px) in enumerate(seed_pts):
    d = (yy - py) ** 2 + (xx - px) ** 2
    m = d < best
    best[m] = d[m]
    who[m] = i
border = np.zeros((H, W), bool)
for ax in (0, 1):
    border |= (who != np.roll(who, 1, ax)) | (who != np.roll(who, -1, ax))
border &= land

# ----------------------------------------------------------------------------- ocean + hex grid
shallow = np.array([156, 198, 214], np.float32)
deep    = np.array([74, 132, 164], np.float32)
ocean_noise = fractal_noise(10, 3, MASTER_SEED + 5)[..., None]
ocean_rgb = deep + (shallow - deep) * coastnear[..., None]
ocean_rgb += (ocean_noise - 0.5) * 16  # subtle depth mottle
ocean_rgb = np.clip(ocean_rgb, 0, 255)

# compose base raster
rgb = np.where(land[..., None], land_rgb, ocean_rgb).astype(np.uint8)
img = Image.fromarray(rgb)
draw = ImageDraw.Draw(img, "RGBA")

# hex grid (flat-top) painted only over ocean, like the reference
def hex_pts(cx, cy, r):
    return [(cx + r * math.cos(math.radians(60 * k)),
             cy + r * math.sin(math.radians(60 * k))) for k in range(6)]
R = 12
hx = 1.5 * R
hy = math.sqrt(3) * R
hexline = (120, 170, 190, 90)
col = 0
x = -R
while x < W + R:
    yoff = 0 if col % 2 == 0 else hy / 2
    y = -R + yoff
    while y < H + R:
        ix, iy = int(x), int(y)
        if 0 <= ix < W and 0 <= iy < H and not land[min(iy, H-1), min(ix, W-1)]:
            draw.line(hex_pts(x, y, R) + [hex_pts(x, y, R)[0]], fill=hexline, width=1)
        y += hy
        col_inner = 0
    x += hx
    col += 1

# coastlines (dark) + province borders (faint brown)
coast_mask = land ^ np.asarray(Image.fromarray((land*255).astype(np.uint8))
                               .filter(ImageFilter.MaxFilter(3))) .astype(bool)
ov = np.zeros((H, W, 4), np.uint8)
ov[border] = (96, 74, 52, 150)          # province borders
ov[coast_mask & land] = (40, 60, 70, 255)  # coastline
img.paste(Image.fromarray(ov), (0, 0), Image.fromarray(ov))

# ----------------------------------------------------------------------------- graticule + labels
def font(sz, bold=True):
    p = ("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold
         else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    return ImageFont.truetype(p, sz)

grat = (70, 90, 100, 130)
for lon in range(-150, 181, 30):
    x, _ = lonlat_to_xy(lon, 0)
    draw.line([(x, 0), (x, H)], fill=grat, width=1)
for lat in range(-60, 61, 30):
    _, y = lonlat_to_xy(0, lat)
    color = (170, 60, 50, 200) if lat == 0 else grat
    draw.line([(0, y), (W, y)], fill=color, width=2 if lat == 0 else 1)

fl = font(15)
def lonlabel(lon):
    if lon == 0: return "PM"
    return f"{abs(lon)}°{'E' if lon>0 else 'W'}"
for lon in range(-150, 151, 30):
    x, _ = lonlat_to_xy(lon, 0)
    t = lonlabel(lon)
    w = draw.textlength(t, font=fl)
    for yy0 in (6, H - 22):
        draw.text((x - w/2, yy0), t, fill=(30, 45, 55), font=fl)
for lat in range(-60, 61, 30):
    _, y = lonlat_to_xy(0, lat)
    t = "EQ" if lat == 0 else f"{abs(lat)}°{'N' if lat>0 else 'S'}"
    draw.text((6, y - 9), t, fill=(30, 45, 55), font=fl)
    w = draw.textlength(t, font=fl)
    draw.text((W - 6 - w, y - 9), t, fill=(30, 45, 55), font=fl)

# ----------------------------------------------------------------------------- continent names
def place_text(lon, lat, text, sz, col=(40, 30, 18), spacing=2, anchor="mm"):
    x, y = lonlat_to_xy(lon, lat)
    f = font(sz)
    draw.text((x, y), text, fill=col, font=f, anchor=anchor,
              stroke_width=2, stroke_fill=(245, 240, 225))

CONTS = [  # (lat, lon, name, size)
    (50, -95, "AURELIA", 30), (24, -86, "KESSARA", 26), (-12, -80, "MURUNGA", 28),
    (52, 110, "VOSKAR", 30), (29, 112, "ZHANG-LU", 26), (-13, 123, "ITZALAN", 26),
    (-60, 18, "THULVEN", 24),
]
for lat, lon, name, sz in CONTS:
    place_text(lon, lat, name, sz, spacing=3)
place_text(20, 50, "THE  AURAN  OCEAN", 18, col=(28, 70, 88))
place_text(5, 5, "THE  PELAGINE", 24, col=(20, 64, 86))
place_text(62, -4, "THE  SUNDER", 16, col=(20, 64, 86))
place_text(30, -68, "THE  VORTH  DEEP", 16, col=(20, 64, 86))

# ----------------------------------------------------------------------------- capitals (snap to nearest land)
def snap(lon, lat):
    x, y = lonlat_to_xy(lon, lat)
    py, px = int(y), int(x)
    if 0 <= py < H and 0 <= px < W and land[py, px]:
        return x, y
    d = (land_idx[:, 0] - py) ** 2 + (land_idx[:, 1] - px) ** 2
    py, px = land_idx[d.argmin()]
    return float(px), float(py)

def star(cx, cy, r, fill):
    pts = []
    for k in range(10):
        ang = math.radians(-90 + k * 36)
        rr = r if k % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=fill, outline=(70, 45, 5))

MAJ = [("Auria",48,-92),("Norvane",60,-100),("Kessar",25,-88),("Khorr",30,-70),
       ("Oba's Seat",-10,-82),("Skelgard",55,98),("Jin",29,110),("Altun",-14,120)]
MIN = [("Sundering",40,-78),("Sunspire",20,-95),("Sava",-18,-72),("Tooth Coast",-2,-66),
       ("Wolfsteppe",46,120),("Deep-Taiga",58,128),("Southmonsoon",18,118),
       ("Tian Wall",33,98),("Q'an",-20,118),("Ballcourt",-8,132),("Vorthshore",-58,30)]
WILD = [("Tide-Lords",2,64)]

lblf = font(13)
def cap_label(x, y, name):
    draw.text((x + 8, y - 7), name, fill=(35, 28, 16), font=lblf,
              stroke_width=2, stroke_fill=(247, 242, 228))

for name, lat, lon in MAJ:
    x, y = snap(lon, lat); star(x, y, 9, (232, 163, 23)); cap_label(x, y, name)
for name, lat, lon in MIN:
    x, y = snap(lon, lat)
    draw.ellipse([x-5, y-5, x+5, y+5], fill=(255, 255, 255), outline=(40, 40, 40))
    cap_label(x, y, name)
for name, lat, lon in WILD:
    x, y = snap(lon, lat)
    draw.polygon([(x, y-7), (x+7, y), (x, y+7), (x-7, y)], fill=(207, 59, 46), outline=(80, 15, 8))
    cap_label(x, y, name)

# ----------------------------------------------------------------------------- title + legend
draw.rectangle([W/2-235, 14, W/2+235, 70], fill=(250, 244, 228, 235), outline=(90, 70, 50))
draw.text((W/2, 30), "X O S", font=font(30), fill=(35, 23, 12), anchor="mm")
draw.text((W/2, 56), "The Known World at the Founding · 60 BC",
          font=font(14, False), fill=(70, 55, 35), anchor="mm")

img.save("xos-world-map.png")
print("wrote xos-world-map.png", img.size)
