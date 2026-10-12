ingredients_had = {"bacon", "green onions", "bell pepper", "eggs", "flour"}
ingredients_needed = {"green onions", "tomato", "parsley", "garlic", "bacon", "chicken_ribs", "flour"}

missing_ingredients = ingredients_needed - ingredients_had
print(missing_ingredients)

required_ingredients_had = ingredients_had & ingredients_needed
print(required_ingredients_had)

extra_ingredients = ingredients_had ^ ingredients_needed
print(extra_ingredients)
