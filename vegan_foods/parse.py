import json

from .utils import get_data_file_path, logger


def read_foods_json(file_path='foods.json'):
    """
    Read and parse the foods.json file

    Args:
        file_path (str): Path to the foods.json file

    Returns:
        dict: Parsed JSON data
    """
    # Get the absolute path to the data file
    abs_file_path = get_data_file_path(file_path)
    with open(abs_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
