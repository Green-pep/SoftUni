needed_jump = int(input())
high_of_jump = needed_jump - 30
success = True
count_of_jumps = 0
count_of_fails = 0
jump_try = 0

while jump_try <= high_of_jump:
    jump_try = int(input())
    if jump_try >= needed_jump:
        count_of_fails += 1
        if count_of_fails == 3:
            success = False
            continue
    count_of_fails = 0
    count_of_jumps += 1
    high_of_jump += 5
    if not success:
        break

if not success:
    print(f"Tihomir failed at {high_of_jump}cm after {count_of_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {needed_jump}cm after {count_of_jumps} jumps.")
