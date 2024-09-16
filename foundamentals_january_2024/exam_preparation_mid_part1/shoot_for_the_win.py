numbers = input().split(" ")
numbers = [int(number) for number in numbers]

list_with_new_numbers = []
target_int = 0
count_of_shot_targets = 0

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    target_int = numbers[index]
    for number in numbers:
        number -= target_int
        list_with_new_numbers.append(number)

 