import json

from .utils import get_data_file_path, logger


def read_foods_json(file_path='foods.json'):
    """
    Read and parse the foods.json file

    Args:
        file_path (str): Path to the foods.json file

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


def get_food_by_name(data, name):
    """
    Find a food item by name

    Args:
        data (dict): Parsed foods.json data
        name (str): Name of the food to search for

    Returns:
        dict or None: Food item if found, None otherwise
    """
    if not data or 'foods' not in data:
        return None

    for food in data['foods']:
        if 'foodName' in food and name.lower() in food['foodName'].lower():
            return food
    return None


def get_foods_by_nutrient(data, nutrient_id, min_value=None):
    """
    Find food items containing a specific nutrient

    Args:
        data (dict): Parsed foods.json data
        nutrient_id (str): ID of the nutrient to search for
        min_value (float, optional): Minimum value of the nutrient

    Returns:
        list: List of food items containing the nutrient
    """
    if not data or 'foods' not in data:
        return []

    matching_foods = []
    for food in data['foods']:
        if 'constituents' not in food:
            continue

        for constituent in food['constituents']:
            if constituent.get('nutrientId') == nutrient_id:
                if min_value is None or ('quantity' in constituent and constituent['quantity'] >= min_value):
                    matching_foods.append(food)
                    break

    return matching_foods


def main():
    # Read and parse the foods.json file
    data = read_foods_json()
    if not data:
        return

    # Print the total number of food items
    logger.debug("Total number of food items: %s", len(data['foods']))

    # Example 1: Find a specific food by name
    food = get_food_by_name(data, "Adzuki beans")
    if food:
        logger.debug("\nFound food: %s", food['foodName'])
        logger.debug("Calories: %s %s", food['calories']['quantity'], food['calories']['unit'])
        logger.debug("Latin name: %s", food.get('latinName', 'N/A'))

    # Example 2: Find foods with high iron content
    iron_foods = get_foods_by_nutrient(data, "Fe", 5.0)  # Iron with minimum 5.0 units
    logger.debug("\nFound %s foods with high iron content:", len(iron_foods))
    for i, food in enumerate(iron_foods[:5], 1):  # Show first 5 results
        logger.debug("%s. %s", i, food['foodName'])

    # Example 3: Get all unique nutrient IDs
    nutrient_ids = set()
    for food in data['foods']:
        if 'constituents' in food:
            for constituent in food['constituents']:
                if 'nutrientId' in constituent:
                    nutrient_ids.add(constituent['nutrientId'])

    logger.debug("\nTotal unique nutrients: %s", len(nutrient_ids))
    logger.debug("Sample nutrients: %s", list(nutrient_ids)[:5])


if __name__ == "__main__":
    main()
