roles = int(input())
stack = []
commands_as_dict = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None
}


for role in range(roles):
    command = input().split()
    commands_as_dict[command[0]](*command[1:])

print(*reversed(stack), sep= ", ")
