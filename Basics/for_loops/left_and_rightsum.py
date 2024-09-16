from math import fabs
n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    number_for_left = float(input())
    left_sum += number_for_left
for _ in range(n):
    number_for_right = float(input())
    right_sum += number_for_right

if left_sum == right_sum:
    print(f"Yes, sum = %d" % left_sum)
else:
    print(f"No, diff = %d" % fabs(right_sum - left_sum))