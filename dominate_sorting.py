from collections import OrderedDict
from typing import Dict, List, Tuple, Any, Callable, TypeVar

import numpy as np

from vegan_foods.utils import logger

T = TypeVar('T')
K = TypeVar('K')


def quantity_in_mcg(quantity_raw: float, unit: str) -> float:
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


def safe_get_quantity_row(food: Dict[str, Any], target_nutrients: List[str]) -> np.ndarray:
    quantity_row = np.zeros(len(target_nutrients))

    nutrient_map = food['constituents']
    # Fill the quantity row based on target nutrients, in order
    for i, target_nutrient in enumerate(target_nutrients):
        nutrient_data = nutrient_map[target_nutrient]
        quantity_raw = float(nutrient_data.get("quantity", 0.0))
        unit = nutrient_data.get("unit", "g")
        # We don't assume the same nutrient is always listed in the same unit, e.g. that calcium is always listed in 'mg'
        quantity = quantity_in_mcg(quantity_raw, unit)

        quantity_row[i] = quantity

    return quantity_row


def map_to_food_nutrient_matrix(foods: List[Dict[str, Any]], target_nutrients: List[str]) -> np.ndarray:
    # Pre-allocate numpy array
    food_matrix = np.zeros((len(foods), len(target_nutrients)))

    for food_row, food in enumerate(foods):
        food_matrix[food_row] = safe_get_quantity_row(food, target_nutrients)

    return food_matrix


def sort_by_least_dominated(foods: List[Dict[str, Any]], F: np.ndarray) -> List[Tuple[int, int]]:
    logger.debug("food_matrix created of shape %s", np.shape(F))

    def dominates(a: np.ndarray, b: np.ndarray) -> bool:
        # Candidate 'a' dominates 'b' if the below is true
        return np.all(a >= b) and np.any(a > b)

    # Inspired by pareto-front and non-dominant sorting, we do a kind of dominant sorting:
    # The food that is the least dominated is first in the sorting order.
    # If multiple foods have the same count of dominated by other foods ("dominate_count"), they come in arbitrary order,
    # i.e. all foods dominated by 1 other foods come before those dominated by 2, and
    # there is no secondary level of sorting within those with the same "dominate_count".
    dominate_count: Dict[int, int] = dict()
    for idx, food in enumerate(foods):
        count = sum(dominates(F[i], F[idx]) for i in range(len(F)) if i != idx)
        dominate_count[idx] = count
    return sorted(dominate_count.items(), key=lambda x: x[1])


def group_by_ordered(iterable: List[T], key_func: Callable[[T], K]) -> OrderedDict:
    grouped: OrderedDict = OrderedDict()
    for item in iterable:
        key = key_func(item)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped


def group_by_food_group(foods: List[Dict[str, Any]], sorted_dominate_count: List[Tuple[int, int]]) -> OrderedDict:
    sorted_foods: List[Dict[str, Any]] = list()
    for idx, count in sorted_dominate_count:
        sorted_foods.append(foods[idx])
    grouped = group_by_ordered(sorted_foods, key_func=lambda w: w['foodGroupId'])  # group by main food group
    return grouped
