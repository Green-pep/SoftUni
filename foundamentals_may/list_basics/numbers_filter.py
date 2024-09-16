number_of_strings = int(input())

list_with_numbers = []
storing_task_list = []

for numbers in range(number_of_strings):
    number = int(input())
    list_with_numbers.append(number)

command = input()

if command == "even":
    for number in list_with_numbers:
        if number % 2 == 0:
            storing_task_list.append(number)
elif command == "odd":
    for number in list_with_numbers:
        if number % 2 != 0:
            storing_task_list.append(number)
elif command == "negative":
    for number in list_with_numbers:
        if number < 0:
            storing_task_list.append(number)
else:
    for number in list_with_numbers:
        if number >= 0:
            storing_task_list.append(number)
print(storing_task_list)