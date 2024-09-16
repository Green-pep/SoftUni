gifts = input().split()

while True:
    command_input = input()
    if command_input == "No Money":
        break

    list_command = command_input.split()
    command = list_command[0]

    if command == "OutOfStock":
        gift_to_remove = list_command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"

    elif command == "Required":
        index = int(list_command[2])
        if 0 <= index < len(gifts):
            gifts[index] = list_command[1]

    elif command == "JustInCase":
        gifts[-1] = list_command[1]

new_gifts = []
for gift in gifts:
    if gift != "None":
        new_gifts.append(gift)

print(" ".join(new_gifts))
