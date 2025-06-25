from .find_non_vegan_langual_codes import dynamically_determine_non_vegan_langual_codes
from .find_nutrients import nutrients_to_avoid, target_nutrients
from .parse import read_foods_json

vegan_food_groups = {
    "Korn- og bakevarer": "5",
    "Grønnsaker": "6",
    "Drikke": "9",
    "Belgvekster": "12",
    "Frukt og bær": "13",
    "Nøtter og frø": "14",
    "Poteter": "15",
    "Urter og krydder": "16",
    "Spisefett": "8",  # potentially
    "Diverse matvarer og retter": "10",  # potentially
    "Spedbarnsmat": "11",  # potentially
}.values()

non_vegan_ingredients = nutrients_to_avoid.values()
non_vegan_langual_codes = dynamically_determine_non_vegan_langual_codes()


def is_vegan(food):
    group_id = food.get('foodGroupId')
    primary_group_id = group_id.split('.')[0]
    if primary_group_id in vegan_food_groups:
        for c in food.get('constituents', []):
            if c in non_vegan_ingredients:
                if c.get('quantity') not in (None, 0.0):
                    return False  # more than allowed of illegal ingredient

        langual_codes = set(food.get('langualCodes', []))
        unwanted_langual_codes = langual_codes.intersection(non_vegan_langual_codes)
        no_non_vegan_langual_codes = len(unwanted_langual_codes) == 0

        return no_non_vegan_langual_codes
    else:
        return False


def find_relevant_vegan_foods():
    foods = read_foods_json()
    target_nutrient_ids = set(target_nutrients().values())
    relevant_foods = []

    for food in foods['foods']:
        if not is_vegan(food):
            continue
        nutrient_ids = set(x["nutrientId"] for x in food.get('constituents', []) if x.get("quantity"))
        if target_nutrient_ids.intersection(nutrient_ids):
            relevant_foods.append(food)

    return relevant_foods
