import json

from vegan_foods.utils import get_data_file_path


def read_foods_json(foods: str, groups: str, nutrients: str) -> dict:
    """
    Read and parse the api files
    Returns:
        dict: Parsed JSON data, not filtered
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
        # enrich with food group name
        group_id = food['foodGroupId']
        group_name = group_id_to_name[group_id]
        food['foodGroupName'] = group_name

        # enrich nutrient data
        valid_nutrients_dict = dict()
        for constituent in food['constituents']:
            nutrient_id = constituent['nutrientId']
            nutrient_detail = get_nutrient_detail(nutrient_id)
            if nutrient_detail:
                nutrient = nutrient_detail[0]
                constituent['nutrientName'] = nutrient['name']
                eurofir_id = nutrient['euroFirId']
                constituent['euroFirId'] = eurofir_id
                valid_nutrients_dict[eurofir_id] = constituent
            else:
                # We ignore nutrients with an unrecognized nutrient_id. They are considered data set errors
                invalid_nutrient_ids.add(nutrient_id)

        food['constituents'] = valid_nutrients_dict

    if invalid_nutrient_ids:
        print(len(invalid_nutrient_ids),
              "undefined nutrient_id values were ignored (not present in nutrients.json):", invalid_nutrient_ids)

    return data
