import sys

n = int(input())
max_num = -sys.maxsize
sum_num = 0

for checker in range(n):
    number = int(input())

    if number > max_num:
        max_num = number
    sum_num += number

if max_num == sum_num - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    diff = abs(max_num - (sum_num - max_num))
    print(f"Diff = {diff}")
