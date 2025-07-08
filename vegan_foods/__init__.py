"""
Vegan Foods module for analyzing and processing food data from Matvaretabellen.
"""

from typing import List

from .core import find_relevant_vegan_foods
from .food import Food
from .nutrients import target_nutrients as target_nutrients


def food_list() -> List[Food]:
    """
    Get a list of relevant vegan foods.

    Returns:
        List[Food]: A list of Food objects representing relevant vegan foods
    """
    # Convert dictionaries to Food objects
    food_dicts = find_relevant_vegan_foods()
    return [Food.from_dict(food_dict) for food_dict in food_dicts]
