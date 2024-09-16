steps_counter = 0

while steps_counter < 10000:
    command = input()
    if command != "Going home":
        steps = int(command)
        steps_counter += steps
        continue
    else:
        steps_to_home = int(input())
        steps_counter += steps_to_home
        break

difference = abs(steps_counter - 10000)
if steps_counter >= 10000:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
