def target_nutrients():
    # as Euro FIR codes, in order
    return [
        "VITA",  # Vitamin A TODO and CARTB
        "RIBF",  # Vitamin B2
        "VITB6",  # Vitamin B6
        "CA",  # Calcium
        "FE",  # Iron
        "ZN",  # Zinc
        "SE",  # Selenium
        "VITB12",  # Vitamin B12
        "ID"  # Iodine
    ]


def nutrients_to_avoid():
    # as Euro FIR codes
    return {
        # always animal-derived
        "FATRS"  # Trans-fats
        "RETOL",  # Retinonal
        "CHORL",  # Cholesterol
    }
