"""
Vegan Foods module for analyzing and processing food data from Matvaretabellen.
"""

from .parse import read_foods_json, get_food_by_name, get_foods_by_nutrient
from .find_nutrients import nutrients_to_find, nutrients_to_avoid
from .find_non_vegan_langual_codes import dynamically_determine_non_vegan_langual_codes
from .core import is_vegan, find_relevant_vegan_foods, print_relevant_foods
from .utils import get_data_file_path
