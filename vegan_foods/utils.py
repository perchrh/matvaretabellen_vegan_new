"""
Utility functions for the vegan_foods module.
"""

import logging
import os

# Configure logger
logger = logging.getLogger('vegan_foods')


def get_data_file_path(file_name):
    """
    Get the absolute path to a data file.

    Args:
        file_name (str): Name of the data file

    Returns:
        str: Absolute path to the data file
    """
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, file_name)
