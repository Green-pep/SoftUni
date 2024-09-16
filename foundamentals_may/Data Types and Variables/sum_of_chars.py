number_of_letters = int(input())
counter_of_characters = 0

for ascii_rows in range(number_of_letters):
    character = input()
    counter_of_characters += ord(character)
print(f"The sum equals: {counter_of_characters}")