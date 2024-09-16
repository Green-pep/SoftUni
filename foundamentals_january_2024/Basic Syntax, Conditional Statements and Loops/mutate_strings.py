first_string = input()
second_string = input()

unique_string = ""
changed_string = ""

for letter in range(len(first_string)):
    first_half_string = first_string[letter + 1:]
    second_string_half = second_string[:letter + 1]
    changed_string = second_string_half + first_half_string
    if changed_string != unique_string:
        unique_string = changed_string
        print(unique_string)