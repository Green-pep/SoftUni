text_entry = input()
name_for_file = text_entry
name_for_file = name_for_file.split()
new_name = []
print(name_for_file)
for word in name_for_file:
    word = word.lower()
    new_name.append(word)
print(new_name)