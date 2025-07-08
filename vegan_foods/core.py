from typing import Dict, List, Any, Set

from vegan_foods.find_non_vegan_langual_codes import dynamically_determine_non_vegan_langual_codes
from vegan_foods.nutrients import nutrients_to_avoid, target_nutrients
from vegan_foods.parse import read_foods_json

non_vegan_nutrients = nutrients_to_avoid()
non_vegan_langual_codes = dynamically_determine_non_vegan_langual_codes()


def is_vegan(food: Dict[str, Any]) -> bool:
    food_group = food['foodGroupId']
    main_group = food_group.split(".")[0]
    if main_group in ["6", "12", "13"] or food_group in "9.5":
        # vegetables, fruits and berries are vegan, and plant-based drinks
        return True

    for key, data in food['constituents'].items():
        if key in non_vegan_nutrients:
            if data.get('quantity') not in (None, 0.0):
                return False  # more than zero of non-vegan nutrient

    langual_codes = set(food['langualCodes'])
    unwanted_langual_codes = langual_codes.intersection(non_vegan_langual_codes)
    no_non_vegan_langual_codes = len(unwanted_langual_codes) == 0

    return no_non_vegan_langual_codes


def is_uninteresting(food: Dict[str, Any]) -> bool:
    langual_codes = set(food.get('langualCodes', []))
    # Filter out some dried foods, to prefer the cooked/wet entries for the same
    is_dried_legumes = "A0831" in langual_codes and "J0116" in langual_codes and not "H0259" in langual_codes

    category = food.get('foodGroupId')
    main_category = category.split(".")[0] if category else None
    # ignore animal-only categories, spices, alcoholic beverages, fizzy drinks and energy drinks, pure oils,
    # coffee and tea, water
    uninteresting = (main_category in ["1", "2", "3", "4", "11", "16"] or
                     category in ["8.2", "8.3", "9.1", "9.3", "9.4", "9.6", "10.5", "10.11"])

    return is_dried_legumes or uninteresting


def find_relevant_vegan_foods() -> List[Dict[str, Any]]:
    foods = read_foods_json("foods.json", "food-groups.json", "nutrients.json")
    relevant_foods: List[Dict[str, Any]] = []

    for food in foods['foods']:
        if not is_vegan(food):
            continue

        if is_uninteresting(food):
            continue

        nutrient_ids: Set[str] = set(key for key, entry in food['constituents'].items() if entry.get("quantity"))
        target_nutrient_ids: Set[str] = set(target_nutrients())
        if target_nutrient_ids.intersection(nutrient_ids):
            relevant_foods.append(food)

    return relevant_foods
