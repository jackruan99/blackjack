# Single Player Blackjack Terminal Simulator

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from classes.card import Card
from classes.deck import Deck
from classes.dealer import Dealer
from classes.player import Player
from libraries.color import *
from libraries.strategy import *
from games.settings import input_settings


def get_shuffled_deck(num_decks):
    deck = Deck(num_decks)
    deck.shuffle()
    return deck


def get_best_betting_amount(true_count):
    if true_count < 0.5:
        return betting_spread[0]
    if true_count < 1:
        return betting_spread[1]
    if true_count < 1.5:
        return betting_spread[2]
    if true_count < 2:
        return betting_spread[3]
    if true_count < 2.5:
        return betting_spread[4]
    if true_count < 3:
        return betting_spread[5]
    if true_count < 3.5:
        return betting_spread[6]
    if true_count < 4:
        return betting_spread[7]
    if true_count < 4.5:
        return betting_spread[8]
    if true_count < 5:
        return betting_spread[9]
    if true_count < 5.5:
        return betting_spread[10]
    if true_count < 6:
        return betting_spread[11]
    return betting_spread[12]


def deal(deck, dealer, player):
    for hand in player.get_hands():
        hand.append_card(deck.deal())
        hand.append_card(deck.deal())
        # hand.append_card(Card(1, 'S'))
        # hand.append_card(Card(10, 'S'))
    dealer.get_hand().append_card(deck.deal())
    dealer.get_hand().append_card(deck.deal(show=False))


def print_dealer_hand(dealer_hand):
    print(BOLD + 'Dealer: ', end='')
    dealer_hand.print_hand()


def print_player_hand(player_hand, color):
    print(color + 'Player: ', end='')
    player_hand.print_hand()


def print_dealer_player_hand(dealer_hand, player_hand, color):
    print_dealer_hand(dealer_hand)
    print_player_hand(player_hand, color)


def betting(deck, dealer, player):
    print(f'You have {UNDERLINE + str(player.get_chips()) + END} chips.')
    bet_amount = None
    while True:
        try:
            bet_amount = int(input(f"This Round's Bet (Recommend: {UNDERLINE + str(get_best_betting_amount(deck.get_true_count())) + END}): "))
            if bet_amount <= 0 or bet_amount > player.get_chips() :
                print(RED + 'INVALID INPUT!' + END)
            else:
                break
        except:
            print(RED + 'INVALID INPUT!' + END)
    player.bet(bet_amount)
    deal(deck, dealer, player)


def insurance(dealer_hand, player_hand, true_count, player_color):
    best_action = 'Y' if true_count >= 3 else 'N'
    print_dealer_player_hand(dealer_hand, player_hand, player_color)
    print(f'Possible Actions: Yes(Y), No(N). (Best Action: {best_action})')
    insure = input('Do you want to buy insurance: ')
    while insure not in ['Y', 'N']:
        insure = input('Do you want to buy insurance: ')
    return insure == 'Y'

def want_split(dealer_hand, player_hand):
    player_hand_value = player_hand.get_cards_value()
    if player_hand_value[0] == player_hand_value[1]:
        best_action = pair_splitting[player_hand_value[0]][dealer_hand.get_cards_value()[0]]
        print(f'Possible Actions: Yes(Y), No(N). (Best Action: {UNDERLINE + best_action + END})')
        split = input('Do you want to split: ')
        while split not in ['Y', 'N']:
            print(RED + 'INVALID INPUT!' + END)
            split = input('Do you want to split: ')
        return split == 'Y'
    return False


def split_pair(deck, player, i):
    player.split_pair(deck, i)


def get_best_action(dealer_hand, player_hand, can_double=True):
    best_action = 'X'
    if not can_double:
        if player_hand.get_hand_len() == 2:
            player_hand_value = player_hand.get_cards_value()
            dealer_hand_value = dealer_hand.get_cards_value()
            if 1 in player_hand_value:
                other_value = player_hand_value[0] if player_hand_value[0] != 1 else player_hand_value[1]
                best_action = soft_totals2[other_value][dealer_hand_value[0]]
            else:
                player_value = player_hand.get_best_value()
                if (player_value == 15 and dealer_hand_value[0] == 10) or (player_value == 16 and dealer_hand_value[0] in [1, 9, 10]):
                    best_action = 'SUR'
                else:
                    best_action = hard_totals2[player_value][dealer_hand_value[0]]
        elif player_hand.get_hand_len() > 2:
            player_hand_value = player_hand.get_cards_value()
            dealer_hand_value = dealer_hand.get_cards_value()
            if 1 not in player_hand_value:
                player_value = player_hand.get_best_value()
                best_action = hard_totals2[player_value][dealer_hand_value[0]]
            else:
                player_value = player_hand.get_values()
                if player_value[0] > 11:
                    best_action = hard_totals2[player_hand.get_best_value()][dealer_hand_value[0]]
                else:
                    other_value = player_value[0] - 1
                    best_action = soft_totals2[other_value][dealer_hand_value[0]]
    else:
        if player_hand.get_hand_len() == 2:
            player_hand_value = player_hand.get_cards_value()
            dealer_hand_value = dealer_hand.get_cards_value()
            if 1 in player_hand_value:
                other_value = player_hand_value[0] if player_hand_value[0] != 1 else player_hand_value[1]
                best_action = soft_totals[other_value][dealer_hand_value[0]]
            else:
                player_value = player_hand.get_best_value()
                if (player_value == 15 and dealer_hand_value[0] == 10) or (player_value == 16 and dealer_hand_value[0] in [1, 9, 10]):
                    best_action = 'SUR'
                else:
                    best_action = hard_totals[player_value][dealer_hand_value[0]]
        elif player_hand.get_hand_len() > 2:
            player_hand_value = player_hand.get_cards_value()
            dealer_hand_value = dealer_hand.get_cards_value()
            if 1 not in player_hand_value:
                player_value = player_hand.get_best_value()
                best_action = hard_totals2[player_value][dealer_hand_value[0]]
            else:
                player_value = player_hand.get_values()
                if player_value[0] > 11:
                    best_action = hard_totals2[player_hand.get_best_value()][dealer_hand_value[0]]
                else:
                    other_value = player_value[0] - 1
                    best_action = soft_totals2[other_value][dealer_hand_value[0]]
    return best_action


def first_action(deck, dealer, player, i, player_color):
    hand = player.get_hand(i)
    if hand.check_blackjack():
        hand.set_payout_status('B')
    else:
        can_double = True if player.get_chips() >= hand.get_bet_amount() else False
        best_action = get_best_action(dealer.get_hand(), hand, can_double)
        print(f'Possible Actions: Hit(H), Stand(S), Double Down(D), Surrender(SUR). (Best Action: {UNDERLINE + best_action + END})')
        action = input('Your action: ')
        if action == 'H':
            hand.append_card(deck.deal())
            print_player_hand(hand, player_color)
            hand.set_last_action('H')
        elif action == 'S':
            hand.set_last_action('S')
        elif action == 'D':
            if not can_double:
                print(RED + 'NOT ENOUGH CHIPS!' + END)
            else:
                player.double_bet(i)
                hand.append_card(deck.deal())
                print(f"This round's bet (Double Down): {hand.get_bet_amount()}")
                print_player_hand(hand, player_color)
                hand.set_last_action('D')
        elif action == 'SUR':
            hand.set_last_action('SUR')
            hand.set_payout_status('S')
        else:
            print(RED + 'INVALID INPUT!' + END)


def more_action(deck, dealer, player, i, player_color):
    hand = player.get_hand(i)
    if hand.get_values()[0] > 21 and hand.get_values()[1] > 21:
        print(BOLD + 'YOU BUST!' + END)
        hand.set_payout_status('L')
    else:
        best_action = get_best_action(dealer.get_hand(), hand)
        print(f'Possible Actions: Hit(H), Stand(S). (Best Action: {UNDERLINE + best_action + END})')
        action = input('Your action: ')
        if action == 'H':
            hand.append_card(deck.deal())
            print_player_hand(hand, player_color)
            hand.set_last_action('H')
        elif action == 'S':
            hand.set_last_action('S')
        else:
            print(RED + 'INVALID INPUT!' + END)


def update_payout_status(deck, dealer, player, settings, player_color):
    dealer.reveal()
    print_dealer_hand(dealer.get_hand())
    dealer_hand = dealer.get_hand()

    soft_17 = dealer_hand.get_values() == [7, 17]
    while (settings['s17'] and soft_17) or (dealer_hand.get_values()[0] < 17 and (dealer_hand.get_values()[1] < 17 or dealer_hand.get_values()[1] > 21)):
        dealer_hand.append_card(deck.deal())
        print_dealer_hand(dealer.get_hand())
        soft_17 = dealer_hand.get_values() == [7, 17]
    for i in range(player.get_hands_len()):
        hand = player.get_hand(i)
        print(BOLD + f'-- Hand {i+1} --' + END)
        print_dealer_player_hand(dealer_hand, hand, player_color)
        payout_status = hand.get_payout_status()
        if payout_status == 'B':
            print(BOLD + 'BLACKJACK!' + END)
        elif payout_status == 'S':
            print(BOLD + 'YOU SURRENDERED!' + END)
        elif payout_status == 'L':
            pass
        else:
            player_best_value = hand.get_best_value()
            dealer_best_value = dealer_hand.get_best_value()
            if player_best_value <= 21:
                if dealer_best_value > 21:
                    print(BOLD + 'DEALER BUSTS!' + END)
                    hand.set_payout_status('W')
                else:
                    if player_best_value > dealer_best_value:
                        print(BOLD + 'YOU WIN!' + END)
                        hand.set_payout_status('W')
                    elif player_best_value < dealer_best_value:
                        print(BOLD + 'DEALER WINS!' + END)
                        hand.set_payout_status('L' + END)
                    else:
                        print(BOLD + 'PUSH!' + END)
                        hand.set_payout_status('P')


def reset(dealer, player):
    dealer.reset_hand()
    player.reset_hand()


def play_round(round, deck, dealer, player, player_color, game_settings):
    print()
    print(BOLD + f'ROUND {round} ' + END + f'(cards left: {UNDERLINE + str(deck.get_deck_len()) + END} | count: {UNDERLINE + str(deck.get_count()) + END} | true count: {UNDERLINE + str(deck.get_true_count()) + END})')
    betting(deck, dealer, player)
    dealer_hand, player_hand = dealer.get_hand(), player.get_hand()
    # Insurance
    if dealer_hand.get_cards_value()[0] == 1 and game_settings['insurance']:
        if insurance(dealer_hand, player_hand, deck.get_true_count(), player_color):
            if dealer_hand.check_blackjack():
                player.add_chips(int(player_hand.get_bet_amount()))
            else:
                player.lose_chips(int(player_hand.get_bet_amount() / 2))

    if dealer_hand.check_blackjack():
        dealer.reveal()
        print_dealer_player_hand(dealer_hand, player_hand, player_color)
        if player_hand.check_blackjack():
            print(BOLD + 'BLACKJACK PUSH!' + END)
            player_hand.set_payout_status('P')
        else:
            print(BOLD + 'DEALER BLACKJACK!' + END)
            player_hand.set_payout_status('L')
    else:
        i = 0
        while i < player.get_hands_len():
            print(BOLD + f'-- Hand {i+1} --' + END)
            print_dealer_player_hand(dealer.get_hand(), player.get_hand(i), player_color)
            while want_split(dealer_hand, player.get_hand(i)):
                split_pair(deck, player, i)
                print(BOLD + f'-- Hand {i+1} --' + END)
                print_dealer_player_hand(dealer.get_hand(), player.get_hand(i), player_color)
            while True:
                if player.get_hand(i).get_hand_len() == 2:
                    first_action(deck, dealer, player, i, player_color)
                    if player.get_hand(i).get_last_action() in ['S', 'D', 'SUR'] or player.get_hand(i).get_payout_status() in ['B', 'S', 'L']:
                        break
                else:
                    more_action(deck, dealer, player, i, player_color)
                    if player.get_hand(i).get_last_action() == 'S' or player.get_hand(i).get_payout_status() == 'L':
                        break
            i += 1
        update_payout_status(deck, dealer, player, game_settings, player_color)
    player.payout()
    reset(dealer, player)


def play_game():
    print(BOLD + f'-- Blackjack Game Simulator --' + END)
    num_decks, s17, insurance, player_color = input_settings()
    game_settings = {'s17': s17, 'insurance': insurance}
    deck, dealer, player = get_shuffled_deck(num_decks), Dealer(), Player()

    round = 1
    # Plays until the player has 0 chips
    while player.get_chips() > 0:
        play_round(round, deck, dealer, player, player_color, game_settings)
        if deck.get_deck_len() < int(num_decks * 52 * 0.25):
            deck = get_shuffled_deck(num_decks)
            print()
            print('DECK RESHUFFLED!')
        round += 1


play_game()