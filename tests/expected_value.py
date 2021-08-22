# Find the Expected Chips Change After Playing n Games of n Rounds

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from games.autoplayer import get_chips_after_rounds

num_rounds = 100
num_games = 10**6
chips = []

for i in range(num_games):
    chip = get_chips_after_rounds(num_rounds)
    print(f'Game {i+1}: {chip}')
    chips.append(chip)

print(f'Expected Chips: {sum(chips) / num_games}')


# STARTING WITH 1000 CHIPS

# No Betting and Playing Deviation (bet amount: 100)
# rounds: 100, games: 10**2 => expected chips: 747.5
# rounds: 100, games: 10**3 => expected chips: 929.15
# rounds: 100, games: 10**4 => expected chips: 984.385
# rounds: 100, games: 10**5 => expected chips: 998.074
# rounds: 100, games: 10**6 => expected chips: 996.3743
# rounds: 100, games: 10**7 => expected chips: 996.987955

# With Betting Deviation (betting deviation: 10 - 600)
# rounds: 100, games: 10**2 => expected chips: 992.45
# rounds: 100, games: 10**3 => expected chips: 1025.3
# rounds: 100, games: 10**4 => expected chips: 1033.748
# rounds: 100, games: 10**5 => expected chips: 1034.88145
# rounds: 100, games: 10**6 => expected chips: 1034.372555
# rounds: 100, games: 10**7 => expected chips: 