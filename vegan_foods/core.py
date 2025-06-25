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
    "Spisefett": "8",  # potentially
    "Diverse matvarer og retter": "10",  # potentially
}.values()

non_vegan_nutrients = nutrients_to_avoid.values()
non_vegan_langual_codes = dynamically_determine_non_vegan_langual_codes()


def is_vegan(food):
    group_id = food.get('foodGroupId')
    primary_group_id = group_id.split('.')[0]
    if primary_group_id in vegan_food_groups:
        for c in food.get('constituents', []):
            if c['nutrientId'] in non_vegan_nutrients:
                if c.get('quantity') not in (None, 0.0):
                    return False  # more than allowed of illegal ingredient

        langual_codes = set(food.get('langualCodes', []))
        unwanted_langual_codes = langual_codes.intersection(non_vegan_langual_codes)
        no_non_vegan_langual_codes = len(unwanted_langual_codes) == 0

        # Filter out some dried foods, to prefer the cooked/wet entries for the same
        is_dried_legumes = "A0831" in langual_codes and "J0116" in langual_codes and not "H0259" in langual_codes

        return no_non_vegan_langual_codes and not is_dried_legumes
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
