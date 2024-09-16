sea_excursion = int(input())
mountain_excursion = int(input())

sum_for_all_excursions = sea_excursion + mountain_excursion
left_sea_excursion = sea_excursion
left_mountain_excursion = mountain_excursion
profit = 0

while sum_for_all_excursions > 0:
    type_of_excursion = input()
    if type_of_excursion == "Stop":
        break
    elif type_of_excursion == "sea":
        if left_sea_excursion == 0:
            continue
        else:
            left_sea_excursion -= 1
            profit += 680
            sum_for_all_excursions -= 1
    elif type_of_excursion == "mountain":
        if left_mountain_excursion == 0:
            continue
        else:
            mountain_excursion -= 1
            profit += 499
            sum_for_all_excursions -= 1

if sum_for_all_excursions <= 0:
    print("Good job! Everything is sold.")
    print(f"Profit: {profit} leva.")
else:
    print(f"Profit: {profit} leva.")
