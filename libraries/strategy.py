# Blackjack Strategy Chart


# X: Null Action
# H: Hit
# S: Stand
# D: Double if allowed, otherwise hit
# Ds: Double if allowed, otherwise stand
hard_totals = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H'],
               ['X', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
               ['X', 'H', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

hard_totals2 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

soft_totals = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'D', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

soft_totals2 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

# N: Don't split the pair
# Y: Split the pair
# 'DAS' is offered
pair_splitting = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                  ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                  ['X', 'N', 'N', 'N', 'N', 'Y', 'Y', 'N', 'N', 'N', 'N'],
                  ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                  ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N'],
                  ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                  ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]

# 'DAS' is not offered
pair_splitting2 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                   ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
                   ['X', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                   ['X', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                   ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                   ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                   ['X', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
                   ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                   ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
                   ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N'],
                   ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                   ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]

# True Count - Bet Amount
# <0.5 - 10, <1 - 50, <1.5 - 100, ..., <5.5 - 500, <6 - 550, >=6 - 600
betting_spread = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]