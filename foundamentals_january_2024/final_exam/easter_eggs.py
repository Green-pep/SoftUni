import re

string = input()
sum_eggs = 0
pattern = "([@#]+[a-z]{3,}[@#]+)[^a-zA-Z\d]*?(/+\d+/+)"
list_with_matches = {}

matches = re.findall(pattern, string)
for match in matches:

    color = match[0]
    color = color.replace("@", "")
    color = color.replace("#", "")

    amount = match[1]
    amount = int(amount.replace("/",""))
    print(f"You found {amount} {color} eggs!")