import itertools
import logging

import numpy as np

import vegan_foods


def quantity_in_mcg(quantity_raw, unit):
    if unit == 'g':
        return quantity_raw * 1000000.0
    elif unit == 'mg':
        return quantity_raw * 1000.0
    elif unit == 'µg':
        return quantity_raw
    elif unit == 'µg-RE':
        return quantity_raw
    else:
        raise Exception("unknown unit %s", unit)


"""
list of foods: 
{
    'id': str, 
    'name': str, 
    'nutrients': dict[str, float]
} 
"""


def map_to_compact_data_objects(foods, target_nutrients_ids):
    # now map the food dicts into more compact representations, with a reference back to the full data object
    food_data = list()
    for food in foods:
        data_object = dict()
        data_object['id'] = food['foodId']
        data_object['name'] = food['foodName']
        for nutrient in food['constituents']:
            nutrient_id = nutrient['nutrientId']
            if nutrient_id in target_nutrients_ids:
                quantity_raw = nutrient.get('quantity', 0.0)
                unit = nutrient.get('unit', 'µg')
                quantity = float(quantity_in_mcg(quantity_raw, unit))

                data_object[nutrient_id] = quantity

            food_data.append(data_object)
    return food_data


def safe_get_quantity_row(food, target_nutrients: list, ):
    quantity_row = list()
    for nutrient in food['constituents']:
        for target_nutrient in target_nutrients:  # keep the ordering from target_nutrients
            if nutrient['nutrientId'] == target_nutrient:
                quantity_raw = nutrient.get('quantity', 0.0)
                unit = nutrient.get('unit', 'µg')
                quantity = float(quantity_in_mcg(quantity_raw, unit))
                quantity_row.append(quantity)
    return quantity_row


def map_to_food_nutrient_matrix(foods: list, target_nutrients: list):
    food_matrix = list()
    for food_row, food in enumerate(foods):
        quantity_row = safe_get_quantity_row(food, target_nutrients)
        food_matrix.append(quantity_row)
    return food_matrix


if __name__ == "__main__":
    # Configure logging to display debug messages
    logger = logging.getLogger('vegan_foods')

    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients().values()

    status = ["considering", len(foods), "foods", "regarding", len(target_nutrients), "nutrients"]
    logger.info(" ".join(str(x) for x in status))

    food_matrix = map_to_food_nutrient_matrix(foods, target_nutrients)

    logger.debug("food_matrix: %s", food_matrix)

    # Present it as a multi-objective optimization problem.
    # Determine the pareto front

    # Convert this to a matrix of just the numbers, where the indicis go to a lookup-table
    # and each row is a food, with the row-id pointing to a food_id
    # and each column is a nutrient, with the column-id pointing to a nutrient_id
    # of nutrient_id
    # food_data = [
    #     {'id': '1', 'name': 'Apple', 'Vit A RE': 500.0, 'Zn': 2.0},
    #     {'id': '2', 'name': 'Beef', 'Vit A RE': 800.0, 'Zn': 5.0},
    #     {'id': '3', 'name': 'Carrot', 'Vit A RE': 1500.0, 'Zn': 1.0},
    #    more foods
    # ]
