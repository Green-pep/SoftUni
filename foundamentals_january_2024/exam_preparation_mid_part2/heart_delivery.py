def split_text(input_text):
    text = input_text.split("@")
    neighborhood_numbers = [int(numbers) for numbers in text]
    return neighborhood_numbers


def cupids_love(neighborhood_numbers):
    last_position_index = 0
    while True:
        command = input()
        if command == "Love!":
            break 
        new_command = command.split()
        position_of_cupid = last_position_index + int(new_command[1])
        last_position_index = position_of_cupid
        if last_position_index > len(neighborhood_numbers) - 1:
            last_position_index = 0
        if neighborhood_numbers[last_position_index] == 0:
            print(f"Place {last_position_index} already had Valentine's day.")
        else:
            neighborhood_numbers[last_position_index] -= 2
            if neighborhood_numbers[last_position_index] <= 0:
                print(f"Place {last_position_index} has Valentine's day.")
                if neighborhood_numbers[last_position_index] < 0:
                    neighborhood_numbers[last_position_index] = 0
    return last_position_index


def is_all_valentine(neighborhood_numbers, last_position_index):
    are_all_valentine = True
    failed_houses = 0
    for numbers in neighborhood_numbers:
        if numbers > 0:
            failed_houses += 1
            are_all_valentine = False
    print(f"Cupid's last position was {last_position_index}.")
    if are_all_valentine:
        print("Mission was successful.")
    else:
        print(f"Cupid has failed {failed_houses} places.")


number_text = input()
numbers_of_neighborhood = split_text(number_text)
position = cupids_love(numbers_of_neighborhood)
is_all_valentine(numbers_of_neighborhood, position)
