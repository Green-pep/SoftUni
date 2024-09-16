matrix = [[el for el in map(int,input().split(", ")) if el % 2 == 0] for row in range(int(input()))]
print(matrix)