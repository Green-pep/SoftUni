def add_action(cards_list, card_name):
    if card_name in cards_list:
        print("Card is already in the deck")
        return cards_list
    else:
        cards_list.append(card_name)
        print("Card successfully added")
        return cards_list


def remove_action(cards_list, card_name):
    if card_name not in cards_list:
        print("Card not found")
        return cards_list
    else:
        cards_list.remove(card_name)
        print("Card successfully removed")
        return cards_list


def index_remove(cards_list, index):
    if index < 0 or index > len(cards_list):
        print("Index out of range")
        return cards_list
    else:
        cards_list.pop(index)
        print("Card successfully removed")
        return cards_list


def insert_action(cards_list, index, new_card):
    if index < 0 or index > len(cards_list):
        print("Index out of range")
        if new_card in cards_list:
            print("Card is already added")
            return cards_list
        return cards_list
    else:
        cards_list.insert(index, new_card)
        print("Card successfully added")
        return cards_list


def main_process(list_with_cards, commands):

    for command in range(commands):
        command_ = input().split(", ")
        action = command_[0]

        if action == "Add":
            card = command_[1]
            list_with_cards = add_action(list_with_cards, card)

        elif action == "Remove":
            card = command_[1]
            remove_action(list_with_cards, card)

        elif action == "Remove At":
            index = int(command_[1])
            index_remove(list_with_cards, index)

        elif action == "Insert":
            index = int(command_[1])
            new_card = command_[2]
            insert_action(list_with_cards, index, new_card)

    return list_with_cards


deck_of_cards = input().split(", ")
count_of_commands = int(input())

print(", ".join(main_process(deck_of_cards, count_of_commands)))
