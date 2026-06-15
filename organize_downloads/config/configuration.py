"""Configuration helpers for the Organize Downloads application.

This module stores the default file-category mappings and the path to the
user configuration file used to persist those categories between runs.
"""

from pathlib import Path
from .loadconfig import load_config

# Location of the JSON file that stores the user's custom file categories.
_SUPPORT_DIR = Path().home() / "PyAppFiles" / "Organize Downloads" / "file_categories.json"
_CATEGORIES_JSON = _SUPPORT_DIR / "file_categories.json"
_CONFIG_JSON = _SUPPORT_DIR / "config.json"

# Default category groups and their associated file extensions.
_DEFAULT_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff",
               ".raw", ".heic", ".webp", ".heif", ".avif", ".psd", ".ai",
               ".eps", ".hif"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt",
                  ".csv", ".pages", ".numbers",],
    "3D Printing & Design": [".stl", ".obj", ".3mf", ".step", ".stp", ".f3d",
                             ".gcode", ".gx", ".fpp"],
    "Archives & Installers": [".zip", ".tar", ".gz", ".7z", ".rar", ".dmg",
                              ".exe", ".msi", ".pkg"],
    "Scripts & Code": [".py", ".sh", ".zsh", ".json", ".xml", ".html", ".css"],
    "Audio & Video": [".mp3", ".wav", ".mp4", ".mov", ".mkv", ".avi", ".flac",
                      ".aac", ".ogg", ".mpeg", ".mpg", ".m4a", ".m4b", ".m4v",
                      ".hevc", ".h264", ".h265", ".av1"],
    "Books": [".epub", ".mobi", ".azw3"],
    "Incomplete Downloads": [".crdownload", ".download", ".tmp"],
}

# Load the saved category mapping from disk, falling back to the defaults if needed.
FILE_CATEGORIES = load_config(json_path=_CATEGORIES_JSON, default_data=_DEFAULT_CATEGORIES)
