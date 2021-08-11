import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from libraries.deck import Deck
from libraries.dealer import Dealer
from libraries.player import Player


# Takes a list of names
# Return a list of Player
def create_players(names):
    players = []
    for name in names:
        players.append(Player(name))
    return players


def deal_cards(deck, dealer, players):
    dealer.append_card(deck.deal())
    dealer.append_card(deck.deal(shown=False))
    for player in players:
        for _ in range(2):
            player.append_card(deck.deal())


def play_game():
    deck = Deck()
    deck.shuffle()

    dealer = Dealer()
    players = create_players(['A', 'B'])

    deal_cards(deck, dealer, players)

    dealer.get_hand().print_hand()
    for player in players:
        player.get_hand()[0].print_hand()


play_game()