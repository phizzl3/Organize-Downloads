# Organize Downloads

Organize Downloads is a Python utility that scans your Downloads folder and sorts files into category-based folders such as Images, Documents, Archives, Audio and Video, Scripts and Code, and more. It automates the repetitive work of moving downloaded files into sensible folders.

## Overview

The project currently consists of:

- a main package entry point that scans the user’s Downloads directory
- configuration logic that loads default category mappings and persists them in user-level JSON files
- helper modules that ensure files are moved safely without overwriting existing files
- a packaging-friendly structure for creating a standalone desktop executable

This tool is useful for anyone who wants a cleaner Downloads folder without manually sorting files every time.

## Features

- Scans the user’s Downloads directory automatically
- Matches file extensions to predefined category folders
- Falls back to an “Other” folder for unrecognized file types
- Avoids overwriting existing files by generating unique destination names
- Persists category settings in a user-level JSON configuration file

## Project Structure

```text
Organize-Downloads/
├── LICENSE
├── README.md
├── requirements.txt
├── icon/
│   └── files-and-folders.png
└── organize_downloads/
    ├── organize_downloads.py
    ├── config/
    │   ├── __init__.py
    │   ├── configuration.py
    │   └── loadconfig.py
    └── modules/
        ├── __init__.py
        ├── _get_unique_path.py
        └── _organize_folder.py
```

## How It Works

1. The script starts from the user’s Downloads folder.
2. It checks each file extension and compares it with the configured category map.
3. Files are moved into the corresponding folder (for example, PDFs into Documents, images into Images, archives into Archives).
4. If a file type is not in the category map, it is placed into an “Other” folder.
5. If the destination file already exists, a numbered suffix is added to keep the original file intact.

## Requirements

- Python 3.x
- PyInstaller (for building a standalone binary)

Install the packaging dependency with:

```bash
pip install -r requirements.txt
```

## Running the Script

From the project root, enter the application folder and run the script with Python:

```bash
cd organize_downloads
python organize_downloads.py
```

The program will scan your Downloads directory and move matching files into category folders.

## Configuration Behavior

The application stores its runtime settings and file-category mapping in the user profile area under:

```text
~/PyAppFiles/Organize Downloads/config.json
~/PyAppFiles/Organize Downloads/file_categories.json
```

If either file does not exist yet, the app creates it using the built-in default definitions from the configuration module.
'config.json' allows for a user-customizable Downloads folder location.
'file_categories.json' allows for user-customizable file sorting.

## Building a Standalone Executable

To create a single-file binary with PyInstaller, run the following command from the project root:

```bash
pyinstaller --onefile --name "Organize Downloads" --icon "icon/files-and-folders.png" organize_downloads/organize_downloads.py
```

This produces a standalone executable named “Organize Downloads” (or “Organize Downloads.exe” on Windows) in the dist/ directory.

### Icon File Location

The icon used for packaging is located here:

```text
icon/files-and-folders.png
```

If you prefer to build from inside the application folder instead, use the relative path to the same icon file:

```bash
pyinstaller --onefile --name "Organize Downloads" --icon ../icon/files-and-folders.png organize_downloads.py
```

## Notes

- The organizer is intentionally simple and focuses on file-extension-based sorting.
- The category rules are easy to extend if you want to add your own file groups.
- The generated executable will still rely on the user’s Downloads folder at runtime.

## License

This project is distributed under the MIT License. See the LICENSE file for details.
