"""Organize Downloads entry point.

This module is the main script for the Organize Downloads application. It
loads the configured downloads directory and file category mappings, then
delegates all file-moving work to the `organize_folder` helper.

When run directly, this script performs the organization workflow. When
imported, it remains import-safe for testing.
"""

__version__ = "1.0.1"
"""Organize Downloads package version number."""

import platform
from modules import organize_folder, display_art, clear_screen  # Core folder organization routine.
from config import FILE_CATEGORIES, DOWNLOADS_DIR  # Loaded app configuration.

# Execute the organization workflow only when run as a script.
if __name__ == "__main__":
    clear_screen()
    display_art(version=__version__)  # Show the app banner and version info.
    organize_folder(downloads_dir=DOWNLOADS_DIR, file_categories=FILE_CATEGORIES)
    if platform.system() == "Windows":
        input("Press Enter to exit...")  # Keep the console open on Windows after completion.
