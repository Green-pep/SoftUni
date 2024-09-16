def list_bracket(n):
    list_with_char = []
    for _ in range(n):
        character = input()
        list_with_char.append(character)
    return list_with_char


def bracket_checker(list_with_char):
    bracket_count = 0
    for char in list_with_char:
        if char == "(":
            if bracket_count > 0:
                return "UNBALANCED"
            bracket_count += 1
        elif char == ")":
            if bracket_count == 0:
                return "UNBALANCED"
            bracket_count -= 1
    return "BALANCED" if bracket_count == 0 else "UNBALANCED"


line_numbers = int(input())
list_with_char = list_bracket(line_numbers)
print(bracket_checker(list_with_char))
