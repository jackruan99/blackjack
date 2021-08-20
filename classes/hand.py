from libraries.color import *


class Hand:
    def __init__(self):
        self.hand = []
        self.values = [0, 0]
        self.bet_amount = 0
        self.last_action = 'X'
        self.payout_status = 'X'

    # example: [AH, 10S] => [Card(), Card()]
    def get_hand(self):
        return self.hand

    def get_hand_len(self):
        return len(self.hand)

    def get_card(self, i=0):
        return self.hand[i]
    
    def append_card(self, card):
        if card.get_show():
            if card.get_value() == 1:
                if self.values[0] == self.values[1]:
                    self.values[0] += 1
                    self.values[1] += 11
                else:
                    self.values[0] += 1
                    self.values[1] += 1
            else:
                value = card.get_value()
                self.values[0] += value
                self.values[1] += value
        self.hand.append(card)
    
    # Only used in splitting pairs
    def pop_card(self, i):
        card = self.hand.pop(i)
        value = card.get_value()
        self.values[0] -= value
        self.values[1] -= value
        return card
    
    def show_second_card(self):
        self.hand[1].flip()
        value = self.hand[1].get_value()
        if value == 1:
            if self.values[0] == self.values[1]:
                self.values[0] += 1
                self.values[1] += 11
            else:
                self.values[0] += 1
                self.values[1] += 1
        else:
            self.values[0] += value
            self.values[1] += value

    # example: [AH, 10S] => [1, 10]
    def get_cards_value(self):
        cards_value = [card.get_value() for card in self.hand]
        return cards_value

    # example: [AH, 10S] => True
    def check_blackjack(self):
        cards_value = self.get_cards_value() 
        return cards_value == [1, 10] or cards_value == [10, 1]

    # example: [AH, 10S] => [11, 21]
    def get_values(self):
        return self.values

    # example: [AH, 10S] => 21
    def get_best_value(self):
        return self.values[1] if self.values[1] <= 21 else self.values[0]

    def get_bet_amount(self):
        return self.bet_amount

    def bet(self, bet_amount):
        self.bet_amount = bet_amount

    def double_bet(self):
        self.bet_amount *= 2

    # Possible Actions: None(X), Stand(S), Hit(H), Double Down(D), Surrender(SUR)
    def get_last_action(self):
        return self.last_action

    def set_last_action(self, action):
        self.last_action = action

    # None(X), Blackjack(B), Win(W), Push(P), Surrender(S), Lose(L)
    def get_payout_status(self):
        return self.payout_status

    def set_payout_status(self, status):
        self.payout_status = status

    def print_hand(self):
        s = "[ "
        for card in self.hand:
            s += card.get_name() + ' '
        print(s + ']  ' + f'(Value: {str(self.get_best_value())})' + END)