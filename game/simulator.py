# Single Player Blackjack Simulator

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from libraries.player import Player
from libraries.dealer import Dealer
from libraries.deck import Deck


def deal(deck, dealer, player):
    player.append_card(deck.deal())
    dealer.append_card(deck.deal())
    player.append_card(deck.deal())
    dealer.append_card(deck.deal(shown=False))


def check_split(hand):
    if hand[0].get_value() == hand[1].get_value():
        split = input('Do you want to split (y/n): ')
        if split == 'y':
            # split cards
            pass


def print_dealer_player_hand(dealer, player):
    print('Dealer: ', end='')
    dealer.get_hand().print_hand()
    print(player.get_name(), end=': ')
    player.get_hand()[0].print_hand()


def play_round(round, deck, dealer, player):
    print()
    print(f'ROUND {round} ({len(deck.get_deck())} cards left)')
    print(f'You have {player.get_chips()} chips.')
    bet_amount = int(input("This round's bet: "))
    player.bet(bet_amount)
    deal(deck, dealer, player)
    print_dealer_player_hand(dealer, player)
    # check_split(player.get_hand()[0])
    while True:
        if len(player.get_hand()[0].get_hand()) == 2:
            print('Possible Actions: Hit(H), Stand(S), Double Down(D), Surrender(SUR).')
            action = input('Your action: ')
            if action == 'H':
                player.append_card(deck.deal())
                print(player.get_name(), end=': ')
                player.get_hand()[0].print_hand()
            elif action == 'S':
                break
            elif action == 'D':
                player.double_bet()
                player.append_card(deck.deal())
                print(f"This round's bet (Double Down): {player.get_bet_amount()}")
                print_dealer_player_hand(dealer, player)
                break
            elif action == 'SUR':
                # surrender
                pass
            else:
                print('NO ACTION FOUND!')
        else:
            if player.get_hand()[0].get_values()[0] > 21 and player.get_hand()[0].get_values()[1] > 21:
                print('YOU BUST!')
                break
            else:
                print('Possible Actions: Hit(H), Stand(S).')
                action = input('Your action: ')
                if action == 'H':
                    player.append_card(deck.deal())
                    print_dealer_player_hand(dealer, player)
                elif action == 'S':
                    break
                else:
                    print('NO ACTION FOUND!')
    # If I have a blackjack
    if player.get_hand()[0] == [1, 10] or player.get_hand()[0] == [10, 1]:
        dealer.reveal()
        if dealer.get_hand()[0] != [1, 10] and dealer.get_hand()[0] != [10, 1]:
            print('BLACKJACK!')
            player.add_chips(2.5 * bet_amount)
    else:
        # Dealer plays out the cards
        dealer.reveal()
        while (dealer.get_hand().get_values()[0] < 17 and dealer.get_hand().get_values()[1] < 17) or (dealer.get_hand().get_values()[0] < 17 and dealer.get_hand().get_values()[1] > 21):
            dealer.append_card(deck.deal())
            print('Dealer: ', end='')
            dealer.get_hand().print_hand()
        # Find winner and fix chips
        player_best_value = player.get_hand()[0].get_best_value()
        dealer_best_value = dealer.get_hand().get_best_value()
        if player_best_value <= 21:
            if dealer_best_value > 21:
                print('DEALER BUSTS!')
                player.add_chips(2 * bet_amount)
            else:
                if player_best_value > dealer_best_value:
                    print('YOU WIN!')
                    player.add_chips(2 * bet_amount)
                elif player_best_value < dealer_best_value:
                    print('DEALER WINS!')
                else:
                    print('PUSH!')
                    player.add_chips(bet_amount)
    # Reset for next round
    dealer.reset_hand()
    player.reset_bet()
    player.reset_hand()


def play_game(num_decks):
    print('Blackjack Game Simulator')
    # Create dealer and player
    dealer = Dealer()
    name = input('Enter your name: ')
    player = Player(name)
    # Initialize deck
    deck = Deck(num_decks)
    deck.shuffle()
    # Play rounds
    round = 1
    while player.get_chips() > 0:
        play_round(round, deck, dealer, player)
        if len(deck.get_deck()) < (1/4 * 52 * num_decks):
            deck = Deck(num_decks)
            deck.shuffle()
            print('DECK RESHUFFLED!')
        round += 1


play_game(2)
