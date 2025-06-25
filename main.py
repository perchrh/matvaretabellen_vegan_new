import itertools
import logging

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
                unit = nutrient.get('unit', 'g')
                quantity = float(quantity_in_mcg(quantity_raw, unit))

                data_object[nutrient_id] = quantity

            food_data.append(data_object)
    return food_data


if __name__ == "__main__":
    # Configure logging to display debug messages
    logger = logging.getLogger('vegan_foods')

    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients()

    status = ["considering", len(foods), "foods", "regarding", len(target_nutrients), "nutrients"]
    logger.info(" ".join(str(x) for x in status))

    # flatten the dictionary values
    target_nutrients_ids = set(itertools.chain.from_iterable(
        [ids] if isinstance(ids, str) else ids
        for ids in target_nutrients.values()
    ))
    food_data = map_to_compact_data_objects(foods, target_nutrients_ids)

    logger.debug("food_data: %s", food_data)
