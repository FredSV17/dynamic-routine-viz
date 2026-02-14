import json
from pathlib import Path

config = json.loads(Path("backend/config/wallpaper.json").read_text())
template = Path("backend/generator/template.html").read_text()

html = template.replace(
    "{{ CONFIG_JSON }}",
    json.dumps(config)
)

out = Path("output")
out.mkdir(exist_ok=True)

# Write the generated HTML to index.html
(out / "index.html").write_text(html)
# Copy styles.css
(out / "styles.css").write_text(
    Path("backend/generator/styles.css").read_text()
)
# Copy app.js
(out / "app.js").write_text(
    Path("backend/generator/app.js").read_text()
)
# Copy wallpapers
wallpapers = Path("backend/generator/wallpapers").glob("*")
# Create wallpapers directory in output
(out / "wallpapers").mkdir(exist_ok=True)
for wallpaper in wallpapers:
    (out / "wallpapers" / wallpaper.name).write_bytes(wallpaper.read_bytes())