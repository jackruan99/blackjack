class Card:
    def __init__(self, rank, suit, shown=True):
        self.rank = rank
        self.suit = suit
        self.value = 10 if rank > 10 else rank
        self.shown = shown

    # ace = 1, ... , 10 = 10, jack = 11, queen = 12, king = 13
    def get_rank(self):
        return self.rank

    # clubs = C, diamonds = D, hearts = H, spades = S
    def get_suit(self):
        return self.suit

    # ace = 1, ... , 10 = 10, jack = 10, queen = 10, king = 10
    def get_value(self):
        return self.value

    def get_shown(self):
        return self.shown

    def show(self):
        self.shown = True

    def flip(self):
        self.shown = not self.shown

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
