month_for_rent = input()
number_of_days = int(input())
price_studio = 0
price_apartment = 0

if month_for_rent == "May" or month_for_rent == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < number_of_days < 14:
        price_studio *= 0.95
    elif number_of_days > 14:
        price_studio *= 0.7
        price_apartment *= 0.9
elif month_for_rent == "June" or month_for_rent == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if number_of_days > 14:
        price_studio *= 0.8
        price_apartment *= 0.9
elif month_for_rent == "July" or month_for_rent == "August":
    price_studio = 76
    price_apartment = 77
    if number_of_days > 14:
        price_apartment *= 0.9

sum_for_rent_studio = price_studio * number_of_days
sum_for_rent_apartment = price_apartment * number_of_days

print(f"Apartment: {sum_for_rent_apartment:.2f} lv.")
print(f'Studio: {sum_for_rent_studio:.2f} lv.')
