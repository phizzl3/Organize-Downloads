"""Utilities for resolving unique file destinations.

This module provides a helper that computes a destination path for a file in a
target folder, ensuring existing files are not overwritten by appending a unique
numeric suffix when necessary.
"""


def get_unique_path(target_dir, file_path):
    """Return a safe destination path for a file in the target directory.

    Args:
        target_dir (Path): The directory where the file will be moved.
        file_path (Path): The original file path being moved.

    Returns:
        Path: A unique file path under `target_dir` that does not collide with an
        existing file.
    """
    # Use the original stem and suffix to preserve the file name and extension.
    name = file_path.stem
    suffix = file_path.suffix
    counter = 1
    new_path = target_dir / f"{name}{suffix}"

    # Increment the suffix until a non-existing path is found.
    while new_path.exists():
        new_path = target_dir / f"{name}_{counter}{suffix}"
        counter += 1

    return new_path
