string = input()

while True:
    decrypting_command = input().split()

    command = decrypting_command[0]
    if command == "Finish":
        break
    if command == "Replace":
        current_char = decrypting_command[1]
        new_char = decrypting_command[2]
        string = string.replace(current_char, new_char)
        print(string)

    elif command == "Cut":
        start_index = int(decrypting_command[1])
        final_index = int(decrypting_command[2])
        if 0 <= start_index < len(string) and 0 < final_index < len(string):
            cut_string = string[start_index:final_index + 1]
            new_string = string.replace(cut_string, "")
            print(new_string)
        else:
            print("Invalid indices!")
    elif command == "Make":
        case = decrypting_command[1]
        if case == "Upper":
            string = string.upper()
        else:
            string = string.lower()
        print(string)
    elif command == "Check":
        check_string = decrypting_command[1]
        if check_string in string:
            print(f"Message contains {check_string}")
        else:
            print(f"Message doesn't contain {check_string}")
    elif command == "Sum":
        start_index = int(decrypting_command[1])
        final_index = int(decrypting_command[2])
        sum_digits = 0
        if 0 <= start_index < len(string) and 0 < final_index < len(string):
            iter_string = string[start_index:final_index + 1]
            for letter in iter_string:
                sum_digits += ord(letter)
            print(sum_digits)
        else:
            print("Invalid indices!")

