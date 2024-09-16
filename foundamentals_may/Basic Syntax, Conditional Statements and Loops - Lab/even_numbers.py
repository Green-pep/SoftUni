n = int(input())

for rows in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")