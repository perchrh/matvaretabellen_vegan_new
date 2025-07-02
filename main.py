import logging

import vegan_foods
from vegan_foods.dominate_sorting import map_to_food_nutrient_matrix, sort_by_least_dominated, group_by_food_group
from vegan_foods.nutrient_scoring import sort_by_nutrient_score


def create_nutrients_summary(food):
    summary = dict()
    nutrients = food['constituents']
    selected_nutrients = {k: nutrients[k] for k in vegan_foods.target_nutrients()}  # filter the dict
    for key, nutrient_data in selected_nutrients.items():
        if 'quantity' in nutrient_data:
            quantity = nutrient_data['quantity']
            if float(quantity) > 0.0:
                name = nutrient_data['nutrientName']
                unit = nutrient_data['unit']
                summary[name] = f"{quantity} {unit}"
    return summary


if __name__ == "__main__":
    # Configure logging to display debug messages
    logger = logging.getLogger('vegan_foods')

    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients()

    status = ["considering", len(foods), "foods", "regarding", len(target_nutrients), "nutrients"]
    logger.info(" ".join(str(x) for x in status))

    # food matrix F
    F = map_to_food_nutrient_matrix(foods, target_nutrients)
    sorted_dominate_count = sort_by_least_dominated(foods, F)

    grouped = group_by_food_group(foods, sorted_dominate_count)
    top_n = 10
    for group in sorted(grouped.keys()):  # present groups in alphabetic order by id
        values = grouped[group]
        group_name = values[0]['foodGroupName']
        print("++", group_name, "++")
        number = 1
        for item in values[:top_n]:
            print(number, item['foodName'], create_nutrients_summary(item))
            number += 1

    # Print the non-dominated foods in order by nutrient points
    non_dominated_foods = sort_by_nutrient_score(foods, F, target_nutrients, sorted_dominate_count)
    print("\n--- Top foods, across all groups ---")
    number = 1
    for item in non_dominated_foods:
        print(number, item['foodName'], create_nutrients_summary(item))
        number += 1
