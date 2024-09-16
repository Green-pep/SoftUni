def report(blacklisted, lost_, list_with_friends):
    print(f"Blacklisted names: {blacklisted}")
    print(f"Lost names: {lost_}")
    print(" ".join(list_with_friends))


def change_action(list_with_friends, index, new_name):
    print(f"{list_with_friends[index]} changed his username to {new_name}.")
    list_with_friends[index] = new_name
    return list_with_friends


def error_action(list_with_friends, index):
    name = list_with_friends[index]

    list_with_friends[index] = "Lost"
    print(f"{name} was lost due to an error.")
    return list_with_friends


def blacklist(list_with_friends, name):

    index_of_the_name = list_with_friends.index(name)
    list_with_friends[index_of_the_name] = "Blacklisted"

    print(f"{name} was blacklisted.")

    return list_with_friends,


def main_process(friends):

    blacklisted_names = 0
    lost_names = 0

    while True:
        command = input().split()

        if command[0] == "Report":
            report(blacklisted_names, lost_names, friends)
            break

        action = command[0]
        name_of_player = command[1]

        if action == "Blacklist":
            if name_of_player not in friends:
                print(f"{name_of_player} was not found.")
                continue
            else:
                blacklist(friends, name_of_player)
                blacklisted_names += 1

        elif action == "Error":
            index = int(name_of_player)

            if index >= len(friends) or index < 0:
                continue

            elif friends[index] == "Blacklisted" or friends[index] == "Lost":
                continue

            else:
                friends = error_action(friends, index)
                lost_names += 1

        elif action == "Change":
            index = int(name_of_player)
            new_name = command[2]
            if index >= len(friends) or index < 0:
                continue
            friends = change_action(friends, index, new_name)


friends_list = input().split(", ")
main_process(friends_list)
