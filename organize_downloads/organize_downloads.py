import os
import shutil
from pathlib import Path

# Define the directory to organize (Tilde expands to your user profile)
DOWNLOADS_DIR = Path.home() / "Downloads"

# Map folder names to the file extensions they should hold
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".raw"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt", ".csv", ".pages", ".numbers"],
    "3D Printing & Design": [".stl", ".obj", ".3mf", ".step", ".stp", ".f3d", ".gcode"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar", ".dmg"],
    "Scripts & Code": [".py", ".sh", ".zsh", ".json", ".xml", ".html", ".css"],
    "Audio & Video": [".mp3", ".wav", ".mp4", ".mov", ".mkv", ".avi"],
}

# Extensions to safely ignore (active browser downloads)
IGNORE_EXTENSIONS = [".crdownload", ".download", ".tmp"]

def get_unique_path(target_dir, file_path):
    """Generates a unique filename if a file already exists in the destination."""
    name = file_path.stem
    suffix = file_path.suffix
    counter = 1
    new_path = target_dir / f"{name}{suffix}"
    
    while new_path.exists():
        new_path = target_dir / f"{name}_{counter}{suffix}"
        counter += 1
    return new_path

def organize_folder():
    if not DOWNLOADS_DIR.exists():
        print(f"Error: Could not find the Downloads directory at {DOWNLOADS_DIR}")
        return

    print(f"Scanning: {DOWNLOADS_DIR}...")
    moved_count = 0

    # Iterate through everything in the Downloads folder
    for item in DOWNLOADS_DIR.iterdir():
        # Skip directories and hidden system files (like .DS_Store)
        if item.is_dir() or item.name.startswith('.'):
            continue
            
        file_extension = item.suffix.lower()
        
        # Skip active, incomplete downloads
        if file_extension in IGNORE_EXTENSIONS:
            continue

        # Find the correct category for the file
        destination_folder = None
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = DOWNLOADS_DIR / category
                break
        
        # If the file type isn't explicitly listed, put it in "Other"
        if not destination_folder:
            destination_folder = DOWNLOADS_DIR / "Other"

        # Create the category folder if it doesn't exist yet
        destination_folder.mkdir(exist_ok=True)

        # Move the file safely
        final_destination = get_unique_path(destination_folder, item)
        try:
            shutil.move(str(item), str(final_destination))
            print(f"Moved: {item.name} -> {destination_folder.name}/")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {item.name}: {e}")

    print(f"\n✨ Done! Organized {moved_count} files successfully.")

if __name__ == "__main__":
    organize_folder()
    