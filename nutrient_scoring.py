from typing import Dict, List, Tuple

import numpy as np

from vegan_foods.food import Food


def sort_by_nutrient_score(foods: List[Food], F: np.ndarray, target_nutrients: List[str],
                           sorted_dominate_count: List[Tuple[int, int]]) -> List[Food]:
    toplists: Dict[str, List[Tuple[str, float]]] = dict()
    # now populate the lists from the food matrix
    for fidx, food in enumerate(foods):
        target_nutrient_values = F[fidx]  # array of normalized nutrient quantities per food
        for nidx, nutrient in enumerate(target_nutrients):
            if nutrient not in toplists:
                toplists[nutrient] = list()  # list of food ids and their value
            nutrient_value= float(target_nutrient_values[nidx])
            if nutrient_value > 0.0:
                toplists[nutrient].append((food.id, nutrient_value))

    toplisted_foods: Dict[str, List[str]] = dict()
    for n in target_nutrients:
        toplists[n].sort(key=lambda w: -w[1])  # sort by descending order of nutrient quantity
        toplist_positions = [e[0] for e in toplists[n]]  # foodId only
        toplisted_foods[n] = toplist_positions

    def food_score(food: Food) -> float:
        nutrient_score = 0.0
        for n in target_nutrients:
            try:
                position = toplisted_foods[n].index(food.id)  # rank among foods having this nutrient
                nutrient_score += position / len(toplist_positions)  # normalized to 0..1
            except ValueError:
                nutrient_score += 1.1  # a small penalty above 1.0 for this nutrient
        return nutrient_score

    non_dominated_foods = [foods[f[0]] for f in sorted_dominate_count if f[1] == 0]
    non_dominated_foods.sort(key=food_score)
    return non_dominated_foods
