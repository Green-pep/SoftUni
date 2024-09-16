def check_balanced_parentheses(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return len(stack) == 0


expression = input()
if check_balanced_parentheses(expression):
    print("YES")
else:
    print("NO")