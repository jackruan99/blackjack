# Find the Expected Chips Change After Playing n Games of n Rounds

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from games.autoplayer import get_chips_after_rounds

num_rounds = 100
num_games = 10000
chips = []

for i in range(num_games):
    chip = get_chips_after_rounds(num_rounds)
    print(f'Game {i+1}: {chip}')
    chips.append(chip)

print(f'Expected Chips: {sum(chips) / num_games}')


# STARTING WITH 1000 CHIPS

# No Betting and Playing Deviation (bet amount: 100)
# rounds: 100, games: 100 => expected chips: 
# rounds: 100, games: 1000 => expected chips: 
# rounds: 100, games: 10000 => expected chips: 
# rounds: 100, games: 100000 => expected chips: 
# rounds: 100, games: 1000000 => expected chips: 

# With Betting Deviation (10 - 600)
# rounds: 100, games: 100 => expected chips: 992.45 (<1 second)
# rounds: 100, games: 1000 => expected chips: 1025.3 (6 seconds)
# rounds: 100, games: 10000 => expected chips: 1033.748 (60 seconds)
# rounds: 100, games: 100000 => expected chips:
# rounds: 100, games: 1000000 => expected chips: 
