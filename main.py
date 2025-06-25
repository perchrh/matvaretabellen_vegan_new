import logging

import numpy as np

import vegan_foods


def quantity_in_mcg(quantity_raw, unit):
    """Convert quantity to micrograms for standardization"""
    conversions = {
        'µg-RE': 1,
        'µg': 1,
        'mg': 1000,
        'g': 1000000,
    }
    return quantity_raw * conversions[unit]


def safe_get_quantity_row(food, target_nutrient_list):
    """Extract nutrient quantities for a single food item using numpy"""
    quantity_row = np.zeros(len(target_nutrient_list))

    # Create a mapping of nutrient IDs to quantities for this food
    nutrient_map = {}
    for nutrient in food['constituents']:
        nutrient_id = nutrient['nutrientId']
        if nutrient_id not in target_nutrient_list:
            continue
        quantity_raw = nutrient.get('quantity', 0.0)
        unit = nutrient.get('unit', 'µg')
        quantity = float(quantity_in_mcg(quantity_raw, unit))
        nutrient_map[nutrient_id] = quantity

    # Fill the quantity row based on target nutrients order
    for i, target_nutrient in enumerate(target_nutrient_list):
        quantity_row[i] = nutrient_map[target_nutrient]

    return quantity_row


def map_to_food_nutrient_matrix(foods: list, target_nutrients: list):
    """Create a numpy matrix of foods vs nutrients
    :param nutrients:
    """
    # Pre-allocate numpy array
    food_matrix = np.zeros((len(foods), len(target_nutrients)))

    for food_row, food in enumerate(foods):
        quantity_row = safe_get_quantity_row(food, target_nutrients)
        food_matrix[food_row] = quantity_row

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

    logger.debug("food_matrix created of shape %s", np.shape(food_matrix))
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
