# Find the Expected Chips Change After Playing n Games of n Rounds

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from game.simulator import get_chips_after_rounds


number_of_rounds = 100
number_of_games = 10000 
chips = []
for _ in range(number_of_games):
    chips.append(get_chips_after_rounds(number_of_rounds))
print(f'Expected Chips: {sum(chips) / number_of_games}')


# STARTING WITH 1000 CHIPS

# No Betting and Playing Deviation
# rounds: 100, games: 10000 => expected chips: 972.6375

# With Betting Deviation (<0.5 - 10, <1 - 50, <1.5 - 100, ..., <5.5 - 500, <6 - 550, >=6 - 600)
# rounds: 100, games: 10000 => expected chips: 1033.2515