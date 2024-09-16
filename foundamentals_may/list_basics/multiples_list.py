factor_number = int(input())
count_number = int(input())

start_number = factor_number
end_number = factor_number * count_number

storing_list = []

for numbers in range(start_number, end_number + 1, factor_number):
    storing_list.append(numbers)
print(storing_list)