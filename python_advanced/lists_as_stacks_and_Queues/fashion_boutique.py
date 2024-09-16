clothes_as_stack = list(int(number) for number in input().split())
capacity_of_rack = int(input())

rack = 0

while clothes_as_stack:
    rack += 1
    current_rack_capacity = capacity_of_rack
    while clothes_as_stack and clothes_as_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_as_stack.pop()

print(rack)


