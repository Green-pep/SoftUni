needed_height = int(input())
record_height = 0
jumps_number = 0
unsuccessful_jumps = 0
starting_height = needed_height - 30

while record_height < needed_height:
    jump_height = int(input())
    if record_height > needed_height:
        break

    if jump_height <= starting_height:
        jumps_number += 1
        unsuccessful_jumps += 1
        if unsuccessful_jumps == 3:
            fail_height = starting_height
            break

    else:
        starting_height += 5
        jumps_number += 1
        unsuccessful_jumps = 0
        record_height = jump_height
if record_height > needed_height:
    print(f'Tihomir succeeded, he jumped over {needed_height}cm after {jumps_number} jumps.')
else:
    print(f'Tihomir failed at {starting_height}cm after {jumps_number} jumps.')