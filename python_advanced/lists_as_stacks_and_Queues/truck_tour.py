from collections import deque

petrol_pumps = int(input())
pumps_as_deque = deque()

for pump in range(petrol_pumps):
    added_fuel, distance = input().split()
    pumps_as_deque.append([int(added_fuel), int(distance)])

start_positions = 0
stops = 0

while True:
    if stops > petrol_pumps:
        break
    fuel = 0
    for i in range(petrol_pumps):
        fuel += pumps_as_deque[i][0]
        destination = pumps_as_deque[i][1]
        if fuel < destination:
            pumps_as_deque.rotate(-1)
            start_positions += 1
            stops = 0
            break
        fuel -= destination
        stops += 1
print(start_positions)