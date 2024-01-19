#! /usr/bin/python
"""A script to remove temporary files from a directory.

The designed use of this script is to periodically be ran by a cron job to remove temporary files
from a specified directory (TMP_DIRECTORY).
The script will recursively prune all files under TMP_DIRECTORY that haven't been ACCESSED within
the expiration period (DEFAULT_EXPIRATION or the expiration period for its parent directory).
You can either use the default expiration or nest the temporary files in time-based directories.

Example:
    temp/
    ├── monthly    # Files in this directory will expire after 31 days of not being accessed.
    │   ├── file1
    │   └── file2
    ├── weekly     # Files in this directory will expire after 7 days of not being accessed.
    │   ├── file1
    │   └── file2
"""
from pathlib import Path
from datetime import datetime

CHECK_TIME = datetime.now()
TMP_DIRECTORY = Path("temp")
DEFAULT_EXPIRATION = 1
TIME_DICT = {"weekly": 7, "monthly": 31, "quarterly": 123, "yearly": 365}


def is_expired(file, expire_period=DEFAULT_EXPIRATION):
    """
    Check if a file is expired based on its last accessed date.

    Args:
        file (Path): The path to the file.
        expire_period (int, optional): The expiration period in days. Defaults to DEFAULT_EXPIRATION.

    Returns:
        bool: True if the file is expired, False otherwise.
    """
    modified_date = datetime.fromtimestamp(file.stat().st_atime)
    file_age = CHECK_TIME - modified_date
    return file_age.days >= expire_period


def prune_directory(dir_path, parent_expiration_period=None):
    """
    Recursively prunes a directory by deleting expired files.

    Args:
        dir_path (Path): The path to the directory to be pruned.
        parent_expiration_period (int, optional): The expiration period in days for the parent directory.
            If not provided, the default expiration period will be used.

    Returns:
        None
    """
    if not parent_expiration_period:
        parent_expiration_period = DEFAULT_EXPIRATION
    # If the directory is a time-based directory, use the expiration period for that directory.
    # Otherwise, use the expiration period for the parent directory.
    expire_period = TIME_DICT.get(dir_path.name, parent_expiration_period)
    for child in dir_path.iterdir():
        if child.is_dir():
            prune_directory(child, expire_period)
        elif child.is_file() and is_expired(child, expire_period):
                child.unlink()


if __name__ == "__main__":
    if TMP_DIRECTORY.exists():
        prune_directory(TMP_DIRECTORY)
