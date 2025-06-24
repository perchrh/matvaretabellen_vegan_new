import json

from .utils import get_data_file_path, logger

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

def target_nutrients():
    return nutrients_to_find

nutrients_to_avoid = {
    "Cholesterol": "Kolest",
    "Retinol": "Retinol",
    "Trans fatty acids": "Trans",
    "EPA": "C20:5n-3Eikosapentaensyre",  # assumed to be animal-derived
    "DPA": "C22:5n-3Dokosapentaensyre",  # assumed to be animal-derived
    "DHA": "C22:6n-3Dokosaheksaensyre",  # assumed to be animal-derived
    "Taurine": "TAURINE",  # amino acid primarily from animal sources
    "Creatine": "CREATINE",  # compound primarily from animal sources
    "Carnosine": "CARNOSINE"  # dipeptide primarily from animal sources
}

# Read the nutrients.json file
try:
    # Get the absolute path to the data file
    abs_file_path = get_data_file_path('nutrients.json')
    with open(abs_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Check if the file has the expected structure
    if 'nutrients' not in data:
        logger.debug("Error: 'nutrients' key not found in the JSON file.")
        exit(1)

    # Create a dictionary to store the results
    results = {}

    # Dictionary to track which original nutrients we've found
    found_original_nutrients = {original: False for original in nutrients_to_find.keys()}

    # Search for each nutrient
    for nutrient in data['nutrients']:
        name = nutrient.get('name', '')
        logger.debug("Considering nutrient %s", name)

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
                    logger.debug("Found match for '%s': %s - nutrientId: %s", original, name, nutrient_id)

    # Print a summary of the results
    logger.debug("\nSUMMARY:")
    for original in nutrients_to_find.keys():
        if original in results:
            logger.debug("%s:", original)
            for name, nutrient_id in set(results[original]):
                logger.debug("  - %s: %s", name, nutrient_id)
        else:
            logger.debug("%s: Not found", original)

    # Check if we found all the nutrients
    for original, found in found_original_nutrients.items():
        if not found:
            logger.debug("Warning: Could not find any match for '%s' in the nutrients.json file.", original)

    # Generate Python code listing all the nutrientId values found
    logger.debug("\n# Python code listing all nutrientId values found:")
    logger.debug("nutrient_ids = {")
    for original in nutrients_to_find.keys():
        if original in results:
            # Get unique nutrient IDs for this original nutrient
            unique_ids = set(nutrient_id for _, nutrient_id in results[original])
            # If there are multiple IDs, use a list, otherwise use a single string
            if len(unique_ids) > 1:
                ids_str = "[" + ", ".join(f'"{id}"' for id in unique_ids) + "]"
            else:
                ids_str = f'"{next(iter(unique_ids))}"'
            logger.debug('    "%s": %s,', original, ids_str)
        else:
            logger.debug('    "%s": None,  # Not found', original)
    logger.debug("}")

except FileNotFoundError:
    logger.debug("Error: File 'nutrients.json' not found.")
except json.JSONDecodeError:
    logger.debug("Error: Unable to parse 'nutrients.json' as JSON.")
except Exception as e:
    logger.debug("Error: %s", str(e))
