energy = int(input())
distance = 0
won_battles = 0
is_enough_energy = True

while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    if distance > energy:
        is_enough_energy = False
        break
    won_battles += 1
    energy -= distance
    if won_battles % 3 == 0:
        energy += won_battles

if is_enough_energy:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")