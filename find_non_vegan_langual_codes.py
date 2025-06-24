import json
import re

boring_langual_codes = {
    "B3749",  # supplements
    "A0806",  # oil product only
    "H0175",  # fizzy drinks
    "A0134",  # Salt or salt substitute (US CFR)
    "A0856",  # Seasoning or extract (EUROFIR)
    "A0181",  # Food additive (US CFR)
    "A0854",  # Baking ingredient (EUROFIR)
    "A0133",  # Flavoring or seasoning (US CFR)
    "A0853",  # Spice, condiment or other ingredient (EUROFIR)
    "A0845",  # Coffee, tea, cocoa (EUROFIR)
    "A0299",  # Light wine, 7-14% alcohol (US CFR)
    "A0849",  # Wine, fortified wine or wine-like beverage (EUROFIR)
    "A0200",  # Distinctive distilled spirits (US CFR)
    "A0850",  # Liqueur or spirits (EUROFIR)
    "A0847",  # Beer or beer-like beverage (EUROFIR)
    "Z0165",  # alcohol content
    "Z0166",  # alcohol content
    "Z0167",  # alcohol content
    "Z0168",  # alcohol content
    "Z0169",  # alcohol content
    "Z0170",  # alcohol content
    "Z0171",  # alcohol content
    "A0297"  # wine
    "A0298"  # wine
    "A0299"  # wine
    "A0224"  # wine

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
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse '{file_path}' as JSON.")
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
        'lard', 'tallow', 'suet', 'game', 'batrachian'
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
                print(f"Found non-vegan code: {code} - {item.get('description', '')}")
                break

    return non_vegan_codes


def dynamically_determine_non_vegan_langual_codes():
    """
    Create a comprehensive list of non-vegan LanguaL codes
    """

    # Dynamically found codes
    all_non_vegan_codes = find_non_vegan_langual_codes().union(boring_langual_codes) - allow_listed_langual_codes

    print(f"\nTotal non-vegan LanguaL codes found: {len(all_non_vegan_codes)}")
    for code in sorted(all_non_vegan_codes):
        print(f'    "{code}",')

    return sorted(all_non_vegan_codes)


def main():
    print("Searching for non-vegan LanguaL codes...")

    dynamically_determine_non_vegan_langual_codes()


if __name__ == "__main__":
    main()
