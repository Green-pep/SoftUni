number_of_days = int(input())
kind_of_room = input()
feedback = input()

price_room_for_one_person = 18
price_apartment = 25
price_president_apartment = 35
nights_for_rent = number_of_days - 1
price_for_rent = 0
price_with_discount = 0

if kind_of_room == "apartment":
    if number_of_days < 10:
        price_for_rent = price_apartment * nights_for_rent
        price_with_discount = price_for_rent * 0.7
    elif number_of_days > 15:
        price_for_rent = price_apartment * nights_for_rent
        price_with_discount = price_for_rent * 0.50
    else:
        price_for_rent = price_apartment * nights_for_rent
        price_with_discount = price_for_rent * 0.65
elif kind_of_room == "president apartment":
    if number_of_days < 10:
        price_for_rent = price_president_apartment * nights_for_rent
        price_with_discount = price_for_rent * 0.9
    elif number_of_days > 15:
        price_for_rent = price_president_apartment * nights_for_rent
        price_with_discount = price_for_rent * 0.80
    else:
        price_for_rent = price_president_apartment * nights_for_rent
        price_with_discount = price_for_rent * 0.85
elif kind_of_room == "room for one person":
    price_with_discount = price_room_for_one_person * nights_for_rent

if feedback == "positive":
    price_with_discount += (price_with_discount * 0.25)
else:
    price_with_discount -= (price_with_discount * 0.1)

print(f"{price_with_discount:.2f}")

