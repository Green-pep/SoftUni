tail_string = input()
body_string = input()
head_string = input()

list = [tail_string, body_string, head_string]

list[0], list[2] = list[2], list[0]

print(list)