import sys
sys.dont_write_bytecode = True
import argparse
from pathlib import Path
from utils.makeFiles import write_file, create_structure
from utils.templates import INDEX_HTML, CSS_MAIN, CSS_THEME, CSS_FONTS, JS_MAIN

sys.path.append(str(Path(__file__).parent))

def main():
    p = argparse.ArgumentParser(description="Create a folder structure.")
    p.add_argument("target", nargs="?", default="quick-web", help="target folder")
    p.add_argument("--force", "-f", action="store_true", help="overwrite files")
    args = p.parse_args()
    target = Path(args.target).resolve()
    print(f"Target: {target}")
    assets_css, assets_js = create_structure(target)
    write_file(target / "index.html", INDEX_HTML, args.force)
    write_file(assets_css / "main.css", CSS_MAIN, args.force)
    write_file(assets_css / "colorscheme.css", CSS_THEME, args.force)
    write_file(assets_css / "fonts.css", CSS_FONTS, args.force)
    write_file(assets_js / "main.js", JS_MAIN, args.force)
    print("Done.")

if __name__ == "__main__":
    main()