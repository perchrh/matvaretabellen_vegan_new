Top vegan food items from Matvaretabellen

A program that outputs the foods most rich in the nutrients that can be harder to find
as a vegan, like selenium, iodine, pyridoxine, etc.

It parses the open data from Matvaretabellen,
filters out non-vegan items, as well as not relevant items
like spices and bottled water. 
Then uses a type of dominant sorting to find the best foods in terms of nutrients.

Data source: https://www.matvaretabellen.no/api/

load the data
cd vegan_foods
export LANG=nb # or nb
curl -O https://www.matvaretabellen.no/api/$LANG/foods.json
curl -O https://www.matvaretabellen.no/api/langual.json
curl -O https://www.matvaretabellen.no/api/$LANG/food-groups.json
curl -O https://www.matvaretabellen.no/api/$LANG/nutrients.json

run main.py

Output excerpt:

```
++ Vegetarian products and dishes ++
1 Cultured, thickened oat product {'Vitamin B2 (riboflavin)': '0.29 mg', 'Calcium (Ca)': '120.0 mg', 'Zinc (Zn)': '0.1 mg', 'Vitamin B12 (cobalamin)': '0.4 µg', 'Iodine (I)': '23.0 µg'}
2 Falafel, chickpeas balls, with Hälsans kök {'Vitamin A (RAE)': '8.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.07 mg', 'Vitamin B6 (pyridoxine)': '0.18 mg', 'Calcium (Ca)': '65.0 mg', 'Iron (Fe)': '2.4 mg', 'Zinc (Zn)': '1.0 mg', 'Selenium (Se)': '24.0 µg'}
3 Plant-based balls {'Vitamin A (RAE)': '14.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.09 mg', 'Vitamin B6 (pyridoxine)': '0.1 mg', 'Calcium (Ca)': '59.0 mg', 'Iron (Fe)': '2.5 mg', 'Zinc (Zn)': '1.1 mg', 'Selenium (Se)': '7.0 µg', 'Iodine (I)': '0.9 µg'}
4 Plant-based balls, potato and lentils, Hoff {'Vitamin A (RAE)': '38.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.11 mg', 'Vitamin B6 (pyridoxine)': '0.17 mg', 'Calcium (Ca)': '44.0 mg', 'Iron (Fe)': '1.8 mg', 'Zinc (Zn)': '0.9 mg', 'Selenium (Se)': '7.0 µg', 'Iodine (I)': '3.0 µg'}
5 Plant-based burger {'Vitamin A (RAE)': '3.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.08 mg', 'Vitamin B6 (pyridoxine)': '0.14 mg', 'Calcium (Ca)': '82.0 mg', 'Iron (Fe)': '2.2 mg', 'Zinc (Zn)': '0.9 mg', 'Selenium (Se)': '6.0 µg', 'Iodine (I)': '2.0 µg'}
6 Plant-based burger, potato and lentils, Hoff {'Vitamin A (RAE)': '7.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.07 mg', 'Vitamin B6 (pyridoxine)': '0.2 mg', 'Calcium (Ca)': '43.0 mg', 'Iron (Fe)': '1.9 mg', 'Zinc (Zn)': '0.9 mg', 'Selenium (Se)': '9.0 µg', 'Iodine (I)': '2.0 µg'}
7 Plant-based grill sausage {'Vitamin A (RAE)': '12.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.15 mg', 'Vitamin B6 (pyridoxine)': '0.15 mg', 'Calcium (Ca)': '66.0 mg', 'Iron (Fe)': '1.9 mg', 'Zinc (Zn)': '0.9 mg', 'Selenium (Se)': '4.0 µg', 'Iodine (I)': '3.0 µg'}
8 Plant-based grill sausage, vegetables and potato, Hoff {'Vitamin A (RAE)': '32.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.23 mg', 'Vitamin B6 (pyridoxine)': '0.1 mg', 'Calcium (Ca)': '29.0 mg', 'Iron (Fe)': '0.6 mg', 'Zinc (Zn)': '0.2 mg', 'Selenium (Se)': '5.0 µg', 'Iodine (I)': '3.0 µg'}
9 Plant-based minced {'Vitamin B2 (riboflavin)': '0.11 mg', 'Vitamin B6 (pyridoxine)': '0.1 mg', 'Calcium (Ca)': '141.0 mg', 'Iron (Fe)': '2.9 mg', 'Zinc (Zn)': '1.1 mg', 'Selenium (Se)': '7.0 µg', 'Vitamin B12 (cobalamin)': '0.1 µg', 'Iodine (I)': '2.0 µg'}
10 Plant-based minced, pea protein, Naturli {'Vitamin A (RAE)': '2.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.08 mg', 'Calcium (Ca)': '280.0 mg', 'Iron (Fe)': '3.8 mg', 'Zinc (Zn)': '1.8 mg', 'Selenium (Se)': '17.0 µg', 'Vitamin B12 (cobalamin)': '0.3 µg', 'Iodine (I)': '2.0 µg'}

... 

++ Legumes ++
1 Edamame, soy beans, frozen {'Vitamin A (RAE)': '14.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.27 mg', 'Vitamin B6 (pyridoxine)': '0.14 mg', 'Calcium (Ca)': '60.0 mg', 'Iron (Fe)': '2.1 mg', 'Zinc (Zn)': '1.3 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '2.0 µg'}
2 Lentils, black, beluga, uncooked {'Vitamin A (RAE)': '6.0 µg-RE', 'Vitamin B2 (riboflavin)': '1.6 mg', 'Vitamin B6 (pyridoxine)': '0.4 mg', 'Calcium (Ca)': '53.0 mg', 'Iron (Fe)': '5.8 mg', 'Zinc (Zn)': '3.7 mg', 'Selenium (Se)': '63.0 µg'}
3 Lentils, green, puy, uncooked {'Vitamin A (RAE)': '4.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.2 mg', 'Vitamin B6 (pyridoxine)': '0.3 mg', 'Calcium (Ca)': '60.0 mg', 'Iron (Fe)': '8.8 mg', 'Zinc (Zn)': '4.5 mg', 'Selenium (Se)': '9.0 µg'}
4 Lentils, red, canned {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '25.0 mg', 'Iron (Fe)': '1.6 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '21.0 µg', 'Iodine (I)': '2.0 µg'}
5 Peas, green, canned, drained {'Vitamin A (RAE)': '33.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.04 mg', 'Vitamin B6 (pyridoxine)': '0.05 mg', 'Calcium (Ca)': '24.0 mg', 'Iron (Fe)': '1.1 mg', 'Zinc (Zn)': '0.7 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '2.0 µg'}
6 Beans, brown, cooked  {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.06 mg', 'Vitamin B6 (pyridoxine)': '0.09 mg', 'Calcium (Ca)': '48.0 mg', 'Iron (Fe)': '1.8 mg', 'Zinc (Zn)': '0.8 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '3.0 µg'}
7 Peas, frozen {'Vitamin A (RAE)': '27.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.09 mg', 'Vitamin B6 (pyridoxine)': '0.09 mg', 'Calcium (Ca)': '36.0 mg', 'Iron (Fe)': '1.4 mg', 'Zinc (Zn)': '0.9 mg'}
8 Yardlong beans, raw {'Vitamin A (RAE)': '40.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.11 mg', 'Vitamin B6 (pyridoxine)': '0.02 mg', 'Calcium (Ca)': '50.0 mg', 'Iron (Fe)': '0.5 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '2.0 µg'}
9 Peas, sugar-snap, Norwegian, raw {'Vitamin A (RAE)': '12.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.04 mg', 'Vitamin B6 (pyridoxine)': '0.04 mg', 'Calcium (Ca)': '54.0 mg', 'Iron (Fe)': '1.1 mg', 'Zinc (Zn)': '0.7 mg', 'Iodine (I)': '2.0 µg'}
10 Beans, green, French, raw {'Vitamin A (RAE)': '9.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.06 mg', 'Vitamin B6 (pyridoxine)': '0.1 mg', 'Calcium (Ca)': '51.0 mg', 'Iron (Fe)': '1.2 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '1.0 µg'}

...

++ Crisp bread and flatbread ++
1 Crisp bread, Synnøve Grovkrisp sesamfrø og linfrø {'Vitamin B2 (riboflavin)': '0.14 mg', 'Vitamin B6 (pyridoxine)': '0.34 mg', 'Calcium (Ca)': '430.0 mg', 'Iron (Fe)': '4.8 mg', 'Zinc (Zn)': '3.8 mg', 'Selenium (Se)': '15.0 µg', 'Iodine (I)': '2.0 µg'}
2 Crisp bread, rye and spelt, Sigdal helsprøtt {'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.39 mg', 'Calcium (Ca)': '88.0 mg', 'Iron (Fe)': '5.2 mg', 'Zinc (Zn)': '4.7 mg', 'Selenium (Se)': '15.0 µg', 'Iodine (I)': '2.0 µg'}
3 Crisp bread, rye, Husman Sport {'Vitamin B2 (riboflavin)': '0.1 mg', 'Vitamin B6 (pyridoxine)': '0.31 mg', 'Calcium (Ca)': '55.0 mg', 'Iron (Fe)': '3.4 mg', 'Zinc (Zn)': '3.1 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '6.0 µg'}
4 Crisp bread, wholemeal flour, rye, thin, Rugsprø, Finncrisp {'Vitamin B2 (riboflavin)': '0.18 mg', 'Vitamin B6 (pyridoxine)': '0.36 mg', 'Calcium (Ca)': '34.0 mg', 'Iron (Fe)': '4.0 mg', 'Zinc (Zn)': '3.1 mg', 'Selenium (Se)': '24.0 µg', 'Iodine (I)': '113.0 µg'}
5 Rice cake, with salt {'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.61 mg', 'Calcium (Ca)': '20.0 mg', 'Iron (Fe)': '1.7 mg', 'Zinc (Zn)': '1.5 mg', 'Selenium (Se)': '23.0 µg', 'Iodine (I)': '2.0 µg'}
6 Rice cake, without salt {'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.61 mg', 'Calcium (Ca)': '20.0 mg', 'Iron (Fe)': '1.7 mg', 'Zinc (Zn)': '1.5 mg', 'Selenium (Se)': '23.0 µg', 'Iodine (I)': '2.0 µg'}
7 Crisp bread, Mesterbakeren Original {'Vitamin B2 (riboflavin)': '0.12 mg', 'Vitamin B6 (pyridoxine)': '0.31 mg', 'Calcium (Ca)': '72.0 mg', 'Iron (Fe)': '4.6 mg', 'Zinc (Zn)': '4.4 mg', 'Selenium (Se)': '11.0 µg', 'Iodine (I)': '2.0 µg'}
8 Crisp bread, home-made {'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.28 mg', 'Calcium (Ca)': '127.0 mg', 'Iron (Fe)': '4.5 mg', 'Zinc (Zn)': '3.5 mg', 'Selenium (Se)': '8.0 µg', 'Iodine (I)': '0.2 µg'}
9 Crisp bread, with wheat bran {'Vitamin B2 (riboflavin)': '0.2 mg', 'Vitamin B6 (pyridoxine)': '0.65 mg', 'Calcium (Ca)': '84.0 mg', 'Iron (Fe)': '9.8 mg', 'Zinc (Zn)': '6.4 mg', 'Selenium (Se)': '2.0 µg'}
10 Crisp bread, wholemeal flour, rye, Husman {'Vitamin B2 (riboflavin)': '0.16 mg', 'Vitamin B6 (pyridoxine)': '0.21 mg', 'Calcium (Ca)': '39.0 mg', 'Iron (Fe)': '2.2 mg', 'Zinc (Zn)': '2.0 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '2.0 µg'}

... 

++ Vegetables, raw and prepared ++
1 Jalapeño, raw {'Vitamin A (RAE)': '47.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.07 mg', 'Vitamin B6 (pyridoxine)': '0.42 mg', 'Calcium (Ca)': '12.0 mg', 'Iron (Fe)': '0.3 mg', 'Zinc (Zn)': '0.1 mg', 'Iodine (I)': '0.4 µg'}
2 Kale, frozen, raw {'Vitamin A (RAE)': '216.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.08 mg', 'Vitamin B6 (pyridoxine)': '0.07 mg', 'Calcium (Ca)': '175.0 mg', 'Iron (Fe)': '0.6 mg', 'Zinc (Zn)': '0.2 mg'}
3 Kale, raw {'Vitamin A (RAE)': '446.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.27 mg', 'Calcium (Ca)': '157.0 mg', 'Iron (Fe)': '1.7 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '2.0 µg'}
4 Leaf beet, mangold, raw {'Vitamin A (RAE)': '304.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.09 mg', 'Vitamin B6 (pyridoxine)': '0.1 mg', 'Calcium (Ca)': '51.0 mg', 'Iron (Fe)': '1.8 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '1.0 µg'}
5 Mushroom, trumpet chanterelle, funnel chanterelle, raw {'Vitamin A (RAE)': '110.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.26 mg', 'Vitamin B6 (pyridoxine)': '0.04 mg', 'Calcium (Ca)': '4.0 mg', 'Iron (Fe)': '0.8 mg', 'Zinc (Zn)': '0.8 mg', 'Selenium (Se)': '18.0 µg', 'Iodine (I)': '1.0 µg'}
6 Nettle, parboiled {'Vitamin A (RAE)': '228.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.12 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '280.0 mg', 'Iron (Fe)': '2.8 mg', 'Zinc (Zn)': '0.3 mg'}
7 Purslane, raw {'Vitamin A (RAE)': '183.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.04 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '125.0 mg', 'Iron (Fe)': '3.0 mg', 'Zinc (Zn)': '0.2 mg', 'Iodine (I)': '4.0 µg'}
8 Salad, rocket, raw {'Vitamin A (RAE)': '210.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.21 mg', 'Vitamin B6 (pyridoxine)': '0.2 mg', 'Calcium (Ca)': '268.0 mg', 'Iron (Fe)': '1.6 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '5.0 µg', 'Iodine (I)': '2.0 µg'}
9 Spinach, frozen {'Vitamin A (RAE)': '268.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.09 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '112.0 mg', 'Iron (Fe)': '0.9 mg', 'Zinc (Zn)': '0.8 mg'}
10 Spinach, raw {'Vitamin A (RAE)': '378.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.17 mg', 'Vitamin B6 (pyridoxine)': '0.28 mg', 'Calcium (Ca)': '83.0 mg', 'Iron (Fe)': '2.1 mg', 'Zinc (Zn)': '0.9 mg', 'Iodine (I)': '3.0 µg'}
++ Vegetable products ++
1 Carrot, peas, sweet corn, frozen {'Vitamin A (RAE)': '402.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '21.0 mg', 'Iron (Fe)': '0.5 mg', 'Zinc (Zn)': '0.5 mg'}
2 Nori, seaweed, dried {'Vitamin A (RAE)': '37.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.32 mg', 'Vitamin B6 (pyridoxine)': '0.01 mg', 'Calcium (Ca)': '680.0 mg', 'Iron (Fe)': '3.3 mg', 'Iodine (I)': '2200.0 µg'}
3 Onion, roasted {'Vitamin A (RAE)': '3.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.11 mg', 'Vitamin B6 (pyridoxine)': '0.39 mg', 'Calcium (Ca)': '42.0 mg', 'Iron (Fe)': '1.2 mg', 'Zinc (Zn)': '0.9 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '14.0 µg'}
4 Tomato purée {'Vitamin A (RAE)': '146.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.12 mg', 'Vitamin B6 (pyridoxine)': '0.28 mg', 'Calcium (Ca)': '45.0 mg', 'Iron (Fe)': '4.5 mg', 'Zinc (Zn)': '0.6 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '2.0 µg'}
5 Tomatoes, sun-dried {'Vitamin A (RAE)': '44.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.49 mg', 'Vitamin B6 (pyridoxine)': '0.33 mg', 'Calcium (Ca)': '110.0 mg', 'Iron (Fe)': '9.1 mg', 'Zinc (Zn)': '2.0 mg', 'Selenium (Se)': '6.0 µg', 'Iodine (I)': '0.7 µg'}
6 Olives, green, filled with sweet pepper, drained {'Vitamin A (RAE)': '20.0 µg-RE', 'Vitamin B6 (pyridoxine)': '0.02 mg', 'Calcium (Ca)': '102.0 mg', 'Iron (Fe)': '0.2 mg', 'Zinc (Zn)': '0.1 mg', 'Iodine (I)': '5.0 µg'}
7 Olives, green, pickled {'Vitamin A (RAE)': '19.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.01 mg', 'Vitamin B6 (pyridoxine)': '0.03 mg', 'Calcium (Ca)': '52.0 mg', 'Iron (Fe)': '0.5 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '5.0 µg'}
8 Olives, black, in oil, canned {'Vitamin A (RAE)': '3.0 µg-RE', 'Vitamin B6 (pyridoxine)': '0.01 mg', 'Calcium (Ca)': '61.0 mg', 'Iron (Fe)': '1.6 mg', 'Zinc (Zn)': '0.2 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '5.0 µg'}
9 Mushroom, common, canned, drained {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.4 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '18.0 mg', 'Iron (Fe)': '0.8 mg', 'Zinc (Zn)': '0.9 mg', 'Selenium (Se)': '3.0 µg'}
10 Carrot, cauliflower, green beans, peas, frozen {'Vitamin A (RAE)': '224.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.05 mg', 'Vitamin B6 (pyridoxine)': '0.08 mg', 'Calcium (Ca)': '36.0 mg', 'Iron (Fe)': '0.6 mg', 'Zinc (Zn)': '0.4 mg', 'Iodine (I)': '0.3 µg'}

.... 

--- Top foods, across all groups ---
1 Almond based beverage, unsweetened, with calcium and vitamins (vit B2, vit B12, vit E, vit D) {'Vitamin B2 (riboflavin)': '0.24 mg', 'Vitamin B6 (pyridoxine)': '0.01 mg', 'Calcium (Ca)': '150.0 mg', 'Iron (Fe)': '0.1 mg', 'Zinc (Zn)': '0.1 mg', 'Vitamin B12 (cobalamin)': '0.3 µg', 'Iodine (I)': '0.2 µg'}
2 Almond flour {'Vitamin B2 (riboflavin)': '0.78 mg', 'Vitamin B6 (pyridoxine)': '0.11 mg', 'Calcium (Ca)': '270.0 mg', 'Iron (Fe)': '3.6 mg', 'Zinc (Zn)': '3.0 mg'}
3 Almond spread, home-made {'Vitamin B2 (riboflavin)': '0.9 mg', 'Vitamin B6 (pyridoxine)': '0.13 mg', 'Calcium (Ca)': '255.0 mg', 'Iron (Fe)': '3.4 mg', 'Zinc (Zn)': '3.2 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '0.6 µg'}
4 Almonds {'Vitamin B2 (riboflavin)': '0.94 mg', 'Vitamin B6 (pyridoxine)': '0.13 mg', 'Calcium (Ca)': '260.0 mg', 'Iron (Fe)': '3.4 mg', 'Zinc (Zn)': '3.3 mg', 'Selenium (Se)': '2.0 µg'}
5 Almonds, without peel {'Vitamin B2 (riboflavin)': '0.41 mg', 'Vitamin B6 (pyridoxine)': '0.12 mg', 'Calcium (Ca)': '236.0 mg', 'Iron (Fe)': '3.3 mg', 'Zinc (Zn)': '3.0 mg', 'Selenium (Se)': '3.0 µg', 'Iodine (I)': '2.0 µg'}
6 Apples, dried {'Vitamin A (RAE)': '8.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.16 mg', 'Vitamin B6 (pyridoxine)': '0.13 mg', 'Calcium (Ca)': '16.0 mg', 'Iron (Fe)': '0.5 mg', 'Zinc (Zn)': '0.5 mg', 'Iodine (I)': '8.0 µg'}
7 Banana, dried, banana chips {'Vitamin A (RAE)': '18.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.02 mg', 'Vitamin B6 (pyridoxine)': '0.44 mg', 'Calcium (Ca)': '19.0 mg', 'Iron (Fe)': '0.7 mg', 'Zinc (Zn)': '0.5 mg', 'Selenium (Se)': '2.0 µg'}
8 Biscuit, sweet, Gjende {'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.12 mg', 'Calcium (Ca)': '14.0 mg', 'Iron (Fe)': '0.9 mg', 'Zinc (Zn)': '0.5 mg', 'Selenium (Se)': '3.0 µg', 'Vitamin B12 (cobalamin)': '0.1 µg', 'Iodine (I)': '0.4 µg'}
9 Blueberries, American, raw {'Vitamin A (RAE)': '4.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.01 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '7.0 mg', 'Iron (Fe)': '0.8 mg', 'Selenium (Se)': '10.0 µg', 'Iodine (I)': '1.0 µg'}
10 Brazil nuts {'Vitamin B6 (pyridoxine)': '0.33 mg', 'Calcium (Ca)': '176.0 mg', 'Iron (Fe)': '2.4 mg', 'Zinc (Zn)': '3.8 mg', 'Selenium (Se)': '225.0 µg'}
11 Bread flour mix, fibre bread, gluten-free, organic, powder, Det Glutenfrie Verksted {'Vitamin B2 (riboflavin)': '0.11 mg', 'Vitamin B6 (pyridoxine)': '0.34 mg', 'Calcium (Ca)': '79.0 mg', 'Iron (Fe)': '4.0 mg', 'Zinc (Zn)': '2.9 mg', 'Iodine (I)': '6.0 µg'}
12 Bread flour mix, no knead bread, gluten-free, organic, powder, Det Glutenfrie Verksted {'Vitamin B2 (riboflavin)': '0.08 mg', 'Vitamin B6 (pyridoxine)': '0.28 mg', 'Calcium (Ca)': '44.0 mg', 'Iron (Fe)': '4.1 mg', 'Zinc (Zn)': '2.6 mg', 'Iodine (I)': '33.0 µg'}
13 Bread, gluten-free, coarse, with soy based beverage, home-made {'Vitamin B2 (riboflavin)': '0.19 mg', 'Vitamin B6 (pyridoxine)': '0.09 mg', 'Calcium (Ca)': '95.0 mg', 'Iron (Fe)': '1.4 mg', 'Zinc (Zn)': '1.3 mg', 'Selenium (Se)': '2.0 µg', 'Vitamin B12 (cobalamin)': '0.1 µg', 'Iodine (I)': '0.6 µg'}
14 Buckwheat flakes {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.15 mg', 'Vitamin B6 (pyridoxine)': '0.58 mg', 'Calcium (Ca)': '33.0 mg', 'Iron (Fe)': '2.2 mg', 'Zinc (Zn)': '2.5 mg', 'Selenium (Se)': '3.0 µg', 'Iodine (I)': '3.0 µg'}
15 Carrot, peas, sweet corn, frozen {'Vitamin A (RAE)': '402.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '21.0 mg', 'Iron (Fe)': '0.5 mg', 'Zinc (Zn)': '0.5 mg'}
16 Cashew nuts {'Vitamin B2 (riboflavin)': '0.06 mg', 'Vitamin B6 (pyridoxine)': '0.42 mg', 'Calcium (Ca)': '37.0 mg', 'Iron (Fe)': '6.7 mg', 'Zinc (Zn)': '5.8 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '11.0 µg'}
17 Cashew nuts, salted, Den lille nøttefabrikken {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.53 mg', 'Calcium (Ca)': '42.0 mg', 'Iron (Fe)': '4.9 mg', 'Zinc (Zn)': '4.9 mg', 'Selenium (Se)': '17.0 µg', 'Iodine (I)': '2.0 µg'}
18 Cashew nuts, salted, Rema 1000 {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.15 mg', 'Vitamin B6 (pyridoxine)': '0.57 mg', 'Calcium (Ca)': '45.0 mg', 'Iron (Fe)': '5.5 mg', 'Zinc (Zn)': '4.8 mg', 'Selenium (Se)': '17.0 µg', 'Iodine (I)': '2.0 µg'}
19 Cocoa powder {'Vitamin A (RAE)': '3.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.15 mg', 'Vitamin B6 (pyridoxine)': '0.07 mg', 'Calcium (Ca)': '105.0 mg', 'Iron (Fe)': '11.0 mg', 'Zinc (Zn)': '10.1 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '3.0 µg'}
20 Cocoa, instant powder, without milk {'Vitamin B2 (riboflavin)': '0.04 mg', 'Vitamin B6 (pyridoxine)': '0.02 mg', 'Calcium (Ca)': '33.0 mg', 'Iron (Fe)': '7.0 mg', 'Zinc (Zn)': '2.3 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '3.0 µg'}
21 Corn and rice flakes, breakfast cereal, gluten-free, special flakes, Semper {'Vitamin B2 (riboflavin)': '2.9 mg', 'Vitamin B6 (pyridoxine)': '2.5 mg', 'Calcium (Ca)': '8.0 mg', 'Iron (Fe)': '12.0 mg', 'Zinc (Zn)': '1.4 mg', 'Vitamin B12 (cobalamin)': '1.3 µg'}
22 Corn and rice flakes, gluten-free, Schär {'Vitamin B2 (riboflavin)': '2.0 mg', 'Vitamin B6 (pyridoxine)': '2.5 mg', 'Calcium (Ca)': '31.0 mg', 'Iron (Fe)': '3.6 mg', 'Zinc (Zn)': '1.3 mg', 'Vitamin B12 (cobalamin)': '1.3 µg'}
23 Corn flakes, gluten-free, Schär {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '2.0 mg', 'Vitamin B6 (pyridoxine)': '2.5 mg', 'Calcium (Ca)': '3.0 mg', 'Iron (Fe)': '0.2 mg', 'Zinc (Zn)': '0.2 mg', 'Vitamin B12 (cobalamin)': '1.3 µg'}
24 Corn flakes, gluten-free, without added sugar, organic, Det Glutenfrie Verksted {'Vitamin A (RAE)': '25.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '35.0 mg', 'Iron (Fe)': '4.7 mg', 'Zinc (Zn)': '4.6 mg', 'Iodine (I)': '5.0 µg'}
25 Crisp bread, Synnøve Grovkrisp sesamfrø og linfrø {'Vitamin B2 (riboflavin)': '0.14 mg', 'Vitamin B6 (pyridoxine)': '0.34 mg', 'Calcium (Ca)': '430.0 mg', 'Iron (Fe)': '4.8 mg', 'Zinc (Zn)': '3.8 mg', 'Selenium (Se)': '15.0 µg', 'Iodine (I)': '2.0 µg'}
26 Crisp bread, rye and spelt, Sigdal helsprøtt {'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.39 mg', 'Calcium (Ca)': '88.0 mg', 'Iron (Fe)': '5.2 mg', 'Zinc (Zn)': '4.7 mg', 'Selenium (Se)': '15.0 µg', 'Iodine (I)': '2.0 µg'}
27 Crisp bread, rye, Husman Sport {'Vitamin B2 (riboflavin)': '0.1 mg', 'Vitamin B6 (pyridoxine)': '0.31 mg', 'Calcium (Ca)': '55.0 mg', 'Iron (Fe)': '3.4 mg', 'Zinc (Zn)': '3.1 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '6.0 µg'}
28 Crisp bread, wholemeal flour, rye, thin, Rugsprø, Finncrisp {'Vitamin B2 (riboflavin)': '0.18 mg', 'Vitamin B6 (pyridoxine)': '0.36 mg', 'Calcium (Ca)': '34.0 mg', 'Iron (Fe)': '4.0 mg', 'Zinc (Zn)': '3.1 mg', 'Selenium (Se)': '24.0 µg', 'Iodine (I)': '113.0 µg'}
29 Cultured, thickened oat product {'Vitamin B2 (riboflavin)': '0.29 mg', 'Calcium (Ca)': '120.0 mg', 'Zinc (Zn)': '0.1 mg', 'Vitamin B12 (cobalamin)': '0.4 µg', 'Iodine (I)': '23.0 µg'}
30 Dates, dried {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.09 mg', 'Vitamin B6 (pyridoxine)': '0.19 mg', 'Calcium (Ca)': '68.0 mg', 'Iron (Fe)': '2.2 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '3.0 µg', 'Iodine (I)': '17.0 µg'}
31 Edamame, soy beans, frozen {'Vitamin A (RAE)': '14.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.27 mg', 'Vitamin B6 (pyridoxine)': '0.14 mg', 'Calcium (Ca)': '60.0 mg', 'Iron (Fe)': '2.1 mg', 'Zinc (Zn)': '1.3 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '2.0 µg'}
32 Elderberries, raw {'Vitamin A (RAE)': '27.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.06 mg', 'Vitamin B6 (pyridoxine)': '0.18 mg', 'Calcium (Ca)': '47.0 mg', 'Iron (Fe)': '0.9 mg', 'Zinc (Zn)': '0.2 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '3.0 µg'}
33 Falafel, chickpeas balls, with Hälsans kök {'Vitamin A (RAE)': '8.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.07 mg', 'Vitamin B6 (pyridoxine)': '0.18 mg', 'Calcium (Ca)': '65.0 mg', 'Iron (Fe)': '2.4 mg', 'Zinc (Zn)': '1.0 mg', 'Selenium (Se)': '24.0 µg'}
34 Figs, dried {'Vitamin A (RAE)': '5.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.04 mg', 'Vitamin B6 (pyridoxine)': '0.35 mg', 'Calcium (Ca)': '191.0 mg', 'Iron (Fe)': '1.4 mg', 'Zinc (Zn)': '0.5 mg', 'Iodine (I)': '2.0 µg'}
35 Flour, gluten-free, coarse, Semper {'Vitamin B2 (riboflavin)': '0.56 mg', 'Vitamin B6 (pyridoxine)': '0.21 mg', 'Calcium (Ca)': '34.0 mg', 'Iron (Fe)': '8.5 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '10.0 µg'}
36 Goji berries, dried {'Vitamin A (RAE)': '26.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.77 mg', 'Vitamin B6 (pyridoxine)': '0.08 mg', 'Calcium (Ca)': '58.0 mg', 'Iron (Fe)': '3.1 mg', 'Zinc (Zn)': '0.8 mg'}
37 Gram flour {'Vitamin A (RAE)': '3.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.17 mg', 'Vitamin B6 (pyridoxine)': '0.45 mg', 'Calcium (Ca)': '58.0 mg', 'Iron (Fe)': '2.6 mg', 'Zinc (Zn)': '1.5 mg', 'Selenium (Se)': '4.0 µg'}
38 Gram flour, organic, Det Glutenfrie Verksted {'Vitamin A (RAE)': '15.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.56 mg', 'Calcium (Ca)': '124.0 mg', 'Iron (Fe)': '6.1 mg', 'Zinc (Zn)': '2.4 mg', 'Selenium (Se)': '4.0 µg', 'Iodine (I)': '9.0 µg'}
39 Grapefruit, raw {'Vitamin A (RAE)': '55.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.02 mg', 'Vitamin B6 (pyridoxine)': '0.35 mg', 'Calcium (Ca)': '26.0 mg', 'Iron (Fe)': '0.1 mg', 'Zinc (Zn)': '0.1 mg', 'Iodine (I)': '3.0 µg'}
40 Hazelnuts {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.38 mg', 'Vitamin B6 (pyridoxine)': '0.21 mg', 'Calcium (Ca)': '140.0 mg', 'Iron (Fe)': '2.7 mg', 'Zinc (Zn)': '2.0 mg', 'Selenium (Se)': '1.0 µg'}
41 Jalapeño, raw {'Vitamin A (RAE)': '47.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.07 mg', 'Vitamin B6 (pyridoxine)': '0.42 mg', 'Calcium (Ca)': '12.0 mg', 'Iron (Fe)': '0.3 mg', 'Zinc (Zn)': '0.1 mg', 'Iodine (I)': '0.4 µg'}
42 Kale, frozen, raw {'Vitamin A (RAE)': '216.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.08 mg', 'Vitamin B6 (pyridoxine)': '0.07 mg', 'Calcium (Ca)': '175.0 mg', 'Iron (Fe)': '0.6 mg', 'Zinc (Zn)': '0.2 mg'}
43 Kale, raw {'Vitamin A (RAE)': '446.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.13 mg', 'Vitamin B6 (pyridoxine)': '0.27 mg', 'Calcium (Ca)': '157.0 mg', 'Iron (Fe)': '1.7 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '2.0 µg'}
44 Leaf beet, mangold, raw {'Vitamin A (RAE)': '304.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.09 mg', 'Vitamin B6 (pyridoxine)': '0.1 mg', 'Calcium (Ca)': '51.0 mg', 'Iron (Fe)': '1.8 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '1.0 µg', 'Iodine (I)': '1.0 µg'}
45 Lentils, black, beluga, uncooked {'Vitamin A (RAE)': '6.0 µg-RE', 'Vitamin B2 (riboflavin)': '1.6 mg', 'Vitamin B6 (pyridoxine)': '0.4 mg', 'Calcium (Ca)': '53.0 mg', 'Iron (Fe)': '5.8 mg', 'Zinc (Zn)': '3.7 mg', 'Selenium (Se)': '63.0 µg'}
46 Lentils, green, puy, uncooked {'Vitamin A (RAE)': '4.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.2 mg', 'Vitamin B6 (pyridoxine)': '0.3 mg', 'Calcium (Ca)': '60.0 mg', 'Iron (Fe)': '8.8 mg', 'Zinc (Zn)': '4.5 mg', 'Selenium (Se)': '9.0 µg'}
47 Lentils, red, canned {'Vitamin A (RAE)': '1.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.03 mg', 'Vitamin B6 (pyridoxine)': '0.06 mg', 'Calcium (Ca)': '25.0 mg', 'Iron (Fe)': '1.6 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '21.0 µg', 'Iodine (I)': '2.0 µg'}
48 Mango, dried {'Vitamin A (RAE)': '103.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.27 mg', 'Vitamin B6 (pyridoxine)': '0.08 mg', 'Calcium (Ca)': '37.0 mg', 'Iron (Fe)': '0.7 mg', 'Zinc (Zn)': '0.4 mg', 'Selenium (Se)': '14.0 µg'}
49 Melon, cantaloupe, raw {'Vitamin A (RAE)': '167.0 µg-RE', 'Vitamin B2 (riboflavin)': '0.02 mg', 'Vitamin B6 (pyridoxine)': '0.07 mg', 'Calcium (Ca)': '9.0 mg', 'Iron (Fe)': '0.2 mg', 'Zinc (Zn)': '0.2 mg', 'Iodine (I)': '4.0 µg'}
50 Millet flakes {'Vitamin B2 (riboflavin)': '0.11 mg', 'Vitamin B6 (pyridoxine)': '0.52 mg', 'Calcium (Ca)': '10.0 mg', 'Iron (Fe)': '6.9 mg', 'Zinc (Zn)': '2.9 mg', 'Selenium (Se)': '2.0 µg', 'Iodine (I)': '3.0 µg'}
....

```