times_of_pours = int(input())
max_capacity = 255
capacity_in_tank = 0

for pours in range(times_of_pours):
    liters_water = int(input())
    if capacity_in_tank + liters_water > max_capacity:
        print("Insufficient capacity!")
    else:
        capacity_in_tank += liters_water
print(capacity_in_tank)