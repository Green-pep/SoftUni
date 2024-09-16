deck_with_cards = input().split()
number_of_shuffles = int(input())
final_deck = []


for deck in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_with_cards) // 2

    left_deck = deck_with_cards[0:middle_of_the_deck]
    right_deck = deck_with_cards[middle_of_the_deck:]

    for shuffle in range(len(left_deck)):
        final_deck.append(left_deck[shuffle])
        final_deck.append(right_deck[shuffle])
    deck_with_cards = final_deck
print(final_deck)
