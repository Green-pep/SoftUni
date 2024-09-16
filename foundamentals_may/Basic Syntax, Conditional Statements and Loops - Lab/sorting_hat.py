name = input()
while name != "Welcome!":
    if name == "Voldemort":
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    name = input()
if name == "Voldemort":
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
