budget = int(input())
season = input()
count_fishermans = int(input())

price_for_boat = 0
discount = 0

if season == "Spring":
    price_for_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_for_boat = 4200
else:
    price_for_boat = 2600

if count_fishermans <= 6:
    discount = price_for_boat * 0.1
elif count_fishermans >= 12:
    discount = price_for_boat * 0.25
else:
    discount = price_for_boat * 0.15

sum_for_boat = price_for_boat - discount

if count_fishermans % 2 and season == "Autumn":
    sum_for_boat *= 0.95

difference = abs(budget - sum_for_boat)

if budget >= sum_for_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")