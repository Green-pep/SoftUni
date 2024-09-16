string = list(input())
parentheses_as_stack = []

for letter in range(len(string)):
    if string[letter] == "(":
        parentheses_as_stack.append(letter)
    elif string[letter] == ")":
        print("".join(string[parentheses_as_stack[-1]:letter + 1]))
        parentheses_as_stack.pop()

