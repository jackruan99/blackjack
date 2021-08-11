# import sys
# import os

# ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
# sys.path.append(ROOT_DIR)


from libraries.hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [Hand()]
        self.chips = 1000
        self.bet_amount = 0

    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand
    
    
    def reset_hand(self):
        self.hand = [Hand()]

    def get_chips(self):
        return self.chips
    
    def get_bet_amount(self):
        return self.bet_amount

    def append_card(self, card):
        self.hand[0].append(card)

    def bet(self, bet_amount):
        self.chips -= bet_amount
        self.bet_amount = bet_amount

    def double_bet(self):
        self.chips -= self.bet_amount
        self.bet_amount *= 2

    def reset_bet(self):
        self.bet_amount = 0
