from collections import deque

quantity_water = int(input())
queue = deque([])

while True:
    name_for_queue = input()
    if name_for_queue == "Start":
        break
    queue.append(name_for_queue)

while True:
    command = input()
    if command == "End":
        break
    if command.isdigit():
        person_name = queue.popleft()
        command = int(command)

        if command <= quantity_water:
            print(f"{person_name} got water")
            quantity_water -= command
        else:
            print(f"{person_name} must wait")

    else:
        command = command.split()
        quantity_water += int(command[1])

print(f"{quantity_water} liters left")

