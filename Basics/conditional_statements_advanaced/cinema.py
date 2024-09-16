type_of_cinema = input()
rows_in_cinema = int(input())
columns_in_cinema = int(input())

count_of_places = rows_in_cinema * columns_in_cinema
price_per_ticket = 0

if type_of_cinema == "Premiere":
    price_per_ticket = 12
if type_of_cinema == "Normal":
    price_per_ticket = 7.5
if type_of_cinema == "Discount":
    price_per_ticket = 5

all_winnings = count_of_places * price_per_ticket

print(f'{all_winnings:.2f} leva')
