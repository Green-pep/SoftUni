def order_calculator(product, quantity):
    dictionary = {"coffee": "1.50", "water": "1.00", "coke": "1.40", "snacks": "2.00"}
    return float(dictionary.get(product)) * quantity


type_of_product = input()
want_quantity = int(input())

print(f"{order_calculator(type_of_product, want_quantity):.2f}")

