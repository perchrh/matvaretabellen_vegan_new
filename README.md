Data source: https://www.matvaretabellen.no/api/

cd vegan_foods
curl -O https://www.matvaretabellen.no/api/en/foods.json
curl -O https://www.matvaretabellen.no/api/langual.json


jq . foods.json > foods-formatted.json
