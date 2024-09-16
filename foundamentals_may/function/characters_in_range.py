def ascii_table_range(first_char, second_char):
    first_char = ord(first_char)
    second_char = ord(second_char)
    list_with_characters = []
    for char in range(first_char + 1, second_char):
        new_symbol = chr(char)
        list_with_characters.append(new_symbol)
    return " ".join(list_with_characters)


first_character = input()
second_character = input()

print(ascii_table_range(first_character, second_character))
