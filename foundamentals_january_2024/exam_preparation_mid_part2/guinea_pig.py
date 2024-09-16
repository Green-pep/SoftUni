quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
guinea_weight_in_kilograms = float(input())

quantity_food_in_grams = int(quantity_food_in_kilograms * 1000)
quantity_hay_in_grams = int(quantity_hay_in_kilograms * 1000)
quantity_cover_in_grams = int(quantity_cover_in_kilograms * 1000)
guinea_weight_in_grams = int(guinea_weight_in_kilograms * 1000)

is_not_enough = False

needed_food = 300

for day in range(1, 30 + 1):
    quantity_food_in_grams -= needed_food
    needed_hay = quantity_food_in_grams * 0.05
    needed_cover = guinea_weight_in_grams / 3
    if quantity_food_in_grams <= needed_food or quantity_hay_in_grams <= needed_hay or quantity_cover_in_grams <= needed_cover:
        is_not_enough = True
        break
    if day % 2 == 0:
        quantity_hay_in_grams -= needed_hay
    if day % 3 == 0:
        quantity_cover_in_grams -= needed_cover

if is_not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_grams / 1000:.2f}, Hay: {quantity_hay_in_grams / 1000:.2f}, Cover: {quantity_cover_in_grams / 1000:.2f}.")
