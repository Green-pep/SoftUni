number = input()

list = number.split(" ")

for i in range(0, len(list)):

     list[i] = -int(list[i])

print(list)