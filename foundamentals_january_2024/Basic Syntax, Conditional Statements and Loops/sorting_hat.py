is_voldemort = False
while True:
    name = input()
    if name == "Voldemort":
        is_voldemort = True
        break
    elif name == "Welcome!":
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")

if is_voldemort:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
