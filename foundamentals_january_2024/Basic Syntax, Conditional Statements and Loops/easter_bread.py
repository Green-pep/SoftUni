budget = float(input())
price_for_kilo_of_flour = float(input())

price_for_one_pack_of_eggs = price_for_kilo_of_flour * 0.75
price_for_one_litter_of_milk = price_for_kilo_of_flour * 1.25

recipe_for_one_loaf = price_for_one_pack_of_eggs + price_for_kilo_of_flour + (price_for_one_litter_of_milk * 0.25)

current_bread = 0
colored_eggs = 0

while budget >= recipe_for_one_loaf:
    budget -= recipe_for_one_loaf
    current_bread += 1
    colored_eggs += 3
    if current_bread % 3 == 0:
        colored_eggs -= max(0, current_bread - 2)
print(f"You made {current_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
