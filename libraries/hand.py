from libraries.color import *


class Hand:
    def __init__(self):
        self.hand = []
        self.values = [0, 0]
        self.bet_amount = 0
        self.last_action = 'X'
        self.payout_status = 'X'

    # [Card(), Card()]
    def get_hand(self):
        return self.hand
    
    def get_hand_len(self):
        return len(self.hand)
    
    # [AH, 10S] = [1, 10]
    def get_hand_value(self):
        hand_value = []
        for card in self.hand:
            hand_value.append(card.get_value())
        return hand_value
    
    def get_card(self, i):
        return self.hand[i]
    
    # [AH, 10S] = [11, 21]
    def get_values(self):
        return self.values
    
    # [AH, 10S] = 21
    def get_best_value(self):
        return self.values[1] if self.values[1] <= 21 else self.values[0]
    
    def get_bet_amount(self):
        return self.bet_amount

    def bet(self, bet_amount):
        self.bet_amount = bet_amount

    def double_bet(self):
        self.bet_amount *= 2

    def reset_bet(self):
        self.bet_amount = 0
    
    # None(X), Stand(S), Hit(H), Double Down(D), Surrender(SUR)
    def get_last_action(self):
        return self.last_action
    
    def set_last_action(self, action):
        self.last_action = action
    
    def reset_last_action(self):
        self.last_action = 'X'

    # None(X), Blackjack(B), Win(W), Push(P), Surrender(S), Lose(L)
    def get_payout_status(self):
        return self.payout_status
    
    def set_payout_status(self, status):
        self.payout_status = status
    
    def append(self, card):
        self.hand.append(card)
        if card.is_shown():
            if self.values == [0, 0]:
                if card.get_value() == 1:
                    self.values = [1, 11]
                else:
                    self.values = [card.get_value(), card.get_value()]
            else:
                if card.get_value() == 1:
                    if self.values[0] == self.values[1]:
                        self.values[0] += 1
                        self.values[1] += 11
                    else:
                        self.values[0] += 1
                        self.values[1] += 1
                else:
                    self.values[0] += card.get_value()
                    self.values[1] += card.get_value()
    
    def pop(self, i):
        card = self.hand.pop(i)
        if card.get_value() == 1:
            self.values[0] -= 1
            self.values[1] -= 1
        else:
            self.values[0] -= card.get_value()
            self.values[1] -= card.get_value()
        return card
    
    def show_second_card(self):
        self.hand[1].show()
        if self.hand[1].get_value() == 1:
            if self.values[0] == self.values[1]:
                self.values[0] += 1
                self.values[1] += 11
            else:
                self.values[0] += 1
                self.values[1] += 11
        else:
            self.values[0] += self.hand[1].get_value()
            self.values[1] += self.hand[1].get_value()

    def print_hand(self):
        s = "[ "
        for card in self.hand:
            s += card.get_name() + ' '
        print(s + ']  ' + f'(Value: {str(self.get_best_value())})' + END)
