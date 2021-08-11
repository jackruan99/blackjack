class Hand:
    def __init__(self):
        self.hand = []
        self.values = [0, 0]

    def get_hand(self):
        return self.hand
    
    def get_hand_value(self):
        hand_value = []
        for card in self.hand:
            hand_value.append(card.get_value())
        return hand_value
    
    def get_card(self, i):
        return self.hand[i]
    
    def get_values(self):
        return self.values
    
    def get_best_value(self):
        return self.values[1] if self.values[1] <= 21 else self.values[0]
    
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
    
    def flip_second_card(self):
        self.hand[1].flip()
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
        print(s + ']' + '  value: ' + str(self.get_best_value()))
