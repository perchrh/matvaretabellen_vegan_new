import json

from vegan_foods.utils import get_data_file_path


def read_foods_json(foods: str, groups: str) -> dict \
        :
    """
    Read and parse the foods.json file

    Args:
        s:
        file_path (str): Path to the foods.json file

    Returns:
        dict: Parsed JSON data
    """
    # Get the absolute path to the data file
    abs_file_path = get_data_file_path(foods)
    with open(abs_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    abs_group_file_path = get_data_file_path(groups)
    with open(abs_group_file_path, 'r', encoding='utf-8') as file:
        group_data = json.load(file)

    group_id_to_name = dict()
    for group in group_data['foodGroups']:
        group_id = group['foodGroupId']
        group_name = group['name']
        group_id_to_name[group_id] = group_name
    for food in data['foods']:
        group_id = food['foodGroupId']
        group_name = group_id_to_name[group_id]
        food['foodGroupName'] = group_name

    return data
