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

(out / "index.html").write_text(html)
(out / "styles.css").write_text(
    Path("backend/generator/styles.css").read_text()
)
(out / "app.js").write_text(
    Path("backend/generator/app.js").read_text()
)