from libraries.hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [Hand()]
        self.chips = 1000

    def get_name(self):
        return self.name

    def get_hand(self, i=0):
        return self.hand[i]
    
    def reset_hand(self):
        self.hand = [Hand()]

    def get_chips(self):
        return self.chips
    
    def add_chips(self, add_amount):
        self.chips += add_amount

    def payout(self):
        for hand in self.hand:
            if hand.get_payout_status() == 'BLACKJACK':
                self.add_chips(int(2.5 * hand.get_bet_amount()))
            elif hand.get_payout_status == 'WIN':
                self.add_chips(int(2 * hand.get_bet_amount()))
            elif hand.get_payout_status() == 'PUSH':
                self.add_chips(int(0.5 * hand.get_bet_amount()))
            elif hand.get_payout_status() == 'SUR':
                self.add_chips(int(0.5 * hand.get_bet_amount()))
