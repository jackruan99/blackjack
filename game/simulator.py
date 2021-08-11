# Single Player Blackjack Simulator

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from libraries.player import Player
from libraries.dealer import Dealer
from libraries.deck import Deck
from strategy import *


def create_dealer_player():
    dealer = Dealer()
    name = input('Enter your name: ')
    player = Player(name)
    return dealer, player


def get_shuffled_deck(num_decks):
    deck = Deck(num_decks)
    deck.shuffle()
    return deck


def check_split(hand):
    if hand[0].get_value() == hand[1].get_value():
        split = input('Do you want to split (y/n): ')
        if split == 'y':
            # split cards
            pass


def deal(deck, dealer, player):
    player.append_card(deck.deal())
    dealer.append_card(deck.deal())
    player.append_card(deck.deal())
    dealer.append_card(deck.deal(shown=False))


def print_dealer_player_hand(dealer, player):
    print('Dealer: ', end='')
    dealer.get_hand().print_hand()
    print(player.get_name(), end=': ')
    player.get_hand()[0].print_hand()


def betting(round, deck, dealer, player):
    print()
    print(f'ROUND {round} ({len(deck.get_deck())} cards left)')
    print(f'You have {player.get_chips()} chips.')
    bet_amount = 0
    while True:
        try:
            bet_amount = int(input("This round's bet: "))
            break
        except:
            print('Please enter a integer number.')
    player.bet(bet_amount)
    deal(deck, dealer, player)
    print_dealer_player_hand(dealer, player)


def get_best_action(dealer, player):
    best_action = 'X'
    player_hand_value = player.get_hand()[0].get_hand_value()
    dealer_hand_value = dealer.get_hand().get_hand_value()
    if 1 in player_hand_value:
        other_value = player_hand_value[0] if player_hand_value[0] != 1 else player_hand_value[1]
        best_action = soft_totals[other_value][dealer_hand_value[0]]
    else:
        player_value = player.get_hand()[0].get_best_value()
        if (player_value == 15 and dealer_hand_value[0] == 10) or (player_value == 16 and dealer_hand_value[0] in [1, 9, 10]):
            best_action = 'SUR'
        else:
            best_action = hard_totals[player_value][dealer_hand_value[0]]
    return best_action

def first_action(deck, dealer, player):
    if player.get_hand()[0].get_hand_value() == [1, 10] or player.get_hand()[0].get_hand_value() == [10, 1]:
        player.set_last_action('BLACKJACK')
    else:
        best_action = get_best_action(dealer, player)
        print(f'Possible Actions: Hit(H), Stand(S), Double Down(D), Surrender(SUR). (Best Action: {best_action})')
        action = input('Your action: ')
        if action == 'H':
            player.append_card(deck.deal())
            print(player.get_name(), end=': ')
            player.get_hand()[0].print_hand()
            player.set_last_action('H')
        elif action == 'S':
            player.set_last_action('S')
        elif action == 'D':
            player.double_bet()
            player.append_card(deck.deal())
            print(f"This round's bet (Double Down): {player.get_bet_amount()}")
            print_dealer_player_hand(dealer, player)
            player.set_last_action('D')
        elif action == 'SUR':
            player.set_last_action('SUR')
        else:
            print('NO ACTION FOUND!')


def more_action(deck, dealer, player):
    if player.get_hand()[0].get_values()[0] > 21 and player.get_hand()[0].get_values()[1] > 21:
        print('YOU BUST!')
        player.set_last_action('BUST')
    else:
        print('Possible Actions: Hit(H), Stand(S).')
        action = input('Your action: ')
        if action == 'H':
            player.append_card(deck.deal())
            print_dealer_player_hand(dealer, player)
            player.set_last_action('H')
        elif action == 'S':
            player.set_last_action('S')
        else:
            print('NO ACTION FOUND!')


def find_winner_and_payout(deck, dealer, player):
    if player.get_last_action() == 'SUR':
        print('YOU SURRENDERED!')
        player.add_chips(int(player.get_bet_amount() / 2))
    elif player.get_last_action() == 'BLACKJACK':
        dealer.reveal()
        if dealer.get_hand().get_hand_value() != [1, 10] and dealer.get_hand().get_hand_value() != [10, 1]:
            print('BLACKJACK!')
            player.add_chips(int(2.5 * player.get_bet_amount()))
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
                player.add_chips(2 * player.get_bet_amount())
            else:
                if player_best_value > dealer_best_value:
                    print('YOU WIN!')
                    player.add_chips(2 * player.get_bet_amount())
                elif player_best_value < dealer_best_value:
                    print('DEALER WINS!')
                else:
                    print('PUSH!')
                    player.add_chips(player.get_bet_amount())


def reset(dealer, player):
    # Reset for next round
    dealer.reset_hand()
    player.reset_bet()
    player.reset_hand()
    player.reset_last_action()


def play_round(round, deck, dealer, player):
    betting(round, deck, dealer, player)
    # check_split(player.get_hand()[0])
    while True:
        if len(player.get_hand()[0].get_hand()) == 2:
            first_action(deck, dealer, player)
            if player.get_last_action() in ['BLACKJACK', 'S', 'D', 'SUR']:
                break
        else:
            more_action(deck, dealer, player)
            if player.get_last_action() in ['BUST', 'S']:
                break
    find_winner_and_payout(deck, dealer, player)
    reset(dealer, player)


def play_game(num_decks):
    print('Blackjack Game Simulator')
    dealer, player = create_dealer_player()
    deck = get_shuffled_deck(num_decks)
    round = 1
    while player.get_chips() > 0:  # Play rounds until player has 0 chip
        play_round(round, deck, dealer, player)
        if len(deck.get_deck()) < (1/4 * 52 * num_decks):
            deck = get_shuffled_deck(num_decks)
            print('DECK RESHUFFLED!')
        round += 1


play_game(2)
