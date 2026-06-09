"""Configuration helpers for the Organize Downloads application.

This module stores the default file-category mappings and the path to the
user configuration file used to persist those categories between runs.
"""

from pathlib import Path
from .loadconfig import load_config

# Location of the JSON file that stores the user's custom file categories.
JSON = Path().home() / "PyAppFiles" / "Organize Downloads" / "file_categories.json"

# Default category groups and their associated file extensions.
DEFAULTS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".raw"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt", ".csv", ".pages", ".numbers",],
    "3D Printing & Design": [".stl", ".obj", ".3mf", ".step", ".stp", ".f3d", ".gcode"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar", ".dmg"],
    "Scripts & Code": [".py", ".sh", ".zsh", ".json", ".xml", ".html", ".css"],
    "Audio & Video": [".mp3", ".wav", ".mp4", ".mov", ".mkv", ".avi"],
    "Incomplete Downloads": [".crdownload", ".download", ".tmp"],
}

# Load the saved category mapping from disk, falling back to the defaults if needed.
FILE_CATEGORIES = load_config(json_path=JSON, default_data=DEFAULTS)
