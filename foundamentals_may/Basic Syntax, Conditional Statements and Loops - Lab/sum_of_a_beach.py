string = input()
string = string.lower()

search_list = ["sand", "water", "fish", "sun"]
word_counter = 0

for item in search_list:
    if item in string:
        word_count_in_text = string.count(item)
        word_counter += word_count_in_text

print(word_counter)




import re

pattern = r"(?:Sand|Water|Fish|Sun)"

matches = re.findall(pattern, string, re.IGNORECASE)

print(len(matches))