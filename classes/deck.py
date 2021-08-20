import random

from classes.card import Card


class Deck:
    def __init__(self, num_decks=1):
        self.deck = [Card(rank, suit) for _ in range(num_decks) for rank in range(1, 14) for suit in ['C', 'D', 'H', 'S']]
        self.num_decks = num_decks
        self.count = 0

    def get_deck(self):
        return self.deck

    def get_deck_len(self):
        return len(self.deck)

    def get_num_decks(self):
        return self.num_decks
    
    def get_count(self):
        return self.count

    def get_true_count(self):
        return round(self.count/self.num_decks, 2)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, show=True):
        card = self.deck.pop()
        if not show:
            card.flip()
        # update count
        card_value = card.get_value()
        if card_value in [1, 10]:
            self.count -= 1
        elif card_value() in [2, 3, 4, 5, 6]:
            self.count += 1
        return card

    def print_deck(self):
        s = "[ "
        for card in self.deck:
            s += card.get_name() + ' '
        print(s + ']')