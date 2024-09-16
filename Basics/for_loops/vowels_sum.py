word = input()

sum_letters = 0

for i in range(0,len(word)):
    if word[i] == "a":
        sum_letters += 1
    elif word[i] == "e":
        sum_letters += 2
    elif word[i] == "i":
        sum_letters += 3
    elif word[i] == "o":
        sum_letters += 4
    elif word[i] == "u":
        sum_letters += 5
print(sum_letters)
