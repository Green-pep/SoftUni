cats = int(input())
small_cats = 0
big_cats = 0
the_biggest_cats = 0
price_for_kilo_food = 12.45
grams_food = 0

for cats_number in range(cats):
    grams_food_needed = float(input())
    grams_food += grams_food_needed
    if 100 <= grams_food_needed < 200:
        small_cats += 1
    elif 200 <= grams_food_needed < 300:
        big_cats += 1
    elif 200 <= grams_food_needed < 400:
        the_biggest_cats += 1

kilo_food = grams_food / 1000
sum_for_all_food = kilo_food * price_for_kilo_food

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {the_biggest_cats} cats.")
print(f"Price for food per day: {sum_for_all_food:.2f} lv.")
