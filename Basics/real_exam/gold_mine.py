count_of_locations = int(input())
days_of_yield = 0
average_profit = 0
yield_gold = 0

for locations in range(count_of_locations):
    average_profit = 0
    yield_gold = 0
    days_of_yield = 0
    average_profit += int(input())
    days_of_yield += int(input())
    for days_in_location in range(days_of_yield):
        yield_gold += int(input())
    average_yield_gold = yield_gold / days_of_yield
    if average_yield_gold >= average_profit:
        print(f"Good job! Average gold per day: {average_yield_gold:.2f}.")
    else:
        difference = average_profit - average_yield_gold
        print(f"You need {difference:.2f} gold.")