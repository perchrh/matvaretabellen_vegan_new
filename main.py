import logging
from collections import OrderedDict

import numpy as np

import vegan_foods


def safe_get_quantity_row(food, target_nutrient_list: list):
    quantity_row = np.zeros(len(target_nutrient_list))

    # Create a mapping of nutrient IDs to quantities for this food
    nutrient_map = {}
    for nutrient in food['constituents']:
        nutrient_id = nutrient['nutrientId']
        nutrient_map[nutrient_id] = float(nutrient.get('quantity', 0.0))

    # Fill the quantity row based on target nutrients, in order
    for i, target_nutrient in enumerate(target_nutrient_list):
        quantity_row[i] = nutrient_map[target_nutrient]

    return quantity_row


def map_to_food_nutrient_matrix(foods: list, target_nutrients: list):
    # Pre-allocate numpy array
    food_matrix = np.zeros((len(foods), len(target_nutrients)))

    for food_row, food in enumerate(foods):
        quantity_row = safe_get_quantity_row(food, target_nutrients)
        food_matrix[food_row] = quantity_row

    return food_matrix


def create_nutrients_summary(food):
    summary = dict()
    for key, value in vegan_foods.target_nutrients().items():
        for nutrient in food['constituents']:
            if nutrient['nutrientId'] == value and 'quantity' in nutrient:
                quantity = nutrient['quantity']
                if float(quantity) > 0.0:
                    summary[key] = f"{quantity} {nutrient['unit']}"
    return summary

def sort_by_least_dominated(foods, target_nutrients):
    # food matrix F
    F = map_to_food_nutrient_matrix(foods, target_nutrients)

    logger.debug("food_matrix created of shape %s", np.shape(F))

    def dominates(a, b):
        return all(ai >= bi for ai, bi in zip(a, b)) and any(ai > bi for ai, bi in zip(a, b))

    # Inspired by pareto-front and non-dominant sorting, we do a kind of dominant sorting
    dominate_count = dict()
    for idx, food in enumerate(foods):
        count = sum(dominates(F[i], F[idx]) for i in range(len(F)) if i != idx)
        dominate_count[idx] = count
    return sorted(dominate_count.items(), key=lambda x: x[1])


def group_by_ordered(iterable, key_func):
    grouped = OrderedDict()
    for item in iterable:
        key = key_func(item)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped


if __name__ == "__main__":
    # Configure logging to display debug messages
    logger = logging.getLogger('vegan_foods')

    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients().values()

    status = ["considering", len(foods), "foods", "regarding", len(target_nutrients), "nutrients"]
    logger.info(" ".join(str(x) for x in status))

    sorted_dominate_count = sort_by_least_dominated(foods, target_nutrients)

    grouped = group_by_ordered(foods, key_func=lambda w: w['foodGroupName'].split(".")[0]) # group by main food group
    top_n = 10
    for group, values in grouped.items():
        print("++ Food group:", group, "++")
        number = 1
        for item in values[:top_n]:
            print(number, item['foodName'], create_nutrients_summary(item))
            number+=1

