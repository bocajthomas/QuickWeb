import sys
sys.dont_write_bytecode = True
import argparse
from pathlib import Path
from utils.makeFiles import write_file, create_structure
from utils.templates import INDEX_HTML, CSS_MAIN, CSS_THEME, CSS_FONTS, JS_MAIN
from utils.logo import LOGO

sys.path.append(str(Path(__file__).parent))

def main():
    print(LOGO)

    p = argparse.ArgumentParser(description="Create a folder structure.")
    p.add_argument("target", nargs="?", default="", help="target folder")
    p.add_argument("--force", "-f", action="store_true", help="overwrite files")
    args = p.parse_args()

    if not args.target:
        folder_input = input("Enter a project name: ").strip()
        args.target = folder_input if folder_input else "quick-web"

    target = Path(args.target).resolve()

    assets_css, assets_js = create_structure(target)
    write_file(target / "index.html", INDEX_HTML, args.force)
    write_file(assets_css / "main.css", CSS_MAIN, args.force)
    write_file(assets_css / "colorscheme.css", CSS_THEME, args.force)
    write_file(assets_css / "fonts.css", CSS_FONTS, args.force)
    write_file(assets_js / "main.js", JS_MAIN, args.force)
    
    print("\nProject created")

    if sys.stdin.isatty(): input("\nPress enter to exit...")

if __name__ == "__main__":
    main()