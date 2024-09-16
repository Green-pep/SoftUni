def add_username(username, sent_messages, received_messages, dict_with_users):
        if username in dict_with_users:
            return dict_with_users
        total_messages = int(sent_messages) + int(received_messages)
        dict_with_users[username] = total_messages
        return dict_with_users


def message_user_to_user(user_one_sender, user_two_receiver, dict_with_users, max_capacity):
    if user_one_sender in dict_with_users.keys() and user_two_receiver in dict_with_users.keys():
        dict_with_users[user_one_sender] += 1
        if dict_with_users[user_one_sender] >= max_capacity:
            dict_with_users.pop(user_one_sender)
            print(f"{user_one_sender} reached the capacity!")

        dict_with_users[user_two_receiver] += 1
        if dict_with_users[user_two_receiver] >= max_capacity:
            dict_with_users.pop(user_two_receiver)
            print(f"{user_two_receiver} reached the capacity!")
    return dict_with_users


def empty_username(username, dict_with_users):
    if username == "All":
        dict_with_users.clear()
        return dict_with_users
    else:
        dict_with_users.pop(username)


total_max_capacity_of_massages = int(input())
data_of_users = {}

while True:
    inline_command = input().split("=")
    if inline_command[0] == "Statistics":
        break
    command = inline_command[0]
    if command == "Add":
        user = inline_command[1]
        sente_msg = inline_command[2]
        received_msg = inline_command[3]
        add_username(user, sente_msg, received_msg, data_of_users)
    elif command == "Message":
        sender = inline_command[1]
        receiver = inline_command[2]
        message_user_to_user(sender, receiver, data_of_users, total_max_capacity_of_massages)
    elif command == "Empty":
        user = inline_command[1]
        empty_username(user, data_of_users)
count = len(data_of_users)

print(f"Users count: {count}")
for key, value in data_of_users.items():
    print(f"{key} - {value}")