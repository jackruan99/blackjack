from classes.hand import Hand


class Player:
    def __init__(self):
        self.hands = [Hand()]
        self.chips = 1000
    
    def get_hand(self, i=0):
        return self.hands[i]
    
    def get_hands_len(self):
        return len(self.hands)
    
    def reset_hand(self):
        self.hands = [Hand()]

    def get_chips(self):
        return self.chips
    
    def add_chips(self, add_amount):
        self.chips += add_amount

    def lose_chips(self, lose_amount):
        self.chips -= lose_amount

    def bet(self, bet_amount):
        self.chips -= bet_amount
        self.hands[0].bet(bet_amount)
    
    def double_bet(self, hand):
        self.chips -= hand.get_bet_amount()
        hand.double_bet()

    def split_pair(self, deck, i):
        new_hand = Hand()
        new_hand.append_card(self.hands[i].pop(1))
        self.chips -= self.hands[i].get_bet_amount()
        new_hand.bet(self.hands[i].get_bet_amount())
        self.hands[i].append_card(deck.deal())
        new_hand.append_card(deck.deal())
        self.hands.append(new_hand)

    def payout(self):
        for hand in self.hands:
            payout_status = hand.get_payout_status()
            if payout_status == 'B':
                self.add_chips(int(2.5 * hand.get_bet_amount()))
            elif payout_status == 'W':
                self.add_chips(int(2 * hand.get_bet_amount()))
            elif payout_status == 'P':
                self.add_chips(int(hand.get_bet_amount()))
            elif payout_status == 'S':
                self.add_chips(int(0.5 * hand.get_bet_amount()))
    
    def check_blackjack(self, i=0):
        cards_value = self.get_hand(i).get_cards_value()
        return cards_value == [1, 10] or cards_value == [10, 1]