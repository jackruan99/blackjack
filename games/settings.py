from libraries.color import *


# For Terminal Simulator
def input_settings():
    print(BOLD + 'Settings:' + END)
    num_decks, s17, insurance = None, None, None
    while True:
        try:
            num_decks = int(input('Number of Decks (1, 2, 4, 6 or 8): '))
            if num_decks in [1, 2, 4, 6, 8]:
                break
            else:
                print(RED + 'INVALID INPUT!' + END)
        except:
            print(RED + 'INVALID INPUT!' + END)
    while True:
        try:
            s17 = input('Dealer Hits on Soft 17? (Y/N): ')
            if s17 in ['Y', 'N']:
                s17 = s17 == 'Y'
                break
            else:
                print(RED + 'INVALID INPUT!' + END)
        except:
            print(RED + 'INVALID INPUT!' + END)
    while True:
        try:
            insurance = input('Allow Insurance? (Y/N): ')
            if insurance in ['Y', 'N']:
                insurance = insurance == 'Y'
                break
            else:
                print(RED + 'INVALID INPUT!' + END)
        except:
            print(RED + 'INVALID INPUT!' + END)
    # TODO: Add player color support
    # while True:
    #     try:
    #         player_color = input("Player's Color on Terminal? (BLUE, GREEN): ")
    #         if player_color in []:
    #             break
    #         else:
    #             print(RED + 'INVALID INPUT!' + END)
    #     except:
    #         print(RED + 'INVALID INPUT!' + END)
    return num_decks, s17, insurance, BLUE


# For Autoplayer
def auto_settings():
    num_decks = 8
    s17 = True
    insurance = True
    player_color = BLUE
    
    return num_decks, s17, insurance, player_color