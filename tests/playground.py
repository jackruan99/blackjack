# Single Player Blackjack Simulator

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
sys.path.append(ROOT_DIR)


from libraries.card import Card
from libraries.player import Player
from libraries.dealer import Dealer
from libraries.deck import Deck
from game.strategy import *


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
        print(f'Possible Actions: Yes(Y), No(N). (Best Action: {best_action})')
        split = input('Do you want to split (Y/N): ')
        return split == 'Y'
    return False


def split_pair(deck, player, i):
    player.split_pair(deck, i)


def deal(deck, dealer, player, dealer_cards, player_cards):
    player.append_card(player_cards[0])
    dealer.append_card(dealer_cards[0])
    player.append_card(player_cards[1])
    dealer.append_card(dealer_cards[1])


def print_dealer_hand(dealer_hand):
    print('Dealer: ', end='')
    dealer_hand.print_hand()


def print_player_hand(player_hand):
    print('Player: ', end='')
    player_hand.print_hand()


def print_dealer_player_hand(dealer_hand, player_hand):
    print_dealer_hand(dealer_hand)
    print_player_hand(player_hand)
    

def betting(round, deck, dealer, player, dealer_cards, player_cards):
    print()
    print(f'ROUND {round} ({deck.get_deck_len()} cards left)')
    print(f'You have {player.get_chips()} chips.')
    bet_amount = None
    while True:
        try:
            bet_amount = int(input("This round's bet: "))
            if bet_amount <= 0 or bet_amount > player.get_chips():
                print('INVALID AMOUNT!')
            else:
                break
        except:
            print('INVALID AMOUNT!')
        
    player.bet(bet_amount)
    deal(deck, dealer, player, dealer_cards, player_cards)


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
        print(f'Possible Actions: Hit(H), Stand(S), Double Down(D), Surrender(SUR). (Best Action: {best_action})')
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
            print('INVALID ACTION!')


def more_action(deck, dealer, player, i=0):
    hand = player.get_hand(i)
    if hand.get_values()[0] > 21 and hand.get_values()[1] > 21:
        print('YOU BUST!')
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
            print('NO ACTION FOUND!')


def update_payout_status(deck, dealer, player):
    for i, hand in enumerate(player.get_all_hands()):
        if player.get_hand_len() > 1:
            print(f'-- Hand {i+1} --')
            print_player_hand(hand)
        if hand.get_payout_status() == 'B':
            dealer.reveal()
            if dealer.get_hand().get_hand_value() != [1, 10] and dealer.get_hand().get_hand_value() != [10, 1]:
                print('BLACKJACK!')
            else:
                hand.set_payout_status('P')
                print('BLACKJACK PUSH!')
        elif hand.get_payout_status() == 'S':
            print('YOU SURRENDERED!')
            dealer.reveal()
        elif hand.get_payout_status == 'L':
            pass
        else:
            dealer.reveal()
            while (dealer.get_hand().get_values()[0] < 17 and dealer.get_hand().get_values()[1] < 17) or (dealer.get_hand().get_values()[0] < 17 and dealer.get_hand().get_values()[1] > 21):
                dealer.append_card(deck.deal())
                print_dealer_hand(dealer.get_hand())
            # Find winner and fix chips
            player_best_value = hand.get_best_value()
            dealer_best_value = dealer.get_hand().get_best_value()
            if player_best_value <= 21:
                if dealer_best_value > 21:
                    print('DEALER BUSTS!')
                    hand.set_payout_status('W')
                else:
                    if player_best_value > dealer_best_value:
                        print('YOU WIN!')
                        hand.set_payout_status('W')
                    elif player_best_value < dealer_best_value:
                        print('DEALER WINS!')
                        hand.set_payout_status('L')
                    else:
                        print('PUSH!')
                        hand.set_payout_status('P')


def reset(dealer, player):
    dealer.reset_hand()
    player.reset_hand()


def play_round(round, deck, dealer, player, dealer_cards, player_cards):
    betting(round, deck, dealer, player, dealer_cards, player_cards)
    i = 0
    while i < player.get_hand_len():
        if player.get_hand_len() > 1:
            print(f'-- Hand {i+1} --')
        print_dealer_player_hand(dealer.get_hand(), player.get_hand(i))
        if want_split(dealer, player.get_hand(i)):
            split_pair(deck, player, i)
            if player.get_hand_len() > 1:
                print(f'-- Hand {i+1} --')
            print_dealer_player_hand(dealer.get_hand(), player.get_hand(i))
        while True:
            if len(player.get_hand(i).get_hand()) == 2:
                first_action(deck, dealer, player, i)
                if player.get_hand(i).get_last_action() in ['S', 'D', 'SUR'] or player.get_hand(i).get_payout_status() in ['B', 'S', 'L']:
                    break
            else:
                more_action(deck, dealer, player)
                if player.get_hand(i).get_last_action() == 'S' or player.get_hand(i).get_payout_status() == 'L':
                    break
        i += 1
    update_payout_status(deck, dealer, player)
    player.payout()
    reset(dealer, player)


def play_game(num_decks, dealer_cards, player_cards):
    print('-- Blackjack Game Simulator --')
    dealer, player = create_dealer_player()
    deck = get_shuffled_deck(num_decks)
    round = 1
    while player.get_chips() > 0:  # Play rounds until the player has 0 chip
        play_round(round, deck, dealer, player, dealer_cards, player_cards)
        if deck.get_deck_len() < int(0.25 * num_decks * 52):
            deck = get_shuffled_deck(num_decks)
            print()
            print('DECK RESHUFFLED!')
        round += 1


play_game(2, [Card(9, 'C'), Card(5, 'H', shown=False)], [Card(11, 'D'), Card(11, 'C')])
