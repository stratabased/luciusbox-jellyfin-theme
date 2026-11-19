"""Make dark-theme versions of the logo: the black "Lucius Box" wordmark turns
white, the icon and the gradient "3.0" stay as they are. The original already
has a transparent background. Writes assets/logo-dark.png, assets/icon.png and
the small WebP copies that build.py embeds in the CSS."""
from pathlib import Path
import numpy as np
from PIL import Image

root = Path(__file__).resolve().parent.parent
rgba = np.asarray(Image.open(root / "assets/logo-original.png").convert("RGBA")).astype(float)
rgb, a = rgba[..., :3], rgba[..., 3]
h, w = a.shape
a[a < 10] = 0  # stray near-invisible pixels
sat = rgb.max(axis=2) - rgb.min(axis=2)
text = np.zeros((h, w), bool)
text[:, int(w * 0.235):] = True          # right of the hexagon
neutral = text & (sat < 70) & (rgb.max(axis=2) < 140)
rgb[neutral] = [244, 244, 250]
img = Image.fromarray(np.dstack([rgb, a]).astype(np.uint8), "RGBA")
img = img.crop(img.getbbox())
img.save(root / "assets/logo-dark.png")
icon = img.crop((0, 0, int(img.width * 0.2), img.height))
icon = icon.crop(icon.getbbox())
icon.save(root / "assets/icon.png")

img.resize((900, round(img.height * 900 / img.width)), Image.LANCZOS).save(
    root / "assets/logo-embed.webp", quality=90, method=6)
icon.resize((256, round(icon.height * 256 / icon.width)), Image.LANCZOS).save(
    root / "assets/icon-embed.webp", quality=90, method=6)
print(img.size, icon.size)
