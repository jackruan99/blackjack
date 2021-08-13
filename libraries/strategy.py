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
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

soft_totals = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H'],
               ['X', 'H', 'Ds', 'Ds', 'Ds', 'Ds', 'Ds', 'S', 'S', 'H', 'H'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'Ds', 'S', 'S', 'S', 'S'],
               ['X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

# N: Don't split the pair
# Y: Split the pair
# Y/N: Split only if 'DAS' is offered
pair_splitting = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                  ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
                  ['X', 'N', 'Y/N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                  ['X', 'N', 'Y/N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                  ['X', 'N', 'N', 'N', 'N', 'Y/N', 'Y/N', 'N', 'N', 'N', 'N'],
                  ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                  ['X', 'N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N'],
                  ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
                  ['X', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N'],
                  ['X', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
                  ['X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]