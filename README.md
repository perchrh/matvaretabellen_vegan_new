Data source: https://www.matvaretabellen.no/api/

load the data
cd vegan_foods
curl -O https://www.matvaretabellen.no/api/en/foods.json
curl -O https://www.matvaretabellen.no/api/langual.json

run main.py

Uses a type of dominant sorting to find the best foods in terms of nutrients that are least common in foods for vegans