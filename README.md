# Lucius Box 3.0: a Jellyfin theme

A dark, glassy Jellyfin theme built around the Lucius Box logo. It uses a
purple-to-cyan gradient, frosted header and drawer, rounded cards that lift on
hover, gradient buttons and progress bars, and the Outfit and Plus Jakarta
Sans fonts. The Jellyfin logo in the header, drawer and sign-in page is
replaced with Lucius Box.

It's built for **Jellyfin 12.x** in the Modern and Legacy layouts, on
desktop, mobile and TV. It recolours Jellyfin 12's `--jf-palette-*` theme
variables, so most of the app follows the palette automatically.

## Install

1. Open `dist/luciusbox.css` and copy all of it.
2. In Jellyfin, go to **Dashboard → Branding → Custom CSS**, paste it, and save.
3. Hard-refresh the browser (Ctrl+F5).

The logos are embedded in the file, so it needs no hosting. Custom CSS
applies to clients that use Jellyfin Web: the browser, the desktop app,
Android, and the web-based TV apps. It doesn't apply to native apps like
Swiftfin or Findroid.

To use it for one account instead of the whole server, paste it under
**Settings → Display → Custom CSS**.

## Change it

- **Colours, corners, fonts:** edit the first block of `src/luciusbox.css`.
  All the `--lb-*` variables are there.
- **Logo:** replace `assets/logo-original.png`, then run
  `python tools/logo.py`. It needs Pillow and NumPy. It turns the black
  wordmark white for the dark background and writes the small WebP copies.
- **Build:** run `python tools/build.py` to write `dist/luciusbox.css`.

## Files

| Path | What it is |
|---|---|
| `dist/luciusbox.css` | The file to paste into Jellyfin |
| `src/luciusbox.css` | The theme source |
| `assets/logo-original.png` | The logo as supplied |
| `assets/logo-dark.png`, `assets/icon.png` | Dark-background versions, full size |
| `assets/*-embed.webp` | Small copies that get embedded in the CSS |
| `tools/logo.py`, `tools/build.py` | Logo processing and build |
