first_string = input()
second_string = input()
last_print_combination = first_string

for char_index in range(len(first_string)):
    left_side = second_string[:char_index + 1]
    right_side = first_string[char_index + 1:]
    combination = left_side + right_side
    if combination == last_print_combination:
        continue
    print(combination)
    last_print_combination = combination
    