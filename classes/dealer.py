from classes.hand import Hand
from libraries.color import *


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_hand(self):
        return self.hand
    
    def reveal(self):
        self.hand.show_second_card()

    def play(self, deck):
        while self.hand.get_values()[0] < 17 and self.hand.get_values()[1] < 17:
            self.hand.append_card(deck.deal())
    
    def reset_hand(self):
        self.hand = Hand()