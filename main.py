import logging
from typing import Dict, List, Tuple

import numpy as np

import vegan_foods
from dominate_sorting import map_to_food_nutrient_matrix, sort_by_least_dominated, group_by_food_group
from nutrient_scoring import sort_by_nutrient_score
from vegan_foods.food import Food


def create_nutrients_summary(food: Food) -> Dict[str, str]:
    summary = dict()
    selected_nutrients = {k: food.nutrients[k] for k in vegan_foods.target_nutrients()}  # filter the dict
    for key, nutrient_data in selected_nutrients.items():
        if nutrient_data.quantity > 0.0:
            name = nutrient_data.name
            unit = nutrient_data.unit
            summary[name] = f"{nutrient_data.quantity} {unit}"

    return summary


def print_top_by_food_group(foods: List[Food], sorted_dominate_count: List[Tuple[int, int]]) -> None:
    # sort foods in each food group by how many other foods dominate them
    grouped = group_by_food_group(foods, sorted_dominate_count)

    top_n = 10
    for group in sorted(grouped.keys()):  # present groups in alphabetic order by id
        values = grouped[group]
        first_food = values[0]
        group_name = first_food.group_name

        print("++", group_name, "++")
        number = 1
        for item in values[:top_n]:
            print(number, item.name, create_nutrients_summary(item))
            number += 1


def print_global_top_foods(foods: List[Food], F: np.ndarray, target_nutrients: List[str],
                           sorted_dominate_count: List[Tuple[int, int]]) -> None:
    # Print the non-dominated foods in order by nutrient points
    non_dominated_foods = sort_by_nutrient_score(foods, F, target_nutrients, sorted_dominate_count)
    print("\n--- Top foods, across all groups ---")
    number = 1
    for item in non_dominated_foods:
        print(number, item.name, create_nutrients_summary(item))
        number += 1


if __name__ == "__main__":
    # Configure logging to display debug messages
    logger = logging.getLogger('vegan_foods')

    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients()

    logger.info(f"Searching among {len(foods)} foods regarding {len(target_nutrients)} nutrients...")

    F = map_to_food_nutrient_matrix(foods, target_nutrients)
    sorted_dominate_count = sort_by_least_dominated(foods, F)

    print_top_by_food_group(foods, sorted_dominate_count)

    print_global_top_foods(foods, F, target_nutrients, sorted_dominate_count)
