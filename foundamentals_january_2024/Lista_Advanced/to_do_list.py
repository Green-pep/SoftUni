task_list = []

while True:
    command = input()
    if command == "End":
        break

    task_list.append(command)
    new_list = sorted(task_list, key=lambda x: int(x.split("-")[0]))

new_list = [index.split("-")[1] for index in new_list]
print(new_list)