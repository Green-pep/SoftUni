number_list = input().split()
numbers_for_removing = int(input())
smallest_number = 0
int_list = []

for number in number_list:
    int_list.append(int(number))

for numbers in range(numbers_for_removing):
    int_list.remove(min(int_list))
print(*int_list, sep=", ")
