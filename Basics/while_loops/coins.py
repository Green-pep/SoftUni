change = float(input())
change = int(change * 100)
coins_counter = 0

while change > 0:
    if change >= 200:
        change -= 200
        coins_counter += 1
    elif change >= 100:
        change -= 100
        coins_counter += 1
    elif change >= 50:
        change -= 50
        coins_counter += 1
    elif change >= 20:
        change -= 20
        coins_counter += 1
    elif change >= 10:
        change -= 10
        coins_counter += 1
    elif change >= 5:
        change -= 5
        coins_counter += 1
    elif change >= 2:
        change -= 2
        coins_counter += 1
    elif change >= 1:
        change -= 1
        coins_counter += 1

print(coins_counter)