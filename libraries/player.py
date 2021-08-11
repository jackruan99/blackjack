# import sys
# import os

# ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
# sys.path.append(ROOT_DIR)


from libraries.hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [Hand()]
        self.chip = 0

    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand

    def get_chip(self):
        return self.chip

    def append_card(self, card):
        self.hand[0].append(card)

    # Actions: Hit, Stand, Double, Split, Surrender, Insurance
    def hit(self, deck):
        self.hand.append_card(deck.deal())
    
    def stand(self):
        pass

    def double(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

    # def insurance(self):
    #     pass