def organize_folder():
    """Scan the Downloads folder and move files into category directories."""
    # Confirm that the source directory exists before attempting to organize it.
    if not DOWNLOADS_DIR.exists():
        print(f"Error: Could not find the Downloads directory at {DOWNLOADS_DIR}")
        return

    # Announce the start of the organization process to the user.
    print(f"Scanning: {DOWNLOADS_DIR}...")
    moved_count = 0

    # Iterate through every item in the Downloads folder.
    for item in DOWNLOADS_DIR.iterdir():
        # Skip directories and hidden system files such as .DS_Store.
        if item.is_dir() or item.name.startswith('.'):
            continue

        # Normalize the file extension for category matching.
        file_extension = item.suffix.lower()
        
        # Determine the destination category for this file.
        destination_folder = None
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = DOWNLOADS_DIR / category
                break

        # Fall back to an "Other" folder for unlisted file types.
        if not destination_folder:
            destination_folder = DOWNLOADS_DIR / "Other"

        # Create the category folder if it does not exist yet.
        destination_folder.mkdir(exist_ok=True)

        # Move the file to its organized destination.
        final_destination = get_unique_path(destination_folder, item)
        try:
            shutil.move(str(item), str(final_destination))
            print(f"Moved: {item.name} -> {destination_folder.name}/")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {item.name}: {e}")

    # Report the number of files successfully organized.
    print(f"\n✨ Done! Organized {moved_count} files successfully.")

    # Pause so the user can review the summary before the console closes.
    input("Press Enter to exit...")