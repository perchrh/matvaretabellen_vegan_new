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
    else:
        raise Exception("unknown unit")


def map_to_compact_data_objects(foods, target_nutrients):
    # flatten the dictionary values
    target_nutrients_ids = set(itertools.chain.from_iterable(
        [ids] if isinstance(ids, str) else ids
        for ids in target_nutrients.values()
    ))
    # now map the food dicts into more compact representations, with a reference back to the full data object
    food_data = list()
    for food in foods:
        data_item = dict()
        data_item['id'] = food['foodId']
        data_item['name'] = food['foodName']
        data_item['nutrients'] = list()
        for nutrient in food['constituents']:
            if nutrient['nutrientId'] in target_nutrients_ids:
                quantity_raw = nutrient.get('quantity', 0.0)
                unit = nutrient.get('unit', 'g')
                quantity = float(quantity_in_mcg(quantity_raw, unit))

                nutrient_data = {'id': nutrient['nutrientId'],
                                 'quantity_µg': quantity,
                                 }
                data_item['nutrients'].append(nutrient_data)
        if len(data_item['nutrients']) == 0:
            logger.error(
                "No nutrients found for food '%s' (%s)",
                data_item['name'],
                data_item['id']
            )
        else:
            food_data.append(data_item)
    return food_data


if __name__ == "__main__":
    # Configure logging to display debug messages
    logger = logging.getLogger('vegan_foods')

    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients()

    status = ["considering", len(foods), "foods", "regarding", len(target_nutrients), "nutrients"]
    logger.info(" ".join(str(x) for x in status))

    food_data = map_to_compact_data_objects(foods, target_nutrients)

    logger.debug("food_data: %s", food_data)

    # Now define the optimization problem and data in pymoo to produce the pareto front
