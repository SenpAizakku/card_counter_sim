# Names and suits used to make a card -> deck -> shoe
card_names = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
card_suits = ['spades', 'clubs', 'hearts', 'diamonds']

# Values to be used for game of blackjack and keeping the running count.
bj_values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 1}
run_values = {'two': 1, 'three': 1, 'four': 1, 'five': 1, 'six': 1, 'seven': 0, 'eight': 0, 'nine': 0, 'ten': -1, 'jack': -1, 'queen': -1, 'king': -1, 'ace': -1}

# All classes. Card -> deck -> shoe -> player
class Card:
    def __init__(self, name, suit, bj_value, run_value):
        self.name = name
        self.suit = suit
        self.blackjack_value = bj_value
        self.running_value = run_value

    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def get_blackjack_val(self):
        return self.blackjack_value
    def get_run_val(self):
        return self.running_value
    def __repr__(self):
        return "{} of {} | bj: {} | run: {}".format(self.name, self.suit, self.blackjack_value, self.running_value)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for name in card_names:
            for suit in card_suits:
                self.cards.append(Card(name, suit, bj_values[name], run_values[name]))

    def __repr__(self):
        return self.cards

    def __iter__(self):
        self.index = 0
        return self.cards[self.index]

    def __next__(self):
        while self.index < 53:
            self.index += 1

class Shoe:
    def __init__(self, num_decks):
        self.size = num_decks
        self.decks = [Deck()] * self.size #creates a list of lists that are each deck
        self.cards = [card for deck in self.decks for card in deck] #iterates through each deck and makes a single list of all cards

    def __repr__(self):
        list_cards = []
        for card in self.cards:
            list_cards.append(card)
        return list_cards


""" make this later
class Player:
    self.cards = {}
    self.card_value = 0

    def play_hand():
"""
test_shoe = Shoe(2)
print(test_shoe)
