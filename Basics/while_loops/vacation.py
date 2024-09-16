needed_money = float(input())
saved_money = float(input())

all_days = 0
spend_days = 0
is_failed = False

while saved_money < needed_money:
    status = input()
    amount = float(input())
    all_days += 1
    if status == "save":
        saved_money += amount
    else:
        spend_days += 1
        if amount >= saved_money:
            saved_money = 0
        else:
            saved_money -= amount
    if spend_days >= 5:
        is_failed = True
        break

if is_failed:
    print(f"You can't save the money.")
    print(f"{all_days}")
else:
    print(f"You saved the money for {all_days} days.")