Data source: https://www.matvaretabellen.no/api/

load the data
cd vegan_foods
curl -O https://www.matvaretabellen.no/api/en/foods.json
curl -O https://www.matvaretabellen.no/api/langual.json
curl -O https://www.matvaretabellen.no/api/en/food-groups.json
curl -O https://www.matvaretabellen.no/api/en/nutrients.json

run main.py

Uses a type of dominant sorting to find the best foods in terms of nutrients that are least common in foods for vegans

Output excerpt: 

++ Food group: Nuts and seed products ++
1 Almond spread, home-made {'Vitamin B2': '0.9 mg', 'Vitamin B6': '0.13 mg', 'Calsium': '255.0 mg', 'Iron': '3.4 mg', 'Zinc': '3.2 mg', 'Selenium': '2.0 µg', 'Iodine': '0.6 µg'}
2 Cashew nut spread, home-made {'Vitamin B2': '0.06 mg', 'Vitamin B6': '0.41 mg', 'Calsium': '37.0 mg', 'Iron': '6.6 mg', 'Zinc': '5.7 mg', 'Selenium': '2.0 µg', 'Iodine': '11.0 µg'}
3 Mixed nuts with dried fruit {'Vitamin A': '200 µg-RE', 'Vitamin B2': '0.16 mg', 'Vitamin B6': '0.25 mg', 'Calsium': '98.0 mg', 'Iron': '3.4 mg', 'Zinc': '2.4 mg', 'Selenium': '5.0 µg', 'Iodine': '2.0 µg'}
4 Peanut butter {'Vitamin B2': '0.09 mg', 'Vitamin B6': '0.58 mg', 'Calsium': '37.0 mg', 'Iron': '2.1 mg', 'Zinc': '3.0 mg', 'Selenium': '3.0 µg', 'Iodine': '2.0 µg'}
++ Food group: Vegetables, raw and prepared ++
1 Kale, raw {'Vitamin A': '891 µg-RE', 'Vitamin B2': '0.13 mg', 'Vitamin B6': '0.27 mg', 'Calsium': '157.0 mg', 'Iron': '1.7 mg', 'Zinc': '0.4 mg', 'Selenium': '2.0 µg', 'Iodine': '2.0 µg'}
2 Sweet potato, roasted {'Vitamin A': '1453 µg-RE', 'Vitamin B2': '0.08 mg', 'Vitamin B6': '0.26 mg', 'Calsium': '42.0 mg', 'Iron': '0.8 mg', 'Zinc': '0.4 mg', 'Selenium': '1.0 µg', 'Iodine': '3.0 µg'}
3 Water-cress, raw {'Vitamin A': '264 µg-RE', 'Vitamin B2': '0.06 mg', 'Vitamin B6': '0.23 mg', 'Calsium': '138.0 mg', 'Iron': '0.7 mg', 'Zinc': '0.5 mg', 'Selenium': '2.0 µg', 'Iodine': '7.0 µg'}
4 Carrot, imported, frozen {'Vitamin A': '1434 µg-RE', 'Vitamin B6': '0.03 mg', 'Calsium': '20.0 mg', 'Iron': '0.2 mg', 'Zinc': '0.3 mg'}
5 Leaf beet, mangold, raw {'Vitamin A': '607 µg-RE', 'Vitamin B2': '0.09 mg', 'Vitamin B6': '0.1 mg', 'Calsium': '51.0 mg', 'Iron': '1.8 mg', 'Zinc': '0.4 mg', 'Selenium': '1.0 µg', 'Iodine': '1.0 µg'}
