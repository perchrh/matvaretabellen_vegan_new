import json

from .utils import get_data_file_path

# List of nutrients to find with their possible alternative names
nutrients_to_find = {
    "Vitamin A": ["Vitamin A"],
    "Riboflavin": ["Riboflavin", "Vitamin B2"],
    "Vitamin B6": ["Vitamin B6", "pyridoxine"],
    "Kalsium": ["Kalsium", "Calcium", "Ca"],
    "Jern": ["Jern", "Iron", "Fe"],
    "Sink": ["Sink", "Zinc", "Zn"],
    "Selen": ["Selen", "Selenium", "Se"]
}

try:
    # Read the nutrients.json file
    # Get the absolute path to the data file
    abs_file_path = get_data_file_path('nutrients.json')
    with open(abs_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Check if the file has the expected structure
    if 'nutrients' not in data:
        print("Error: 'nutrients' key not found in the JSON file.")
        exit(1)

    # Create a dictionary to store the results
    results = {}

    # Dictionary to track which original nutrients we've found
    found_original_nutrients = {original: False for original in nutrients_to_find.keys()}

    # Search for each nutrient
    for nutrient in data['nutrients']:
        name = nutrient.get('name', '')

        # Check if this nutrient matches any of our search terms
        for original, alternatives in nutrients_to_find.items():
            for alt in alternatives:
                if alt.lower() in name.lower():
                    nutrient_id = nutrient.get('nutrientId', 'Not found')
                    # Store with the original name as the key
                    if original not in results:
                        results[original] = []
                    results[original].append((name, nutrient_id))
                    found_original_nutrients[original] = True

    # Generate Python code listing all the nutrientId values found
    print("nutrient_ids = {")
    for original in nutrients_to_find.keys():
        if original in results:
            # Get unique nutrient IDs for this original nutrient
            unique_ids = set(nutrient_id for _, nutrient_id in results[original])
            # If there are multiple IDs, use a list, otherwise use a single string
            if len(unique_ids) > 1:
                ids_str = "[" + ", ".join(f'"{id}"' for id in unique_ids) + "]"
            else:
                ids_str = f'"{next(iter(unique_ids))}"'
            print(f'    "{original}": {ids_str},')
        else:
            print(f'    "{original}": None,  # Not found')
    print("}")

except FileNotFoundError:
    print("Error: File 'nutrients.json' not found.")
except json.JSONDecodeError:
    print("Error: Unable to parse 'nutrients.json' as JSON.")
except Exception as e:
    print(f"Error: {str(e)}")
