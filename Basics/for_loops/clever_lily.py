years = int(input())
price_wash = float(input())
toy_price = int(input())

money = 0
even_birthdays = 0
toys = 0

for birthday in range(1, years + 1):
    if birthday % 2 == 0:
        even_birthdays += 1
        if birthday == 2:
            money += 10 - 1
        else:
            money += (even_birthdays * 10) - 1
    else:
        toys += 1

sum_toys = toys * toy_price
all_savings = money + sum_toys
difference = abs(all_savings - price_wash)

if all_savings >= price_wash:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
