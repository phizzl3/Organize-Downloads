def get_unique_path(target_dir, file_path):
    """Generate a unique destination path for a file.

    If a file with the same name already exists in the target folder,
    this helper appends a numeric suffix to avoid overwriting existing files.
    """
    # Extract the base name and extension from the source file.
    name = file_path.stem
    suffix = file_path.suffix
    counter = 1
    new_path = target_dir / f"{name}{suffix}"
    
    while new_path.exists():
        new_path = target_dir / f"{name}_{counter}{suffix}"
        counter += 1
    return new_path