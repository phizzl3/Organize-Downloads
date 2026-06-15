"""Configuration package exports for Organize Downloads.

This package exposes the application-level configuration values that are used by
other modules in the Organize Downloads application.

`DOWNLOADS_DIR` is the resolved path to the user's downloads folder.
`FILE_CATEGORIES` is the mapping of file extensions to destination folders.
"""

from .configuration import DOWNLOADS_DIR, FILE_CATEGORIES
