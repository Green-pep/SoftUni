from collections import deque

bee_groups = deque(map(int, (input().split())))
bee_eaters_groups = input().split()
bee_eaters_groups = [int(b) for b in bee_eaters_groups]


while bee_groups and bee_eaters_groups:
    defenders_killed = 7
    current_defender = bee_groups.popleft()
    current_attacker = bee_eaters_groups.pop()
    while current_defender > 0 and current_attacker > 0:
        if current_defender <= current_attacker * 7:
            current_attacker -= current_defender // 7
            current_defender = 0
        else:
            current_defender -= current_attacker * 7
            current_attacker = 0

    if current_defender > 0:
        bee_groups.append(current_defender)
    elif current_attacker > 0:
        bee_eaters_groups.append(current_attacker)

print("The final battle is over!")
if not bee_groups and not bee_eaters_groups:
    print("But no one made it out alive!")

if bee_groups:
    print(f"Bee groups left: {', '.join(map(str, bee_groups))}")
elif bee_eaters_groups:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_groups))}")
