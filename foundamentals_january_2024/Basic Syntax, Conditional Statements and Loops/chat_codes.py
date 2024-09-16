count_massages = int(input())
for massages in range(count_massages):
    number_massage = int(input())
    if number_massage == 88:
        print("Hello")
    elif number_massage == 86:
        print("How are you?")
    elif number_massage < 88 and not number_massage == 86:
        print("GREAT!")
    else:
        print("Bye.")