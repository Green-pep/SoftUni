import numpy as np

number_of_orders = int(input())
total_price_order = 0

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())

    if price_per_capsule not in np.arange(0.01, 100.01, 0.01) or days not in range(1,32) or needed_capsule_per_day not in range(1, 2001):
        continue

    order_price = price_per_capsule * days * needed_capsule_per_day
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price_order += order_price

print(f"Total: ${total_price_order:.2f}")
