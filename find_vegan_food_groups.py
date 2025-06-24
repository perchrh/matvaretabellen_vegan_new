import json

food_categories = [
    "Korn- og bakevarer",
    "Grønnsaker",
    "Drikke",
    "Belgvekster",
    "Frukt og bær",
    "Nøtter og frø",
    "Poteter",
    "Urter og krydder",
    "Sukker og søte produkter",
    "Spisefett",
    "Diverse matvarer og retter",
    "Spedbarnsmat"
]

def load_food_groups():
    """Load food groups from JSON file"""
    with open('food-groups.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['foodGroups']

def create_category_mapping():
    """Create mapping from Norwegian category names to foodGroupIds"""
    # Translation mapping from Norwegian to English
    norwegian_to_english = {
        "Korn- og bakevarer": "Cereals, bread and cakes",
        "Grønnsaker": "Vegetables", 
        "Drikke": "Beverages",
        "Belgvekster": "Legumes",
        "Frukt og bær": "Fruit and berries",
        "Nøtter og frø": "Nuts and seeds",
        "Poteter": "Potatoes",
        "Urter og krydder": "Herbs and spices",
        "Sukker og søte produkter": "Sugar and sweet products",
        "Spisefett": "Cooking fat",
        "Diverse matvarer og retter": "Other foods and dishes",
        "Spedbarnsmat": "Infant food"
    }
    
    # Load food groups from JSON
    food_groups = load_food_groups()
    
    # Create mapping from English names to foodGroupIds
    english_to_id = {}
    for group in food_groups:
        # Only include top-level groups (no parentId)
        if 'parentId' not in group:
            english_to_id[group['name']] = group['foodGroupId']
    
    # Create final mapping from Norwegian to foodGroupId
    category_to_id = {}
    for norwegian, english in norwegian_to_english.items():
        if english in english_to_id:
            category_to_id[norwegian] = english_to_id[english]
        else:
            print(f"Warning: Could not find foodGroupId for '{norwegian}' -> '{english}'")
    
    return category_to_id

def main():
    category_to_id = create_category_mapping()

    for category in food_categories:
        if category in category_to_id:
            print(f"{category}: {category_to_id[category]}")

if __name__ == "__main__":
    main()
