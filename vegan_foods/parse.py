import json

from vegan_foods.utils import get_data_file_path


def read_foods_json(foods: str, groups: str, nutrients: str) -> dict \
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

    def get_nutrient_detail(nutrient_id):
        all_nutrients = nutrients_data["nutrients"]
        nutrient_data = [n for n in all_nutrients if n['nutrientId'] == nutrient_id]
        return nutrient_data

    group_id_to_name = dict()
    for group in group_data['foodGroups']:
        group_id = group['foodGroupId']
        group_name = group['name']
        group_id_to_name[group_id] = group_name

    invalid_nutrient_ids = set()
    for food in data['foods']:
        group_id = food['foodGroupId']
        group_name = group_id_to_name[group_id]
        food['foodGroupName'] = group_name
        valid_nutrients = list()
        for constituent in food['constituents']:
            nutrient_id = constituent['nutrientId']
            nutrient_detail = get_nutrient_detail(nutrient_id)
            if nutrient_detail:
                # enrich the food entry
                nutrient = nutrient_detail[0]
                constituent['nutrientName'] = nutrient['name']
                constituent['euroFirId'] = nutrient['euroFirId']
                valid_nutrients.append(constituent)
            else:
                invalid_nutrient_ids.add(nutrient_id)

        # We ignore nutrients with an unrecognized nutrient_id. they are considered data set errors
        food['constituents'] = valid_nutrients

    if invalid_nutrient_ids:
        print(len(invalid_nutrient_ids),
              "nutrient_id values were ignored because they are not defined in nutrients.json:", invalid_nutrient_ids)

    return data
