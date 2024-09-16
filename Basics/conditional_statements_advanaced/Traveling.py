budget = float(input())
season = input()

place_for_journey = "Hotel"
price_for_journey = 0
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_for_journey = "Camp"
        price_for_journey = budget * 0.3
    else:
        price_for_journey = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price_for_journey = budget * 0.4
        place_for_journey = "Camp"
    else:
        price_for_journey = budget * 0.8
else:
    destination = "Europe"
    price_for_journey = budget * 0.9

print (f'Somewhere in {destination}')
print(f'{place_for_journey} - {price_for_journey:.2f}')
