# Single Player Blackjack Autoplayer

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
from games.settings import auto_settings


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
    dealer.get_hand().append_card(deck.deal())
    dealer.get_hand().append_card(deck.deal(show=False))


def betting(deck, dealer, player):
    bet_amount = 100
    # bet_amount = get_best_betting_amount(deck.get_true_count())
    player.bet(bet_amount)
    deal(deck, dealer, player)


def insurance(dealer_hand, player_hand, true_count, player_color):
    return true_count >= 3

def want_split(dealer_hand, player_hand):
    player_hand_value = player_hand.get_cards_value()
    if player_hand_value[0] == player_hand_value[1]:
        return pair_splitting[player_hand_value[0]][dealer_hand.get_cards_value()[0]] == 'Y'
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
        action = get_best_action(dealer.get_hand(), hand, can_double)
        if action == 'H':
            hand.append_card(deck.deal())
            hand.set_last_action('H')
        elif action == 'S':
            hand.set_last_action('S')
        elif action == 'D':
            player.double_bet(i)
            hand.append_card(deck.deal())
            hand.set_last_action('D')
        elif action == 'SUR':
            hand.set_last_action('SUR')
            hand.set_payout_status('S')


def more_action(deck, dealer, player, i, player_color):
    hand = player.get_hand(i)
    if hand.get_values()[0] > 21 and hand.get_values()[1] > 21:
        hand.set_payout_status('L')
    else:
        action = get_best_action(dealer.get_hand(), hand)
        if action == 'H':
            hand.append_card(deck.deal())
            hand.set_last_action('H')
        elif action == 'S':
            hand.set_last_action('S')


def update_payout_status(deck, dealer, player, settings, player_color):
    dealer.reveal()
    dealer_hand = dealer.get_hand()

    soft_17 = dealer_hand.get_values() == [7, 17]
    while (settings['s17'] and soft_17) or (dealer_hand.get_values()[0] < 17 and (dealer_hand.get_values()[1] < 17 or dealer_hand.get_values()[1] > 21)):
        dealer_hand.append_card(deck.deal())
        soft_17 = dealer_hand.get_values() == [7, 17]
    for i in range(player.get_hands_len()):
        hand = player.get_hand(i)
        payout_status = hand.get_payout_status()
        if payout_status not in ['B', 'S', 'L']:
            player_best_value = hand.get_best_value()
            dealer_best_value = dealer_hand.get_best_value()
            if player_best_value <= 21:
                if dealer_best_value > 21:
                    hand.set_payout_status('W')
                else:
                    if player_best_value > dealer_best_value:
                        hand.set_payout_status('W')
                    elif player_best_value < dealer_best_value:
                        hand.set_payout_status('L' + END)
                    else:
                        hand.set_payout_status('P')


def reset(dealer, player):
    dealer.reset_hand()
    player.reset_hand()


def play_round(round, deck, dealer, player, player_color, game_settings):
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
        if player_hand.check_blackjack():
            player_hand.set_payout_status('P')
        else:
            player_hand.set_payout_status('L')
    else:
        i = 0
        while i < player.get_hands_len():
            while want_split(dealer_hand, player.get_hand(i)):
                split_pair(deck, player, i)
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
    num_decks, s17, insurance, player_color = auto_settings()
    game_settings = {'s17': s17, 'insurance': insurance}
    deck, dealer, player = get_shuffled_deck(num_decks), Dealer(), Player()

    round = 1
    # Plays until the player has 0 chips
    while player.get_chips() > 0:
        play_round(round, deck, dealer, player, player_color, game_settings)
        if deck.get_deck_len() < int(num_decks * 52 * 0.25):
            deck = get_shuffled_deck(num_decks)
        round += 1


def get_chips_after_rounds(num_rounds):
    num_decks, s17, insurance, player_color = auto_settings()
    game_settings = {'s17': s17, 'insurance': insurance}
    deck, dealer, player = get_shuffled_deck(num_decks), Dealer(), Player()

    round = 1
    # Plays until the player has 0 chips
    while player.get_chips() > 0:
        play_round(round, deck, dealer, player, player_color, game_settings)
        if deck.get_deck_len() < int(num_decks * 52 * 0.25):
            deck = get_shuffled_deck(num_decks)
        if round == num_rounds:
            return player.get_chips()
        round += 1
    return 0


print(get_chips_after_rounds(100))