counter = 0

while True:
    text = input()
    if text == "NoMoreMoney":
        break

    amount_for_deposit = float(text)

    if amount_for_deposit >= 0:
        counter += amount_for_deposit
        print(f"Increase: {amount_for_deposit:.2f}")

    else:
        print("Invalid operation!")
        break

print(f"Total: {counter:.2f}")