number_of_strings = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

storing_task_list = []

numbers = [int(input()) for _ in range(number_of_strings)]

command = input()

for number in numbers:
    filter_numbers = ((command == COMMAND_EVEN and number % 2 == 0) or
                      (command == COMMAND_ODD and number % 2 != 0) or
                      (command == COMMAND_NEGATIVE and number < 0) or
                      (command == COMMAND_POSITIVE and number >= 0))
    if filter_numbers:
        storing_task_list.append(number)
print(storing_task_list)