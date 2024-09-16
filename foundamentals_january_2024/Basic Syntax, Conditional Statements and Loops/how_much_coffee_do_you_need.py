needed_coffee = 0
events_list = ["coding", "dog", "cat", "movie"]

while True:
    command = input()
    if command == "END":
        break
    if command.islower():
        if command.lower() in events_list:
            needed_coffee += 1
    else:
        if command.lower() in events_list:
            needed_coffee += 2
if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)
