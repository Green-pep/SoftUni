count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

price_chicken = count_chicken_menu * 10.35
price_fish = count_fish_menu * 12.40
price_vegan = count_vegan_menu * 8.15

sum_all_food = price_chicken + price_fish + price_vegan
dessert_price = sum_all_food * 0.20
price_delivery = 2.50

final_price = sum_all_food + dessert_price + price_delivery

print(f"{final_price:.2f}")