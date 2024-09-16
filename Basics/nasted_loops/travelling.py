saved_money = 0
needed_budget = 0
is_enough = False


while True:
    destination = input()
    if destination == "End":
        exit()
    budget = float(input())
    needed_budget += budget
    while needed_budget > saved_money:
        added_money = float(input())
        saved_money += added_money
        if saved_money >= needed_budget:
            print(f"Going to {destination}!")


