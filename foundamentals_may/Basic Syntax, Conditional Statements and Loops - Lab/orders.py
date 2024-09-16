number_of_orders = int(input())
amount_for_order = 0
amount_for_all_orders = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    amount_for_order = (days * capsules_needed_per_day) * price_per_capsule
    amount_for_all_orders += amount_for_order

    print(f"The price for the coffee is: ${amount_for_order:.2f}")
print(f"Total: ${amount_for_all_orders:.2f}")