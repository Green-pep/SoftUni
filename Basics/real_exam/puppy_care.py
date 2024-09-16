bought_food_in_kilos = int(input())
is_not_adopted = True
eaten_food = 0

while is_not_adopted:
    command = input()
    if command != "Adopted":
        grams_food = int(command)
        eaten_food += grams_food
    else:
        is_not_adopted = False

bought_food_in_grams = bought_food_in_kilos * 1000

if bought_food_in_grams >= eaten_food:
    enough = bought_food_in_grams - eaten_food
    print(f"Food is enough! Leftovers: {enough} grams.")
else:
    not_enough = eaten_food - bought_food_in_grams
    print(f"Food is not enough. You need {not_enough} grams more.")