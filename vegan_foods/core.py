from vegan_foods.find_non_vegan_langual_codes import dynamically_determine_non_vegan_langual_codes
from vegan_foods.nutrients import nutrients_to_avoid, target_nutrients
from vegan_foods.parse import read_foods_json

non_vegan_nutrients = nutrients_to_avoid()
non_vegan_langual_codes = dynamically_determine_non_vegan_langual_codes()


def is_vegan(food):
    for c in food.get('constituents', []):
        if c['euroFirId'] in non_vegan_nutrients:
            if c.get('quantity') not in (None, 0.0):
                return False  # more than allowed of illegal ingredient

    langual_codes = set(food.get('langualCodes', []))
    unwanted_langual_codes = langual_codes.intersection(non_vegan_langual_codes)
    no_non_vegan_langual_codes = len(unwanted_langual_codes) == 0

    return no_non_vegan_langual_codes


def find_relevant_vegan_foods():
    foods = read_foods_json("foods.json", "food-groups.json", "nutrients.json")
    relevant_foods = []

    for food in foods['foods']:
        if not is_vegan(food):
            continue
        langual_codes = set(food.get('langualCodes', []))
        # Filter out some dried foods, to prefer the cooked/wet entries for the same
        is_dried_legumes = "A0831" in langual_codes and "J0116" in langual_codes and not "H0259" in langual_codes
        if is_dried_legumes:
            continue

        nutrient_ids = set(x["euroFirId"] for x in food.get('constituents', []) if x.get("quantity"))
        target_nutrient_ids = set(target_nutrients())
        if target_nutrient_ids.intersection(nutrient_ids):
            relevant_foods.append(food)

    return relevant_foods
