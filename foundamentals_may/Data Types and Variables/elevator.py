import math
number_of_people = int(input())
capacity = int(input())

needed_courses = math.ceil(number_of_people / capacity)

print(needed_courses)