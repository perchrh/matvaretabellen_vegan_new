from vegan_foods.food import Food, Nutrient

# Create a Nutrient object
nutrient = Nutrient(
    id="PROT",
    name="Protein",
    quantity=10.0,
    unit="g"
)

# Create a Food object
food = Food(
    id="123",
    name="Test Food",
    group_id="6.1",
    group_name="Vegetables",
    nutrients={"123": nutrient}
)

# Create a food dictionary for testing from_dict
food_dict = {
    'foodId': '456',
    'foodName': 'Another Test Food',
    'foodGroupId': '12.3',
    'foodGroupName': 'Fruits',
    'constituents': {
        'PROT': {
            'nutrientId': '123',
            'euroFirId': 'PROT',
            'nutrientName': 'Protein',
            'quantity': 15.0,
            'unit': 'g'
        },
        'FAT': {
            'nutrientId': '456',
            'euroFirId': 'FAT',
            'nutrientName': 'Fat',
            'quantity': 5.0,
            'unit': 'g'
        }
    }
}

# Convert dictionary to Food object
food2 = Food.from_dict(food_dict)
print("Dictionary converted to Food object:")
print(f"id: {food2.id}")
print(f"name: {food2.name}")
print(f"group_id: {food2.group_id}")
print(f"group_name: {food2.group_name}")
print(f"nutrients: {food2.nutrients}")

# Verify that the Food object has the correct values
assert food2.id == '456'
assert food2.name == 'Another Test Food'
assert food2.group_id == '12.3'
assert food2.group_name == 'Fruits'
assert len(food2.nutrients) == 2

# Verify that the Nutrient objects have the correct values
assert 'PROT' in food2.nutrients
assert 'FAT' in food2.nutrients

nutrient_123 = food2.nutrients['PROT']
assert nutrient_123.id == 'PROT'
assert nutrient_123.quantity == 15.0
assert nutrient_123.unit == 'g'

nutrient_456 = food2.nutrients['FAT']
assert nutrient_456.id == 'FAT'
assert nutrient_456.quantity == 5.0
assert nutrient_456.unit == 'g'

print("\nAll assertions passed! The Food and Nutrient classes are working correctly.")
