"""Configuration helpers for the Organize Downloads application.

This module defines default file category mappings, resolves the location of
persistent JSON configuration files, loads saved user settings, and exposes the
values required by the rest of the application.

The configuration flow is:
1. Ensure the application config directory exists under the user's home folder.
2. Load or create `config.json` for runtime settings.
3. Load or create `file_categories.json` for extension-category mappings.
4. Determine the active downloads directory using the loaded settings.
"""

from pathlib import Path
from time import sleep
from .loadconfig import load_config

# Location of the application's persistent support directory under the user home.
_SUPPORT_DIR = Path().home() / "PyAppFiles" / "Organize Downloads"
_CATEGORIES_JSON = _SUPPORT_DIR / "file_categories.json"
_CONFIG_JSON = _SUPPORT_DIR / "config.json"


# Default runtime configuration values used when no user config exists yet.
_DEFAULT_CONFIG = {
    "comments": (
        "'default' means the app will use the system's default downloads folder.",
        "You can set this to a custom path if you want to use a different location for your downloads.",
        "Make sure to use a valid path format for your operating system.",
    ),
    "downloads folder location": "default",
}

# Default category groups and their associated file extensions.
_DEFAULT_CATEGORIES = {
    "comments": (
        "This is the default file category mapping.",
        "You can customize it by adding or removing categories and file extensions.",
        "Each category is a folder name, and its list is a list of file extensions that belong to that category.",
        "Make sure to include the dot (.) before each file extension, and to use lowercase for consistency.",
        "For example, '.jpg' is the extension for JPEG image files, and it belongs in the 'Images' category.",
        "Feel free to modify the categories and extensions to suit your needs!",
        "Maintain the same format when editing to prevent errors when loading the configuration.",
    ),
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".tiff",
        ".raw",
        ".heic",
        ".webp",
        ".heif",
        ".avif",
        ".psd",
        ".ai",
        ".eps",
        ".hif",
    ],
    "Documents": [
        ".pdf",
        ".docx",
        ".doc",
        ".xlsx",
        ".xls",
        ".pptx",
        ".txt",
        ".csv",
        ".pages",
        ".numbers",
    ],
    "3D Printing and Design": [
        ".stl",
        ".obj",
        ".3mf",
        ".step",
        ".stp",
        ".f3d",
        ".gcode",
        ".gx",
        ".fpp",
    ],
    "Archives and Installers": [
        ".zip",
        ".tar",
        ".gz",
        ".7z",
        ".rar",
        ".dmg",
        ".exe",
        ".msi",
        ".pkg",
    ],
    "Scripts and Code": [".py", ".sh", ".zsh", ".json", ".xml", ".html", ".css"],
    "Audio and Video": [
        ".mp3",
        ".wav",
        ".mp4",
        ".mov",
        ".mkv",
        ".avi",
        ".flac",
        ".aac",
        ".ogg",
        ".mpeg",
        ".mpg",
        ".m4a",
        ".m4b",
        ".m4v",
        ".hevc",
        ".h264",
        ".h265",
        ".av1",
    ],
    "Books": [".epub", ".mobi", ".azw3"],
    "Incomplete Downloads": [".crdownload", ".download", ".tmp"],
}


# Load the runtime configuration, creating config.json with defaults if needed.
_CONFIG = load_config(json_path=_CONFIG_JSON, default_data=_DEFAULT_CONFIG)

# Read the configured downloads folder location from the user config.
_downloads_path = _CONFIG.get("downloads folder location", "default")

# If the configured downloads path is invalid, fall back to the system default.
if _downloads_path != "default" and not Path(_downloads_path).exists():
    print(
        f"Warning: The configured downloads folder path '{_downloads_path}' does not exist. Reverting to default."
    )
    _downloads_path = "default"
    sleep(5)


# Resolve the active downloads folder path for the app to use.
if _downloads_path != "default":
    DOWNLOADS_DIR = Path(_downloads_path)
else:
    DOWNLOADS_DIR = Path.home() / "Downloads"


# Load the saved category mapping from disk, using defaults when no file exists.
FILE_CATEGORIES = load_config(
    json_path=_CATEGORIES_JSON, default_data=_DEFAULT_CATEGORIES
)

# Remove any documentation-only keys from the in-memory category mapping.
if "comments" in FILE_CATEGORIES:
    del FILE_CATEGORIES["comments"]
