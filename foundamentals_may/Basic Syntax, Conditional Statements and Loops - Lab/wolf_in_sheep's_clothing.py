string = input()
count_number_of_group = 0

if string.split()[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    splitting_string = string.split(", ")
    for i in range(len(splitting_string) - 1, -1, -1):
        if splitting_string[i] == "sheep":
            count_number_of_group += 1
        if splitting_string[i] == "wolf":
            print(f"Oi! Sheep number {count_number_of_group}! You are about to be eaten by a wolf!")
            break
