count_of_messages = int(input())

for n in range(count_of_messages):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88 and not number == 86:
        print("GREAT!")
    else:
        print("Bye.")