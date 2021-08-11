class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = 10 if rank > 10 else rank
        self.shown = True

    # 1 = ace, ... , 11 = jack, 12 = queen, 13 = king
    def get_rank(self):
        return self.rank

    # C = clubs, D = diamonds, H = hearts, S = spades
    def get_suit(self):
        return self.suit

    # ace = 1, ..., 10 = 10, jack = 10, queen = 10, king = 10
    def get_value(self):
        return self.value

    def flip(self):
        self.shown = not self.shown

    # return 'black' or 'red'
    # def get_color(self):
    #     return 'black' if self.suit in ['C', 'S'] else 'red'

    def get_name(self):
        if not self.shown:
            return 'card'
        if self.rank == 1:
            return 'A' + str(self.suit)
        if self.rank == 11:
            return 'J' + str(self.suit)
        if self.rank == 12:
            return 'Q' + str(self.suit)
        if self.rank == 13:
            return 'K' + str(self.suit)
        return str(self.rank) + str(self.suit)
