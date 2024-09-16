number_of_strings = int(input())
bad_charecters = [",", ".", "_"]

for strings in range(number_of_strings):
    string = input()
    is_pure = True
    for char in string:
        if char in bad_charecters:
            is_pure = False
            break
    if not is_pure:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
