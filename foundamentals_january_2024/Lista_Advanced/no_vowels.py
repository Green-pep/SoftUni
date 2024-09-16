text = [i for i in input()]
removing_vowels = ['a', 'o', 'u', 'e', 'i']
sorted_list = []

for i in text:
    if i.lower() not in removing_vowels:
        sorted_list.append(i)

print("".join(sorted_list))