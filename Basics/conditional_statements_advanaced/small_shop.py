product_type = input()
city = input()
quantity_of_product = float(input())
price = 0

if city == "Sofia":
    if product_type == "coffee":
        price += 0.50
    elif product_type == "water":
        price += 0.80
    elif product_type == "beer":
        price += 1.20
    elif product_type == "sweets":
        price += 1.45
    elif product_type == "peanuts":
        price += 1.60
elif city == "Plovdiv":
    if product_type == "coffee":
        price += 0.40
    elif product_type == "water":
        price += 0.70
    elif product_type == "beer":
        price += 1.15
    elif product_type == "sweets":
        price += 1.30
    elif product_type == "peanuts":
        price += 1.50
elif city == "Varna":
    if product_type == "coffee":
        price += 0.45
    elif product_type == "water":
        price += 0.70
    elif product_type == "beer":
        price += 1.10
    elif product_type == "sweets":
        price += 1.35
    elif product_type == "peanuts":
        price += 1.55

sum_of_all = quantity_of_product * price

print(round(sum_of_all,4))