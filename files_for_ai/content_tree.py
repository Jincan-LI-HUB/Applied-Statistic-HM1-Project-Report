"""
📁 Content Tree Generator
Visualizes a directory structure up to N layers deep.
Author: Generated for UFUG 2104 Applied Statistics / HW1 Project Report
"""

import os

# ── Configuration ──────────────────────────────────────────────────────────────
ROOT_DIR = r"E:/canfiles/Common courses study/大学通识/25-26 Spring/UFUG 2104 Applied statistics/HW1_project_report"
MAX_DEPTH = 3          # Number of layers to display
SHOW_HIDDEN = False    # Toggle hidden files/folders (starting with '.')
# ───────────────────────────────────────────────────────────────────────────────

# Emoji mapping by file extension
EXT_EMOJI = {
    ".py":    "🐍", ".ipynb": "📓", ".r": "📊", ".rmd": "📊",
    ".csv":   "📋", ".xlsx": "📊",  ".xls": "📊",
    ".pdf":   "📄", ".docx": "📝",  ".doc": "📝",
    ".png":   "🖼️",  ".jpg": "🖼️",   ".jpeg": "🖼️", ".svg": "🎨",
    ".mp4":   "🎬", ".mp3": "🎵",
    ".txt":   "📃", ".md":  "📖",   ".json": "🔧", ".yaml": "🔧",
    ".html":  "🌐", ".css": "🎨",   ".js": "⚡",
    ".zip":   "🗜️",  ".rar": "🗜️",
}

def get_emoji(name: str, is_dir: bool) -> str:
    if is_dir:
        return "📁"
    ext = os.path.splitext(name)[1].lower()
    return EXT_EMOJI.get(ext, "📄")

def build_tree(path: str, depth: int, max_depth: int, prefix: str = "") -> None:
    if depth > max_depth:
        return

    try:
        entries = sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower()))
    except PermissionError:
        print(f"{prefix}⛔ [Permission Denied]")
        return

    # Filter hidden if needed
    if not SHOW_HIDDEN:
        entries = [e for e in entries if not e.name.startswith(".")]

    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        emoji = get_emoji(entry.name, entry.is_dir())
        print(f"{prefix}{connector}{emoji} {entry.name}")

        if entry.is_dir():
            build_tree(entry.path, depth + 1, max_depth, prefix + extension)

def main():
    print()
    print("=" * 60)
    print(f"  🗂️  Content Tree  (max depth: {MAX_DEPTH} layers)")
    print(f"  📍 Root: {ROOT_DIR}")
    print("=" * 60)

    if not os.path.exists(ROOT_DIR):
        print(f"\n  ❌ Path not found: {ROOT_DIR}")
        print("  💡 Please update ROOT_DIR in the Configuration block.\n")
        return

    root_name = os.path.basename(ROOT_DIR) or ROOT_DIR
    print(f"\n📁 {root_name}")
    build_tree(ROOT_DIR, depth=1, max_depth=MAX_DEPTH)

    # Summary statistics
    total_files = total_dirs = 0
    for _, dirs, files in os.walk(ROOT_DIR):
        total_dirs  += len(dirs)
        total_files += len(files)

    print()
    print("─" * 60)
    print(f"  📊 Summary │ 📁 {total_dirs} folders   📄 {total_files} files")
    print("─" * 60)
    print()

if __name__ == "__main__":
    main()
