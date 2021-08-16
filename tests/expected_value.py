# Find the Expected Chips Change After Playing n Games of n Rounds

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from game.simulator import get_chips_after_rounds


number_of_rounds = 1000
number_of_games = 100
total = 0
for _ in range(number_of_games):
    total += get_chips_after_rounds(number_of_rounds)
print(f'Expected Chips: {total / number_of_games}')