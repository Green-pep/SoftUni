string = input()
capital_letters = []
for index, char in enumerate(string):
    if char.isupper():
        capital_letters.append(index)
print(capital_letters)