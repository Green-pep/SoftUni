start_from_character = int(input())
end_from_character = int(input())
storage_character = ""

for char in range(start_from_character, end_from_character + 1):
    storage_character += " " + chr(char)
print(storage_character)