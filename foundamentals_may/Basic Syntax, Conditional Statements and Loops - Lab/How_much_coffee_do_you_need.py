command = ""
time_for_coffe = 0
list = ["coding", "dog", "cat", "movie", "CODING", "DOG", "CAT", "MOVIE"]

while command != "END":
    command = input()
    if not command in list:
        continue
    else:
        if command.islower():
            time_for_coffe += 1
        elif command.isupper():
            time_for_coffe += 2
if time_for_coffe > 5:
    print("You need extra sleep")
else:
    print(time_for_coffe)