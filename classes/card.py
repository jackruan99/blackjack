class Card:
    def __init__(self, rank, suit, shown=True):
        self.rank = rank
        self.suit = suit
        self.shown = shown

    # ace = 1, ... , 10 = 10, jack = 11, queen = 12, king = 13
    def get_rank(self):
        return self.rank

    # clubs = C, diamonds = D, hearts = H, spades = S
    def get_suit(self):
        return self.suit

    def get_shown(self):
        return self.shown

    def show(self):
        self.shown = True

    def flip(self):
        self.shown = not self.shown
    
    # ace = 1, ... , 10 = 10, jack = 10, queen = 10, king = 10
    def get_value(self):
        return 10 if self.rank > 10 else self.rank

    def get_name(self):
        if not self.shown:
            return 'Card'
        if self.rank == 1:
            return 'A' + self.suit
        if self.rank == 11:
            return 'J' + self.suit
        if self.rank == 12:
            return 'Q' + self.suit
        if self.rank == 13:
            return 'K' + self.suit
        return str(self.rank) + self.suit
