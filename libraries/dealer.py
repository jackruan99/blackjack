from libraries.hand import Hand


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_hand(self):
        return self.hand
    
    def reveal(self):
        self.hand.flip_second_card()
        print('Dealer: ', end='')
        self.hand.print_hand()

    def append_card(self, card):
        self.hand.append(card)

    def hit(self, deck):
        self.hand.append_card(deck.deal())
    
    def play(self, deck):
        values = self.hand.get_values()
        while values[0] < 17 and values[1] < 17:
            self.hit(deck)
    
    def reset_hand(self):
        self.hand = Hand()
