command = input()
while True:
    if command == "End":
        break
    string = ""
    if command != "SoftUni":
        for i in command:
            string = string + i * 2
        print(string)
    command = input()