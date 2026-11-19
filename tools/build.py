"""Build dist/luciusbox.css: the theme with the logos embedded, ready to paste
into Jellyfin (Dashboard → Branding → Custom CSS). Run: python tools/build.py"""
import base64
from pathlib import Path

root = Path(__file__).resolve().parent.parent


def data_uri(name: str) -> str:
    return "data:image/webp;base64," + base64.b64encode((root / "assets" / name).read_bytes()).decode()


css = (root / "src/luciusbox.css").read_text(encoding="utf-8")
css = css.replace('url("__LOGO__")', f'url("{data_uri("logo-embed.webp")}")').replace('url("__ICON__")', f'url("{data_uri("icon-embed.webp")}")')
out = root / "dist/luciusbox.css"
out.write_text(css, encoding="utf-8", newline="\n")
print(f"{out.relative_to(root)}: {len(css) / 1024:.0f} KB")
