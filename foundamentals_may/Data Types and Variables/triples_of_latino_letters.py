number_of_characters = int(input())
for a in range(0, number_of_characters):
    for b in range(0, number_of_characters):
        for c in range(0, number_of_characters):
            print(f'{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}')