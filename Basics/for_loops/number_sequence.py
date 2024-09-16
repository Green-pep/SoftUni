count_numbers = int(input())
list = []

for _ in range(count_numbers):
    numbers = int(input())
    list.append(numbers)

print("Max number:",max(list))
print("Min number:",min(list))
