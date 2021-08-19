from classes.hand import Hand
from libraries.color import *


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_hand(self):
        return self.hand
    
    def reveal(self):
        self.hand.show_second_card()
        print(GREEN + 'Dealer: ', end='')
        self.hand.print_hand()

    def hit(self, deck):
        self.hand.append_card(deck.deal())
    
    def play(self, deck):
        while self.hand.get_values()[0] < 17 and self.hand.get_values()[1] < 17:
            self.hit(deck)
    
    def reset_hand(self):
        self.hand = Hand()
    
    def check_blackjack(self):
        cards_value = self.hand.get_cards_value()
        return cards_value == [1, 10] or cards_value == [10, 1]