import json


def read_foods_json(file_path='foods.json'):
    """
    Read and parse the foods.json file

    Args:
        file_path (str): Path to the foods.json file

    Returns:
        dict: Parsed JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse '{file_path}' as JSON.")
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
    print(f"Total number of food items: {len(data['foods'])}")

    # Example 1: Find a specific food by name
    food = get_food_by_name(data, "Adzuki beans")
    if food:
        print(f"\nFound food: {food['foodName']}")
        print(f"Calories: {food['calories']['quantity']} {food['calories']['unit']}")
        print(f"Latin name: {food.get('latinName', 'N/A')}")

    # Example 2: Find foods with high iron content
    iron_foods = get_foods_by_nutrient(data, "Fe", 5.0)  # Iron with minimum 5.0 units
    print(f"\nFound {len(iron_foods)} foods with high iron content:")
    for i, food in enumerate(iron_foods[:5], 1):  # Show first 5 results
        print(f"{i}. {food['foodName']}")

    # Example 3: Get all unique nutrient IDs
    nutrient_ids = set()
    for food in data['foods']:
        if 'constituents' in food:
            for constituent in food['constituents']:
                if 'nutrientId' in constituent:
                    nutrient_ids.add(constituent['nutrientId'])

    print(f"\nTotal unique nutrients: {len(nutrient_ids)}")
    print(f"Sample nutrients: {list(nutrient_ids)[:5]}")


if __name__ == "__main__":
    main()
