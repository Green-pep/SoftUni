items_for_buy = input().split("|")
budget = int(input())
ticket_for_france = 150
profit = 0
list_with_new_prices = []
new_price_product = 0
profit_per_item = 0


for bought_items in items_for_buy:
    bought_item = bought_items.split("->")
    value_of_the_product = float(bought_item[1])
    new_price_product = 0
    if budget < value_of_the_product:
        continue
    if bought_item[0] == "Clothes":
        if value_of_the_product <= 50.00:
            new_price_product = round(value_of_the_product * 1.40, 2)
            budget -= value_of_the_product
            profit_per_item += new_price_product - value_of_the_product
            profit += new_price_product
            list_with_new_prices.append(new_price_product)
    elif bought_item[0] == "Shoes":
        if value_of_the_product <= 35.00:
            new_price_product = round(value_of_the_product * 1.40, 2)
            budget -= value_of_the_product
            profit_per_item += new_price_product - value_of_the_product
            profit += new_price_product
            list_with_new_prices.append(new_price_product)
    elif bought_item[0] == "Accessories":
        if value_of_the_product <= 20.50:
            new_price_product = round(value_of_the_product * 1.40, 2)
            budget -= value_of_the_product
            profit_per_item += new_price_product - value_of_the_product
            profit += new_price_product
            list_with_new_prices.append(new_price_product)


profit += budget
print(" ".join([f"{list_with_new_prices}" for list_with_new_prices in list_with_new_prices]))
print(f"Profit: {profit_per_item}")
if profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")