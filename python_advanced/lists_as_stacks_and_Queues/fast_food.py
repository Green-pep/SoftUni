from collections import deque

quantity_of_food = int(input())
quantity_food_orders = deque(map(int,input().split()))
print(max(quantity_food_orders))

while True:
    if len(quantity_food_orders) == 0:
        print("Orders complete")
        break

    first_order = quantity_food_orders[0]
    if first_order <= quantity_of_food:
        quantity_food_orders.popleft()
        quantity_of_food -= first_order
    else:
        print(f"Orders left:", *quantity_food_orders)
        break
