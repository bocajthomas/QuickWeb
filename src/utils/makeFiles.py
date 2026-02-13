from pathlib import Path

def write_file(path: Path, content: str, force: bool):
    if path.exists() and not force:
        print(f"Skipping existing file: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote: {path}")

def create_structure(target: Path):
    assets_css = target / "assets" / "css"
    assets_js = target / "assets" / "js"

    for d in (target, assets_css, assets_js):
        d.mkdir(parents=True, exist_ok=True)
    
    return assets_css, assets_js