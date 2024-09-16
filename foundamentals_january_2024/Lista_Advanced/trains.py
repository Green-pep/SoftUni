def add_peoples(wagons, peoples):
    wagons[-1] += peoples
    return wagons


def insert_peoples(wagons, peoples, index):
    wagons[index] += peoples
    return wagons


def leave_peoples(wagons, peoples, index):
    wagons[index] -= peoples
    return wagons


def main(wagons):
    while True:
        prompt = input().split(" ")
        command = prompt[0]

        if command == "End":
            break

        if command == "add":
            number_of_people = int(prompt[1])
            add_peoples(wagons, number_of_people)

        elif command == "insert":
            index = int(prompt[1])
            number_of_people = int(prompt[2])
            insert_peoples(wagons, number_of_people, index)

        elif command == "leave":
            index = int(prompt[1])
            number_of_people = int(prompt[2])
            leave_peoples(wagons, number_of_people, index)

    return wagons


wagon = [0 for i in range(int(input()))]
print(main(wagon))
