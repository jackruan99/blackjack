# import sys
# import os

# ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
# sys.path.append(ROOT_DIR)


from libraries.hand import Hand
from libraries.deck import Deck


deck = Deck(2)
deck.shuffle()

hand = Hand()
hand.append(deck.deal())
hand.append(deck.deal())

hand.print_hand()
print(hand.get_values())