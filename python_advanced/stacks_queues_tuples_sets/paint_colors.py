from collections import deque
from math import ceil

string = deque(input().split())

main_colors = ["red", "yellow", "blue"]
second_colors = {"orange": ["red", "yellow"],
                 "purple": ["red", "blue"],
                 "green": ["blue", "yellow"]
                 }
made_colors = []

while string:
    first_substring = string.popleft()
    second_substring = string.pop() if string else ""

    for color in (first_substring + second_substring, second_substring + first_substring):
        if color in main_colors or color in second_colors:
            made_colors.append(color)
            break
    else:
        position_of_the_new_substring = ceil(len(string) / 2)
        if first_substring != "":
            string.insert(position_of_the_new_substring,first_substring[:-1])
        if second_substring != "":
            string.insert(position_of_the_new_substring, second_substring[:-1])

for color in made_colors:
    if color in second_colors:
        for element in second_colors[color]:
            if element not in made_colors:
                made_colors.remove(color)
                break

print(made_colors)