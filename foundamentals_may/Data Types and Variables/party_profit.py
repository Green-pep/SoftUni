import math

group_size = int(input())
days_of_adventure = int(input())
earned_coins = 0


for days_in_row in range(1, days_of_adventure + 1):
    if days_in_row % 10 == 0:
        group_size -= 2
    if days_in_row % 15 == 0:
        group_size += 5
    earned_coins += 50
    earned_coins -= 2 * group_size
    if days_in_row % 3 == 0:
        earned_coins -= group_size * 3
    if days_in_row % 5 == 0:
        earned_coins += group_size * 20
        if days_in_row % 3 == 0:
            earned_coins -= group_size * 2

coins_for_companion = math.floor(earned_coins / group_size)

print(f"{group_size} companions received {coins_for_companion} coins each.")