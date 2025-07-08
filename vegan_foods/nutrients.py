from typing import List, Set


def target_nutrients() -> List[str]:
    # as Euro FIR codes, in order
    return [
        "VITA",  # Vitamin A
        "RIBF",  # Vitamin B2
        "VITB6",  # Vitamin B6
        "CA",  # Calcium
        "FE",  # Iron
        "ZN",  # Zinc
        "SE",  # Selenium
        "VITB12",  # Vitamin B12
        "ID"  # Iodine
    ]


def nutrients_to_avoid() -> Set[str]:
    # as Euro FIR codes
    return {
        "FATRS",  # Trans-fats, always animal-derived
        "RETOL",  # Retinol, always animal-derived
        "CHORL",  # Cholesterol, always animal-derived
        "CLA",  # Conjugated Linoleic Acid,	only found in ruminant fats
    }
