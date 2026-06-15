"""Download folder organization routines.

This module contains the primary routine used by the application to scan the
configured downloads directory, classify files by extension, and move them into
named category folders. It relies on a helper to ensure files are not overwritten
when duplicate names exist in the destination directory.
"""

import shutil
from modules import get_unique_path


def organize_folder(downloads_dir, file_categories):
    """Scan the Downloads folder and move files into category directories."""
    # Confirm that the source directory exists before attempting to organize it.
    if not downloads_dir.exists():
        print(f"Error: Could not find the Downloads directory at {downloads_dir}")
        return

    # Announce the start of the organization process to the user.
    print(f"Scanning: {downloads_dir}...")
    moved_count = 0

    # Iterate through every item in the Downloads folder.
    for item in downloads_dir.iterdir():
        # Skip directories and hidden system files such as .DS_Store.
        if item.is_dir() or item.name.startswith("."):
            continue

        # Normalize the file extension for category matching.
        file_extension = item.suffix.lower()

        # Determine the destination category for this file.
        destination_folder = None
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                destination_folder = downloads_dir / category
                break

        # Fall back to an "Other" folder for unlisted file types.
        if not destination_folder:
            destination_folder = downloads_dir / "Other"

        # Create the category folder if it does not exist yet.
        destination_folder.mkdir(exist_ok=True)

        # Choose a collision-free path for this file before moving it.
        final_destination = get_unique_path(destination_folder, item)
        try:
            shutil.move(str(item), str(final_destination))
            print(f"Moved: {item.name} -> {destination_folder.name}/")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {item.name}: {e}")

    # Report the number of files successfully organized.
    print(f"\n✨ Done! Organized {moved_count} files successfully.")

