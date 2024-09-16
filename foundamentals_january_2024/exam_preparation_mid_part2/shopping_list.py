list_with_products = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break
    new_command = command.split()
    if new_command[0] == "Urgent":
        if new_command[1] in list_with_products:
            continue
        list_with_products.insert(0, new_command[1])
    elif new_command[0] == "Unnecessary":
        if not new_command[1] in list_with_products:
            continue
        list_with_products.remove(new_command[1])
    elif new_command[0] == "Correct":
        if not new_command[1] in list_with_products:
            continue
        old_item = list_with_products.index(new_command[1])
        list_with_products[old_item] = new_command[2]
    elif new_command[0] == "Rearrange":
        if not new_command[1] in list_with_products:
            continue
        list_with_products.remove(new_command[1])
        list_with_products.append(new_command[1])

print(", ".join(list_with_products))
