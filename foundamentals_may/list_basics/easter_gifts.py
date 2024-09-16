gifts = input().split()
list_command = []
index_for_replacement = 0


while True:
    list_command = input().split()
    if list_command[0] == "No" and list_command[1] == "Money":
        break
    command = list_command[0]

    if command == "OutOfStock":
        for removing in gifts:
            if removing == list_command[1]:
                index_for_replacement = gifts.index(removing)
                gifts[index_for_replacement] = "None"

    elif command == "Required":
        index_for_replacement = int(list_command[2])
        if index_for_replacement > len(gifts) - 1:
            continue
        gifts[index_for_replacement] = list_command[1]

    elif command == "JustInCase":
        gifts[-1] = list_command[1]

for elements in gifts:
    if elements == "None":
         gifts.remove(elements)

final_string_result = " ".join(gifts)
print(final_string_result)
