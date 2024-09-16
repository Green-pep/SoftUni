start_interval = int(input())
finish_interval = int(input())
magic_number = int(input())
next_combination = 0
is_found = False

for first_number in range(start_interval, finish_interval + 1):
    for second_number in range(start_interval, finish_interval + 1):
        next_combination += 1
        if first_number + second_number == magic_number:
            print(f"Combination N:{next_combination} ({first_number} + {second_number} = {magic_number})")
            exit()

print(f"{next_combination} combinations - neither equals {magic_number}")