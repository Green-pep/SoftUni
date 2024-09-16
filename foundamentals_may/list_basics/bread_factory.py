events = input().split("|")
initial_energy = 100
initial_coins = 100
is_closed = False
gained_energy = 0

for event in events:
    event_or_ingredient, value = event.split("-")
    value = int(value)
    gained_energy = 0
    if event_or_ingredient == "rest":
        if initial_energy + value > 100:
            removed_energy = (initial_energy + value) - 100
            gained_energy += abs(removed_energy - value)
        else:
            initial_energy += value
            gained_energy = value
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event_or_ingredient == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += value
            print(f"You earned {value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= value:
            initial_coins -= value
            print(f"You bought {event_or_ingredient}.")
        else:
            is_closed = True
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
