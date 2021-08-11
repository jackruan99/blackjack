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

    def play(self):
        pass

    def hit(self):
        pass