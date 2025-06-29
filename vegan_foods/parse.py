import json

from vegan_foods.utils import get_data_file_path


def read_foods_json(foods: str, groups: str, nutrients:str) -> dict \
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

    abs_nutrient_file_path = get_data_file_path(nutrients)
    with open(abs_nutrient_file_path, 'r', encoding='utf-8') as file:
        nutrients_data = json.load(file)

    nutrients = nutrients_data["nutrients"]
    group_id_to_name = dict()
    for group in group_data['foodGroups']:
        group_id = group['foodGroupId']
        group_name = group['name']
        group_id_to_name[group_id] = group_name
    for food in data['foods']:
        group_id = food['foodGroupId']
        group_name = group_id_to_name[group_id]
        food['foodGroupName'] = group_name
        for constituent in food['constituents']:
            nutrient_id = constituent['nutrientId']
            nutrient = [n for n in nutrients if n['nutrientId'] == nutrient_id][0]
            euro_fir_id = nutrient['euroFirId']
            name = nutrient['name']
            constituent['nutrientName'] = name
            constituent['euroFirId'] = euro_fir_id

    return data
