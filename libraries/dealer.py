# import sys
# import os

# ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
# sys.path.append(ROOT_DIR)


from libraries.hand import Hand


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_hand(self):
        return self.hand

    def append_card(self, card):
        self.hand.append(card)

    def play(self, deck):
        while self.hand.get_values()[0] < 17 and self.hand.get_values()[1] < 17:
            self.hit(deck)

    def hit(self, deck):
        self.hand.append_card(deck.deal())
    
    def reset_hand(self):
        self.hand = Hand()
    
    def reveal(self):
        self.hand.flip_second_card()
        print('Dealer: ', end='')
        self.hand.print_hand()