# Single Player Blackjack Simulator

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from libraries.card import Card
from libraries.player import Player
from libraries.dealer import Dealer
from libraries.deck import Deck
from libraries.strategy import *
from libraries.color import *



def create_dealer_player():
    dealer = Dealer()
    name = input("Enter player's name: ")
    player = Player(name)
    return dealer, player


def get_shuffled_deck(num_decks):
    deck = Deck(num_decks)
    deck.shuffle()
    return deck


def want_split(dealer, hand):
    hand_value = hand.get_hand_value()
    if hand_value[0] == hand_value[1]:
        best_action = pair_splitting[hand_value[0]][dealer.get_hand().get_hand_value()[0]]
        print(f'Possible Actions: Yes(Y), No(N). (Best Action: {UNDERLINE + best_action + END})')
        split = input('Do you want to split: ')
        while split not in ['Y', 'N']:
            print(RED + 'INVALID INPUT!' + END)
            split = input('Do you want to split: ')
        else:
            return split == 'Y'
    return False


def split_pair(deck, player, i):
    player.split_pair(deck, i)


def deal(deck, dealer, player):
    player.append_card(Card(1, 'S'))
    dealer.append_card(Card(1, 'S'))
    player.append_card(Card(9, 'S'))
    dealer.append_card(Card(10, 'S', shown=False))
    # player.append_card(deck.deal())
    # dealer.append_card(deck.deal())
    # player.append_card(deck.deal())
    # dealer.append_card(deck.deal(shown=False))


def print_dealer_hand(dealer_hand):
    print(GREEN + 'Dealer: ', end='')
    dealer_hand.print_hand()


def print_player_hand(player_hand):
    print(BLUE + 'Player: ', end='')
    player_hand.print_hand()


def print_dealer_player_hand(dealer_hand, player_hand):
    print_dealer_hand(dealer_hand)
    print_player_hand(player_hand)
    

def betting(round, deck, dealer, player):
    print()
    print(BOLD + f'ROUND {round} ' + END + f'({deck.get_deck_len()} cards left)')
    print(f'You have {UNDERLINE + str(player.get_chips()) + END} chips.')
    bet_amount = None
    while True:
        try:
            bet_amount = int(input("This round's bet: "))
            if bet_amount <= 0 or bet_amount > player.get_chips():
                print(RED + 'INVALID AMOUNT!' + END)
            else:
                break
        except:
            print(RED + 'INVALID AMOUNT!' + END)
        
    player.bet(bet_amount)
    deal(deck, dealer, player)


def get_best_action(dealer_hand, player_hand):
    best_action = 'X'
    player_hand_value = player_hand.get_hand_value()
    dealer_hand_value = dealer_hand.get_hand_value()
    if 1 in player_hand_value:
        other_value = player_hand_value[0] if player_hand_value[0] != 1 else player_hand_value[1]
        best_action = soft_totals[other_value][dealer_hand_value[0]]
    else:
        player_value = player_hand.get_best_value()
        if (player_value == 15 and dealer_hand_value[0] == 10) or (player_value == 16 and dealer_hand_value[0] in [1, 9, 10]):
            best_action = 'SUR'
        else:
            best_action = hard_totals[player_value][dealer_hand_value[0]]
    return best_action


def first_action(deck, dealer, player, i=0):
    hand = player.get_hand(i)
    if hand.get_hand_value() == [1, 10] or hand.get_hand_value() == [10, 1]:
        hand.set_payout_status('B')
    else:
        best_action = get_best_action(dealer.get_hand(), hand)
        print(f'Possible Actions: Hit(H), Stand(S), Double Down(D), Surrender(SUR). (Best Action: {UNDERLINE + best_action + END})')
        action = input('Your action: ')
        if action == 'H':
            hand.append(deck.deal())
            print_player_hand(hand)
            hand.set_last_action('H')
        elif action == 'S':
            hand.set_last_action('S')
        elif action == 'D':
            player.double_bet(hand)
            hand.append(deck.deal())
            print(f"This round's bet (Double Down): {hand.get_bet_amount()}")
            print_player_hand(hand)
            hand.set_last_action('D')
        elif action == 'SUR':
            hand.set_last_action('SUR')
            hand.set_payout_status('S')
        else:
            print(RED + 'INVALID ACTION!' + END)


def more_action(deck, dealer, player, i=0):
    hand = player.get_hand(i)
    # TODO: add best_action logic here 
    if hand.get_values()[0] > 21 and hand.get_values()[1] > 21:
        print(BOLD + 'YOU BUST!' + END)
        hand.set_payout_status('L')
    else:
        print('Possible Actions: Hit(H), Stand(S).')
        action = input('Your action: ')
        if action == 'H':
            hand.append(deck.deal())
            print_player_hand(hand)
            hand.set_last_action('H')
        elif action == 'S':
            hand.set_last_action('S')
        else:
            print(RED + 'INVALID ACTION!' + END)


def update_payout_status(deck, dealer, player):
    dealer.reveal()
    soft_17 = dealer.get_hand().get_values() == [7, 17]
    while soft_17 or (dealer.get_hand().get_values()[0] < 17 and (dealer.get_hand().get_values()[1] < 17 or dealer.get_hand().get_values()[1] > 21)):
        dealer.append_card(deck.deal())
        print_dealer_hand(dealer.get_hand())
        soft_17 = dealer.get_hand().get_values() == [7, 17]
    for i, hand in enumerate(player.get_all_hands()):
        if player.get_hand_len() > 1:
            print(BOLD + f'-- Hand {i+1} --' + END)
            print_dealer_player_hand(dealer.get_hand(), hand)
        if hand.get_payout_status() == 'B':
            if dealer.get_hand().get_hand_value() != [1, 10] and dealer.get_hand().get_hand_value() != [10, 1]:
                print(BOLD + 'BLACKJACK!' + END)
            else:
                hand.set_payout_status('P')
                print(BOLD + 'BLACKJACK PUSH!' + END)
        elif hand.get_payout_status() == 'S':
            print(BOLD + 'YOU SURRENDERED!' + END)
        elif hand.get_payout_status == 'L':
            pass
        else:
            player_best_value = hand.get_best_value()
            dealer_best_value = dealer.get_hand().get_best_value()
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
                        print(BOLD + 'PUSH!')
                        hand.set_payout_status('P')


def reset(dealer, player):
    dealer.reset_hand()
    player.reset_hand()


def play_round(round, deck, dealer, player):
    betting(round, deck, dealer, player)
    if dealer.check_blackjack():
        print_player_hand(player.get_hand())
        dealer.reveal()
        if player.check_blackjack():
            print(BOLD + 'BLACKJACK PUSH!' + END)
            player.get_hand().set_payout_status('P')
        else:
            print(BOLD + 'DEALER BLACKJACK!' + END)
            player.get_hand().set_payout_status('L')
    else:
        i = 0
        while i < player.get_hand_len():
            if player.get_hand_len() > 1:
                print(BOLD + f'-- Hand {i+1} --' + END)
            print_dealer_player_hand(dealer.get_hand(), player.get_hand(i))
            while want_split(dealer, player.get_hand(i)):
                split_pair(deck, player, i)
                if player.get_hand_len() > 1:
                    print(BOLD + f'-- Hand {i+1} --' + END)
                print_dealer_player_hand(dealer.get_hand(), player.get_hand(i))
            while True:
                if len(player.get_hand(i).get_hand()) == 2:
                    first_action(deck, dealer, player, i)
                    if player.get_hand(i).get_last_action() in ['S', 'D', 'SUR'] or player.get_hand(i).get_payout_status() in ['B', 'S', 'L']:
                        break
                else:
                    more_action(deck, dealer, player, i)
                    if player.get_hand(i).get_last_action() == 'S' or player.get_hand(i).get_payout_status() == 'L':
                        break
            i += 1
        update_payout_status(deck, dealer, player)
    player.payout()
    reset(dealer, player)


def play_game(num_decks):
    print(BOLD + '-- Blackjack Game Simulator --' + END)
    dealer, player = create_dealer_player()
    deck = get_shuffled_deck(num_decks)
    round = 1
    while player.get_chips() > 0:  # Play rounds until the player has 0 chip
        play_round(round, deck, dealer, player)
        if deck.get_deck_len() < int(0.25 * num_decks * 52):
            deck = get_shuffled_deck(num_decks)
            print()
            print('DECK RESHUFFLED!')
        round += 1


play_game(2)