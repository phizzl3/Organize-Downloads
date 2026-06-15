"""ASCII-art display helper for the Organize Downloads package.

This module provides a simple utility to print a decorative ASCII banner
including a version label. It is intentionally lightweight and import-safe
so other modules can import the helper without producing side effects.
"""


def display_art(version: str) -> None:
    """Print a decorative ASCII banner including the given version.

    Args:
        version: A short version string to display near the top of the banner.
    """

    # Compose the banner as a single f-string so the version can be
    # interpolated directly into the artwork without additional formatting.
    _art = f"""
     V{version}
     ██████╗ ██████╗  ██████╗  █████╗ ███╗   ██╗██╗███████╗███████╗               
    ██╔═══██╗██╔══██╗██╔════╝ ██╔══██╗████╗  ██║██║╚══███╔╝██╔════╝               
    ██║   ██║██████╔╝██║  ███╗███████║██╔██╗ ██║██║  ███╔╝ █████╗                 
    ██║   ██║██╔══██╗██║   ██║██╔══██║██║╚██╗██║██║ ███╔╝  ██╔══╝                 
    ╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║ ╚████║██║███████╗███████╗               
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝               
                                                                                
    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗
    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝
    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║███████╗
    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║╚════██║
    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████║
    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
                                                                         :phiZzL3
                                                                                """

    # Output the banner to stdout. Keep this function side-effect limited to printing.
    print(_art)



if __name__ == "__main__":
    # Display a sample banner when run directly for quick manual testing.
    display_art("Test Version")
                                                                       