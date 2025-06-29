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

++ Food group: Vegetable products ++
1 Asparagus, canned, drained {'Vitamin A': '82 µg-RE', 'Vitamin B2': '0.1 mg', 'Vitamin B6': '0.11 mg', 'Kalsium': '16.0 mg', 'Jern': '0.4 mg', 'Sink': '0.4 mg', 'Jod': '0.7 µg'}
2 Baby carrot, baby corn, French beans, frozen {'Vitamin A': '474 µg-RE', 'Vitamin B2': '0.05 mg', 'Vitamin B6': '0.05 mg', 'Kalsium': '35.0 mg', 'Jern': '0.8 mg', 'Sink': '0.2 mg', 'Jod': '1.0 µg'}
3 Baby corn, canned {'Vitamin A': '23 µg-RE', 'Vitamin B2': '0.04 mg', 'Kalsium': '8.0 mg', 'Jern': '1.2 mg', 'Jod': '1.0 µg'}
4 Bamboo shoots, canned {'Vitamin A': '1 µg-RE', 'Vitamin B2': '0.06 mg', 'Vitamin B6': '0.14 mg', 'Kalsium': '13.0 mg', 'Jern': '0.4 mg', 'Sink': '1.1 mg', 'Selen': '1.0 µg', 'Jod': '0.5 µg'}
5 Beetroot, pickled {'Kalsium': '17.0 mg', 'Jern': '0.3 mg', 'Sink': '0.3 mg', 'Jod': '0.4 µg'}
++ Food group: Legumes ++
1 Beans, black, canned {'Vitamin B2': '0.1 mg', 'Kalsium': '71.0 mg', 'Jern': '2.0 mg', 'Sink': '0.9 mg'}
2 Beans, brown, cooked  {'Vitamin A': '1 µg-RE', 'Vitamin B2': '0.06 mg', 'Vitamin B6': '0.09 mg', 'Kalsium': '48.0 mg', 'Jern': '1.8 mg', 'Sink': '0.8 mg', 'Selen': '1.0 µg', 'Jod': '3.0 µg'}
3 Beans, green, French, frozen {'Vitamin A': '56 µg-RE', 'Vitamin B2': '0.07 mg', 'Vitamin B6': '0.06 mg', 'Kalsium': '71.0 mg', 'Jern': '0.9 mg', 'Sink': '0.3 mg'}
4 Beans, green, French, raw {'Vitamin A': '18 µg-RE', 'Vitamin B2': '0.06 mg', 'Vitamin B6': '0.1 mg', 'Kalsium': '51.0 mg', 'Jern': '1.2 mg', 'Sink': '0.4 mg', 'Selen': '1.0 µg', 'Jod': '1.0 µg'}
5 Beans, in chili sauce, canned {'Vitamin A': '11 µg-RE', 'Vitamin B2': '0.1 mg', 'Vitamin B6': '0.1 mg', 'Kalsium': '41.0 mg', 'Jern': '1.5 mg', 'Sink': '0.6 mg', 'Selen': '1.0 µg'}
