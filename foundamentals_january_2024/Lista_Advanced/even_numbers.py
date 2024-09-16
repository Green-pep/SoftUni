numbers = list(map(int, input().split(", ")))

checked_numbers = list(map(lambda x: x if numbers[x] % 2 == 0 else "no", range((len(numbers)))))
filtered_numbers = list(filter(lambda f: f != "no", checked_numbers))
print(filtered_numbers)