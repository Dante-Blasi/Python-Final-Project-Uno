#Dante Blasi
#CS21 Final Project
#Plays the card game Uno with the user

    #Import random module
import random

def main():
        #Print start screen
    print('''
     ___________
    |           |
    |           |
    |           |
    |    UNO!   |
    |           |
    |           |
    |___________|
                    ''')
        #Start game (user always starts)
    gameplay = 'y'
    print('\n')
    print("All action cards skip the other player's turn (One player cannot play an action card on top of the other player's to reverse the effect)")
    print('User always starts first')
    print('\n')
    print('\n')
        #Loop for turns, ends if user selects not to play again
    while gameplay != 'n':
            #Load the file containing the official Uno deck
        deckfile = open('uno_deck.txt', 'r')
            #Define deck list
        deck = []
            #Read deck file into list (can't use set and pop cards because deck contains duplicates)
        for line in deckfile:
            deck.append(line.rstrip('\n'))
            #Close deck file
        deckfile.close()
            #Draw hands for CPU and user
        user_hand = []
        user_hand, deck = draw_hand(user_hand, deck)
        cpu_hand = []
        cpu_hand, deck = draw_hand(cpu_hand, deck)
            #Define discard pile
        discard = set()
            #Draw first card from deck
        first_index = random.randint(0, len(deck) - 1)
        card_in_play = deck[first_index]
        card_in_play_list = card_in_play.split()
            #Draw until the starting card is not a wild card or action card, doesn't delete cards from deck list
        while card_in_play_list[0] == 'Wild' or card_in_play_list[1] == 'Reverse' or card_in_play_list[1] == 'Skip' or card_in_play_list[1] == 'Draw':
            first_index = random.randint(0, len(deck) - 1)
            card_in_play = deck[first_index]
            card_in_play_list = card_in_play.split()
        del deck[first_index]
            #Start with user turn
        user_turn = 'y'
        cpu_turn = 'n'
        turns = 'y'
        while turns != 'n' and len(user_hand) != 0 and len(cpu_hand) != 0 and len(deck) != 0:
#User's turn
            while user_turn != 'n' and len(user_hand) != 0 and len(deck) != 0:
                    #Say what the card in play is
                print('\t\t\t'+'The card in play is a', card_in_play)
                print('\n')
                    #Define list of playing options and number of options
                options = []
                option_count = 1
                    #Print hand
                if len(user_hand) == 1:
                    print('UNO!')
                print('Your hand ('+str(len(user_hand))+'):')
                for item in user_hand:
                    print(item)
                    #Choice of what to play
                print('Cards that can be played:')
                match_types = card_in_play.split()
                for card in user_hand:
                        #Split card string into two parts
                    card_list = card.split()
                        #Card with matching first part (color) or matching second part (number) can be played, cards with first part as wild can always be played
                    if card_list[0] == match_types[0] or card_list[1] == match_types[1] or card_list[0] == 'Wild':
                        print(option_count, '----', card)
                        options.append(card)
                        option_count += 1
                    #If user has no cards to play
                if len(options) == 0:
                        #Alert user
                    print('No playable cards')
                    print('autodraw until a card is playable')
                    print('\n')
                        #Draw cards until the user has one to play
                    while len(options) == 0 and len(deck) != 0:
                        user_hand, deck = draw_card(user_hand, deck)
                        for card in user_hand:
                            card_list = card.split()
                            if card_list[0] == match_types[0] or card_list[1] == match_types[1]:
                                print('Your hand ('+str(len(user_hand))+'):')
                                for item in user_hand:
                                    print(item)
                                print('Cards that can be played:')
                                print(option_count, '----', card)
                                options.append(card)
                                option_count += 1
                if len(deck) != 0:
                        #User chooses card to play
                    choice = input('Enter the number to the left of the card you choose to play: ')
                    print('\n')
                        #Input validation, input must be a number and an index in the options list
                    if choice.isdigit() == True and int(choice) in range(1, len(options) + 1):
                            play = options[int(choice) - 1]
                    while choice.isdigit() != True or int(choice) not in range(1, len(options) + 1):
                        choice = input('Enter the number to the left of the card you choose to play: ')
                        print('\n')
                        if choice.isdigit() == True and int(choice) in range(1, len(options) + 1):
                            play = options[int(choice) - 1]
                        #Card chosen is not a wild
                    if play != 'Wild Card' and play != 'Wild Draw Four':
                        play_list = play.split()
                            #Add cards to CPU's hand if card played was a Draw Two
                        if play_list[1] == 'Draw' and len(deck) != 0:
                            for time in range(0, 2):
                                cpu_hand, deck = draw_card(cpu_hand, deck)
                            #Card in play updated with new value
                        card_in_play = play
                            #Card index in hand found and removed
                        play_index = user_hand.index(play)
                        del user_hand[play_index]
                        #Card chosen is a wild, user chooses new color
                    elif play == 'Wild Card':
                            #User chooses color
                        new_color = input('What should the new color be? (r, g, b, y): ')
                            #Input validation
                        while new_color != 'r' and new_color != 'g' and new_color != 'b' and new_color != 'y':
                            print('\n')
                            print('New color must be red (r), green (g), blue (b), or yellow (y)')
                            print('\n')
                            new_color = input('What should the new color be? (r, g, b, y): ')
                            #Interpret input
                        if new_color == 'r':
                            card_in_play = 'Red Wild'
                        elif new_color == 'g':
                            card_in_play = 'Green Wild'
                        elif new_color == 'b':
                            card_in_play = 'Blue Wild'
                        elif new_color == 'y':
                            card_in_play = 'Yellow Wild'
                            #Remove card from hand
                        play_index = user_hand.index(play)
                        del user_hand[play_index]
                        #Card chosen is a wild draw four, user chooses new color and CPU's hand gets four cards added
                    elif play == 'Wild Draw Four':
                            #User chooses color
                        new_color = input('What should the new color be? (r, g, b, y): ')
                            #Input validation
                        while new_color != 'r' and new_color != 'g' and new_color != 'b' and new_color != 'y':
                            print('\n')
                            print('New color must be red (r), green (g), blue (b), or yellow (y)')
                            print('\n')
                            new_color = input('What should the new color be? (r, g, b, y): ')
                            #Interpret input and change value of card in play
                        if new_color == 'r':
                            card_in_play = 'Red Draw Four Wild'
                        elif new_color == 'g':
                            card_in_play = 'Green Draw Four Wild'
                        elif new_color == 'b':
                            card_in_play = 'Blue Draw Four Wild'
                        elif new_color == 'y':
                            card_in_play = 'Yellow Draw Four Wild'
                            #Remove card from hand
                        play_index = user_hand.index(play)
                        del user_hand[play_index]
                            #Add cards to CPU's hand
                        if len(deck) != 0:
                            for time in range(0, 4):
                                cpu_hand, deck = draw_card(cpu_hand, deck)
                    #End user's turn
                user_turn = 'n'
                cpu_turn = 'y'
                    #If user plays action card, skips CPU's turn
                card_in_play_list = card_in_play.split()
                if card_in_play_list[1] == 'Skip' or card_in_play_list[1] == 'Reverse' or card_in_play_list[1] == 'Draw':
                    user_turn = 'y'
                    cpu_turn = 'n'
                    print('\n')
                    print('\t\t\t\t\t\t\t'+"Skipped CPU's turn")
                    print('\n')
                    #If deck is out of cards, game ends
                if len(deck) == 0:
                    turns = 'n'
#CPU's turn
            while cpu_turn != 'n' and len(cpu_hand) != 0 and len(deck) != 0:
                print('\n')
                print('\t\t\t\t\t\t\t'+"CPU's turn")
                if len(cpu_hand) == 1:
                    print('\t\t\t\t\t\t\t'+'UNO!')
                print('\n')
                    #Define list of playing options and number of options
                options = []
                option_count = 1
                    #Choice of what to play
                match_types = card_in_play.split()
                for card in cpu_hand:
                        #Split card string into two parts
                    card_list = card.split()
                        #Card with matching first part (color) or matching second part (number) can be played, cards with first part as wild can always be played
                    if card_list[0] == match_types[0] or card_list[1] == match_types[1] or card_list[0] == 'Wild':
                        options.append(card)
                        option_count += 1
                    #If CPU has no cards to play
                if len(options) == 0:
                        #Draw cards until the CPU has one to play
                    while len(options) == 0 and len(deck) != 0:
                        cpu_hand, deck = draw_card(cpu_hand, deck)
                        for card in cpu_hand:
                            card_list = card.split()
                            if card_list[0] == match_types[0] or card_list[1] == match_types[1]:
                                options.append(card)
                                option_count += 1
                if len(deck) != 0:
                        #CPU chooses card to play through random index
                    choice = random.randint(0, len(options) - 1)
                        #Choice retrieved from options list
                    play = options[choice]
                        #Card chosen is not a wild
                    if play != 'Wild Card' and play != 'Wild Draw Four':
                        play_list = play.split()
                            #Add cards to CPU's hand if card played was a Draw Two
                        if play_list[1] == 'Draw' and len(deck) != 0:
                            for time in range(0, 2):
                                user_hand, deck = draw_card(user_hand, deck)
                            #Card in play value updated to new card
                        card_in_play = play
                            #Card index in hand found and removed
                        play_index = cpu_hand.index(play)
                        del cpu_hand[play_index]
                        #Card chosen is a wild, user chooses new color
                    elif play == 'Wild Card':
                            #CPU chooses color through random index
                        colors = ['r', 'g', 'b', 'y']
                        new_color_index = random.randint(0, 3)
                        new_color = colors[new_color_index]
                            #Interpret input
                        if new_color == 'r':
                            card_in_play = 'Red Wild'
                        elif new_color == 'g':
                            card_in_play = 'Green Wild'
                        elif new_color == 'b':
                            card_in_play = 'Blue Wild'
                        elif new_color == 'y':
                            card_in_play = 'Yellow Wild'
                            #Remove card from hand
                        play_index = cpu_hand.index(play)
                        del cpu_hand[play_index]
                        #Card chosen is a wild draw four, user chooses new color and CPU's hand gets four cards added
                    elif play == 'Wild Draw Four':
                            #CPU chooses color through random index
                        colors = ['r', 'g', 'b', 'y']
                        new_color_index = random.randint(0, 3)
                        new_color = colors[new_color_index]
                            #Interpret input and change value of card in play
                        if new_color == 'r':
                            card_in_play = 'Red Draw Four Wild'
                        elif new_color == 'g':
                            card_in_play = 'Green Draw Four Wild'
                        elif new_color == 'b':
                            card_in_play = 'Blue Draw Four Wild'
                        elif new_color == 'y':
                            card_in_play = 'Yellow Draw Four Wild'
                            #Remove card from hand
                        play_index = cpu_hand.index(play)
                        del cpu_hand[play_index]
                            #Add cards to User's hand
                        if len(deck) != 0:
                            for time in range(0, 4):
                                user_hand, deck = draw_card(user_hand, deck)
                    #End CPU's turn
                user_turn = 'y'
                cpu_turn = 'n'
                print('\t\t\t\t\t\t'+'CPU ends turn with', str(len(cpu_hand)), 'cards')
                print('\n')
                    #If CPU played action card, skips user's turn
                card_in_play_list = card_in_play.split()
                if card_in_play_list[1] == 'Skip' or card_in_play_list[1] == 'Reverse' or card_in_play_list[1] == 'Draw':
                    user_turn = 'n'
                    cpu_turn = 'y'
                    print('\n')
                    print("Skipped User's turn")
                    print('\n')
                    #If deck is out of cards, game ends
                if len(deck) == 0:
                    turns = 'n'
            #Did the deck run out of cards?
        if len(deck) == 0:
            print('The deck ran out of cards')
            print('\n')
            #Who won?
        if len(user_hand) < len(cpu_hand) or len(user_hand) == 0:
            print('User won with '+str(len(user_hand))+' cards left, CPU had '+str(len(cpu_hand))+' cards left')
            print('\n')
        if len(user_hand) > len(cpu_hand) or len(cpu_hand) == 0:
            print('CPU won with '+str(len(cpu_hand))+' cards left, User had '+str(len(user_hand))+' cards left')
            print('\n')
        if len(user_hand) == len(cpu_hand):
            print('Tie game')
            #Ask to play again
        play_again = input('Do you want to play again? (Yes or No): ')
            #Input validation
        while play_again != 'Yes' and play_again != 'No':
            print('Type either "Yes" or "No"')
            play_again = input('Do you want to play again? (Yes or No): ')
            #Play again
        if play_again == 'Yes':
            gameplay = 'y'
            print('\n')
            #Don't play again
        if play_again == 'No':
            gameplay = 'n'
            print('\n')
            print('Exiting game')



    #Used at the start of a new game to populate the CPU and user hand lists with card strings. Gets an empty list, adds 7 card strings from the deck list and deletes them from the
    #deck list. Returns the list with 7 card strings
def draw_hand(hand, deck_list):
    for draw in range(0, 7):
        index = random.randint(0, len(deck_list) - 1)
        card = deck_list[index]
        del deck_list[index]
        hand.append(card)
    return hand, deck_list



    #Used to add a card to a hand if no card can be played and for Draw X cards. Gets hand and deck list, adds a random card from the deck list to the hand based on index, deletes the index from the
    #deck list, returns the hand with a new card and the deck list without the drawn card
def draw_card(hand, deck_list):
    index = random.randint(0, len(deck_list) - 1)
    card = deck_list[index]
    del deck_list[index]
    hand.append(card)
    return hand, deck_list



main()
