from libraries.hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [Hand()]
        self.chips = 1000

    def get_name(self):
        return self.name

    def get_all_hands(self):
        return self.hand

    def get_hand(self, i=0):
        return self.hand[i]
    
    def reset_hand(self):
        self.hand = [Hand()]

    def get_hand_len(self):
        return len(self.hand)

    def append_card(self, card, i=0):
        self.hand[i].append(card)

    def get_chips(self):
        return self.chips
    
    def add_chips(self, add_amount):
        self.chips += add_amount

    def bet(self, bet_amount):
        self.chips -= bet_amount
        self.hand[0].bet(bet_amount)
    
    def double_bet(self, hand):
        self.chips -= hand.get_bet_amount()
        hand.double_bet()

    def split_pair(self, deck, i):
        new_hand = Hand()
        new_hand.append(self.hand[i].pop(1))
        self.chips -= self.hand[i].get_bet_amount()
        new_hand.bet(self.hand[i].get_bet_amount())
        self.hand[i].append(deck.deal())
        new_hand.append(deck.deal())
        self.hand.append(new_hand)

    def payout(self):
        for hand in self.hand:
            if hand.get_payout_status() == 'B':
                self.add_chips(int(2.5 * hand.get_bet_amount()))
            elif hand.get_payout_status() == 'W':
                self.add_chips(int(2 * hand.get_bet_amount()))
            elif hand.get_payout_status() == 'P':
                self.add_chips(int(hand.get_bet_amount()))
            elif hand.get_payout_status() == 'S':
                self.add_chips(int(0.5 * hand.get_bet_amount()))
            elif hand.get_payout_status() == 'L':
                pass
    
    def reset_hand(self):
        self.hand = [Hand()]
    
    def check_blackjack(self, i=0):
        return self.get_hand(i).get_hand_value() == [1, 10] or self.get_hand(i).get_hand_value() == [10, 1]