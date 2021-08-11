# import sys
# import os

# ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
# sys.path.append(ROOT_DIR)


import random

from libraries.card import Card


class Deck:
    def __init__(self, size=1):
        self.deck = []
        for _ in range(size):
            for rank in range(1, 14):
                for suit in ['C', 'D', 'H', 'S']:
                    self.deck.append(Card(rank, suit))

    # return a list of Card
    def get_deck(self):
        return self.deck

    # shuffles the current deck
    def shuffle(self):
        random.shuffle(self.deck)

    # remove a Card from deck and return it
    def deal(self):
        return self.deck.pop()

    def print_deck(self):
        s = "[ "
        for card in self.deck:
            s += card.get_name() + ' '
        print(s + ']')
