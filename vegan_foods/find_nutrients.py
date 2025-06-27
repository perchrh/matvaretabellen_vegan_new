# List of nutrients to find with their possible alternative names
# TODO use the EUROFIR codes, if always present
def target_nutrients():
    return {
        "Vitamin A": "Vit A RE",
        "Vitamin B2": "Vit B2",
        "Vitamin B6": "Vit B6",
        "Kalsium": "Ca",
        "Jern": "Fe",
        "Sink": "Zn",
        "Selen": "Se",
        # fortified nutrients
        "Vitamin B12": "Vit B12",
        "Jod": "I"
    }


nutrients_to_avoid = {
    "Cholesterol": "Kolest",  # animal-derived
    "Retinol": "Retinol",  # animal-derived
    "Trans fatty acids": "Trans",  # animal-derived
    # "EPA": "C20:5n-3Eikosapentaensyre",  # assumed to be animal-derived
    # "DPA": "C22:5n-3Dokosapentaensyre",  # assumed to be animal-derived
    # "DHA": "C22:6n-3Dokosaheksaensyre",  # assumed to be animal-derived
    # "Taurine": "TAURINE",  # amino acid primarily from animal sources
    # "Creatine": "CREATINE",  # compound primarily from animal sources
    # "Carnosine": "CARNOSINE"  # dipeptide primarily from animal sources
}
