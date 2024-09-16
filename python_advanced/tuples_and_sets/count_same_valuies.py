numbers = tuple(float(x) for x in input().split())


counter = {}
for num in numbers:
    counter[num] = numbers.count(num)

for key, value in counter.items():
    print(f"{key:.1f} - {value} times")