collection_of_items = input().split("|")
budget = int(input())
sold_clothes_prices = []
true_profit = 0

for collection in collection_of_items:
    type_of_clothes, price = collection.split("->")
    price = float(price)
    is_bought = False
    if type_of_clothes == "Clothes":
        if price <= 50:
            is_bought = True
    elif type_of_clothes == "Shoes":
        if price <= 35:
            is_bought = True
    elif type_of_clothes == "Accessories":
        if price <= 35:
            is_bought = True
    if is_bought:
        if budget >= price:
            budget -= price
            sold_cloth_price = price * 1.40
            true_profit += sold_cloth_price - price
            sold_clothes_prices.append(sold_cloth_price)

end_result_of_money = budget + sum(sold_clothes_prices)


print(" ".join([f"{sold_clothes_prices:.2f}" for sold_clothes_prices in sold_clothes_prices]))
print(f"Profit: {true_profit:.2f}")
if end_result_of_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")