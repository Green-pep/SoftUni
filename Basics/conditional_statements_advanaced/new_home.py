type_of_flowers = input()
count_of_flowers = int(input())
budget = int(input())

price_roses = 5
price_dahlias = 3.8
price_tulips = 2.8
price_narcissus = 3
price_gladiolus = 2.5
sum_of_all = 0

if type_of_flowers == "Roses":
    sum_of_all = count_of_flowers * price_roses
    if count_of_flowers > 80:
        sum_of_all -= sum_of_all * 0.1
if type_of_flowers == "Dahlias":
    sum_of_all = count_of_flowers * price_dahlias
    if count_of_flowers > 90:
        sum_of_all -= sum_of_all * 0.15
if type_of_flowers == "Tulips":
    sum_of_all = count_of_flowers * price_tulips
    if count_of_flowers > 80:
        sum_of_all -= sum_of_all * 0.15
if type_of_flowers == "Narcissus":
    sum_of_all = count_of_flowers * price_narcissus
    if count_of_flowers < 120:
        sum_of_all += sum_of_all * 0.15
if type_of_flowers == "Gladiolus":
    sum_of_all = count_of_flowers * price_narcissus
    if count_of_flowers < 80:
        sum_of_all += sum_of_all * 0.2

difference = abs(budget - sum_of_all)

if budget > sum_of_all:
    print(f"Hey, you have a great garden with {count_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")