import json
import re

from vegan_foods.utils import get_data_file_path, logger

boring_langual_codes = {
    "B3749",  # supplements
    "B3764",  # supplements
}

allow_listed_langual_codes = {
    "P0171",  # Lactose free food,
    "P0072",  # No animal fat added claim or use
    "A0639",  # Beverages, excluding dairy products (CCFAC)
    "A0836",  # too broad category - Sugar, honey or syrup (EUROFIR)
    "A0840",  # Beverage (NON-MILK) (EUROFIR)
    "P0200",  # No pork added
    "P0201",  # No beef added
    "P0175"  # Egg free claim or use
}


def read_langual_json(file_path='langual.json'):
    """
    Read and parse the langual.json file

    Args:
        file_path (str): Path to the langual.json file

    Returns:
        dict: Parsed JSON data
    """
    try:
        # Get the absolute path to the data file
        abs_file_path = get_data_file_path(file_path)
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        logger.debug("Error: File '%s' not found.", file_path)
        return None
    except json.JSONDecodeError:
        logger.debug("Error: Unable to parse '%s' as JSON.", file_path)
        return None


def find_non_vegan_langual_codes():
    """
    Find LanguaL codes that contain non-vegan keywords

    Returns:
        set: Set of non-vegan LanguaL codes
    """
    data = read_langual_json()
    if not data:
        return set()

    # Keywords that indicate non-vegan ingredients
    non_vegan_keywords = [
        'egg', 'eggs', 'albumin', 'yolk',
        'milk', 'dairy', 'cheese', 'cream', 'lactose', 'casein', 'whey',
        'honey', 'beeswax', 'propolis', 'royal jelly',
        'meat', 'beef', 'pork', 'chicken', 'turkey', 'lamb', 'veal', 'duck', 'goose',
        'fish', 'salmon', 'tuna', 'cod', 'herring', 'sardine', 'mackerel', 'seafood',
        'shellfish', 'shrimp', 'crab', 'lobster', 'oyster', 'mussel', 'clam',
        'gelatin', 'gelatine', 'collagen',
        'lard', 'tallow', 'suet', 'game', 'batrachian',
        'cow', 'pig', 'sheep', 'goat', 'animal',
        'bone', 'blood', 'organ',
        'isinglass', 'carmine', 'cochineal', 'shellac'
    ]
    allowed_keywords = {"analog", "fruit", "imitation", "substitute", "mushroom", "analogue",
                        "substitutes", "fungus"}

    non_vegan_codes = set()

    # Check if the data has a 'langual' key or is a list directly
    langual_items = data.get('langual', data) if isinstance(data, dict) else data

    for item in langual_items["codes"]:
        code = item.get('langualCode', '')
        description = item.get('description', '').lower()

        # Check if any non-vegan keyword appears in the description
        for keyword in non_vegan_keywords:
            description_words = set(description.split())
            intersection = description_words.intersection(allowed_keywords)
            contains_allow_listed_words = len(intersection) > 0
            if re.search(r'\b' + keyword + r'\b', description) and not contains_allow_listed_words:
                non_vegan_codes.add(code)
                logger.debug("Found non-vegan code: %s - %s", code, item.get('description', ''))
                break

    return non_vegan_codes


def dynamically_determine_non_vegan_langual_codes():
    """
    Create a comprehensive list of non-vegan LanguaL codes
    """

    # Dynamically found codes
    all_undesired_langual_codes = find_non_vegan_langual_codes().union(boring_langual_codes) - allow_listed_langual_codes

    logger.debug("\nTotal non-vegan LanguaL codes found: %s", len(all_undesired_langual_codes))
    for code in sorted(all_undesired_langual_codes):
        logger.debug('    "%s",', code)

    return sorted(all_undesired_langual_codes)


def main():
    logger.debug("Searching for non-vegan LanguaL codes...")

    dynamically_determine_non_vegan_langual_codes()


if __name__ == "__main__":
    main()
