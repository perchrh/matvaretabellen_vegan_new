import logging

import vegan_foods

if __name__ == "__main__":
    # Configure logging to display debug messages
    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

    foods = vegan_foods.food_list()
    target_nutrients = vegan_foods.target_nutrients()

    logger = logging.getLogger('vegan_foods')

    status = ["considering", len(foods), "foods", "regarding", len(target_nutrients), "nutrients"]
    logger.info(" ".join(str(x) for x in status))
