from classes.hand import Hand


class Player:
    def __init__(self, num_hands=1):
        self.hands = [Hand() for _ in range(num_hands)]
        self.num_hands = num_hands
        self.chips = 1000

    def get_hands(self):
        return self.hands

    def get_hand(self, i=0):
        return self.hands[i]

    def get_hands_len(self):
        return len(self.hands)

    def reset_hand(self):
        self.hands = [Hand() for _ in range(self.num_hands)]

    def get_chips(self):
        return self.chips

    def add_chips(self, add_amount):
        self.chips += add_amount

    def lose_chips(self, lose_amount):
        self.chips -= lose_amount

    def bet(self, bet_amount):
        self.chips -= bet_amount
        for hand in self.hands:
            hand.bet(bet_amount)

    def double_bet(self, i):
        self.chips -= self.hands[i].get_bet_amount()
        self.hands[i].double_bet()

    def split_pair(self, deck, i):
        old_hand = self.hands[i]
        new_hand = Hand()
        new_hand.append_card(old_hand.pop_card(1))
        self.chips -= old_hand.get_bet_amount()
        new_hand.bet(old_hand.get_bet_amount())
        old_hand.append_card(deck.deal())
        new_hand.append_card(deck.deal())
        self.hands.append(new_hand)

    # Blackjack = B, Win = W, Push = P, Surrender = S, Lose = L(do nothing)
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
