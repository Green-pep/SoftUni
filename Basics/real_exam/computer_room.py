month = input()
count_of_playing_hours = int(input())
number_of_peoples = int(input())
day_or_night = input()

price_for_person = 0

if month == "march" or month == "april" or month == "may":
    if day_or_night == "day":
        price_for_person = 10.50
    else:
        price_for_person = 8.40
else:
    if day_or_night == "day":
        price_for_person = 12.60
    else:
        price_for_person = 10.20
if number_of_peoples >= 4:
    price_for_person *= 0.9

if count_of_playing_hours >= 5:
    price_for_person *= 0.5

sum_of_all = (price_for_person * number_of_peoples) * count_of_playing_hours
print(f"Price per person for one hour: {price_for_person:.2f}")
print(f"Total cost of the visit: {sum_of_all:.2f}")