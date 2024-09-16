number_of_strings = int(input())

for n in range(number_of_strings):
    string = input()
    if string.count(',') or string.count('.') or string.count('_'):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")