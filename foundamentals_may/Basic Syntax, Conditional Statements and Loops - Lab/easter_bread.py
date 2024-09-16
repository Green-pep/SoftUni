budget = float(input())
price_for_kilo_flour = float(input())

price_for_pack_eggs = price_for_kilo_flour * 0.75
price_for_milk = price_for_kilo_flour + price_for_kilo_flour * 0.25
price_for_recipe_for_one_bread = price_for_milk * 0.25 + price_for_pack_eggs + price_for_kilo_flour
cooked_bread = 0
painted_eggs = 0

while budget >= price_for_recipe_for_one_bread:
    cooked_bread += 1
    painted_eggs += 3
    budget -= price_for_recipe_for_one_bread
    if cooked_bread % 3 == 0:
        painted_eggs -= max(0, cooked_bread - 2)
print(f"You made {cooked_bread} loaves of Easter bread! Now you have {painted_eggs} eggs anц {budget:.2f}BGN left.")