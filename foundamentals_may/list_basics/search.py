number_of_strings = int(input())
special_word = input()

list_with_strings = []
special_list = []

for strings in range(number_of_strings):
    string = input()
    list_with_strings.append(string)
    if special_word in string:
        special_list.append(string)

print(list_with_strings)
print(special_list)