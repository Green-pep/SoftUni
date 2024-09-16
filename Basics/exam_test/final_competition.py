count_dancers = int(input())
count_points = float(input())
season = input()
place_of_competition = input()

winning_money = 0

if place_of_competition == "Bulgaria":
    winning_money = count_points * count_dancers
    if season == "summer":
        winning_money *= 0.95
    else:
        winning_money *= 0.92
else:
    winning_money = count_points * count_dancers
    winning_money += winning_money * 0.50
    if season == "summer":
        winning_money *= 0.90
    else:
        winning_money *= 0.85

charity_money = winning_money * 0.75
left_money = winning_money * 0.25
money_for_dancer = left_money / count_dancers

print(f"Charity - {charity_money:.2f}")
print(f"Money per dancer - {money_for_dancer:.2f}")
