"""
This program implements a simple version of the game "Twenty One" 
(also known as Blackjack).
It includes functions to deal cards, 
# calculate scores, 
# and determine the winner.

The player can ether hit or stay 
and the game continues until the player decides to stay
or exceeds a score of TARGET_SCORE.
"""
import time
import os
import random

MATCH_WIN_COUNT = 5
PAUSE_TIME = 1
TARGET_SCORE = 21
DEALER_MIN_HIT = 17

YES_RESPONSES = {'y', 'yes', 'sure', 'ok', 'yeah'}
NO_RESPONSES = {'n', 'no', 'nope', 'nah'}
HIT_RESPONSES = {'h', 'hit'}
STAY_RESPONSES = {'s', 'stay'}

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

def clear_screen():
    """
    Clears the console screen.
    This function is used to keep the console output clean.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
def prompt(message):
    """
    Prints a message to the console.
    PARAM: message: str - The message to print.
    
    Prints the message with ==> prefixed to it."""
    print(f"=> {message}")

def initialize_deck():
    """
    Initializes a standard deck of 52 playing cards.
    Returns a shuffled list of cards in the format 'value+suit'.
    """
    deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(deck)
    return deck

def total(cards):
    """
    Calculates the total value of a hand of cards.
    PARAM: cards: A list of cards in the format 'value+suit'.
    RETURNS: The total value of the hand.
    """
    sum_val = 0

    for card in cards:
        value = card[:-1]

        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # Correct for Aces
    for card in cards:
        value = card[:-1]
        if sum_val <= TARGET_SCORE:
            break
        if value == "A":
            sum_val -= 10

    return sum_val

def is_busted(total_score):
    """
    Checks if the total score exceeds the TARGET_SCORE.
    PARAM: cards: A list of cards in the format 'value+suit'.
    RETURNS: True if the total value exceeds TARGET_SCORE, False otherwise.
    """
    return total_score > TARGET_SCORE

def detect_result(dealer_total, player_total):
    """
    Determines the result of the game based on the dealer's and player's hands.
    PARAM: dealer_cards: A list of cards for the dealer.
    PARAM: player_cards: A list of cards for the player.

    RETURNS: A string indicating the result of the game.
    """
    if player_total > TARGET_SCORE:
        return 'PLAYER_is_busted'
    if dealer_total > TARGET_SCORE:
        return 'DEALER_is_busted'
    if dealer_total < player_total:
        return 'PLAYER'
    if dealer_total > player_total:
        return 'DEALER'
    return 'TIE'

def display_results(dealer_total, player_total):
    """
    Displays the results of the game based on the dealer's and player's hands.
    PARAM: dealer_cards: A list of cards for the dealer.
    PARAM: player_cards: A list of cards for the player.
    """
    result = detect_result(dealer_total, player_total)

    match result:
        case 'PLAYER_is_busted':
            prompt('You BUSTED! Dealer wins!')
        case 'DEALER_is_busted':
            prompt('Dealer BUSTED! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")

def play_again():
    """
    Asks the user if they want to play again. Handles flexible input.
    Returns True if yes, False if no.
    """
    while True:
        print("-------------")
        answer = input('Do you want to play again? (y/n): ').strip().lower()
        if answer in YES_RESPONSES:
            return True
        if answer in NO_RESPONSES:
            return False
        prompt("Invalid input. Please enter yes or no.")

def pop_two_from_deck(deck):
    """
    Pops two cards from the deck.
    PARAM: deck: A list representing the deck of cards.
    RETURNS: A list containing two cards popped from the deck.
    """
    return [deck.pop(), deck.pop()]

def hand(cards):
    """
    Formats a list of cards into a string representation.
    PARAM: cards: A list of cards in the format 'value+suit'.
    RETURNS: A string representation of the cards
    """
    return ', '.join(cards)

def player_turn(deck, player_cards):
    """
    Manages player's turn.
    Returns (bool, int): False if player busts, True otherwise; final total.
    """
    while True:
        choice = input("Hit or stay? (h/s): ").strip().lower()
        if choice in HIT_RESPONSES:
            player_cards.append(deck.pop())
            current_total = total(player_cards)
            prompt(f"Your cards: {hand(player_cards)}")
            prompt(f"Your total: {current_total}")
            if is_busted(current_total):
                prompt("You're BUSTED!")
                return False, current_total
        elif choice in STAY_RESPONSES:
            current_total = total(player_cards)
            return True, current_total
        else:
            prompt("Invalid input. Please enter 'hit' or 'stay'.")


def dealer_turn(deck, dealer_cards):
    """
    Manages the dealer's turn in the game.
    The dealer hits until their total is DEALER_MIN_HIT or more.
    
    PARAM: deck: A list representing the deck of cards.
    PARAM: dealer_cards: A list of cards in the dealer's hand.

    RETURNS: True if the dealer does not bust, 
    False if the dealer busts.
    """
    while True:
        total_score = total(dealer_cards)
        if total_score >= DEALER_MIN_HIT:
            return True, total_score
        dealer_cards.append(deck.pop())
        prompt(f"Dealer hits: {hand(dealer_cards)}")

def show_end_of_round(dealer_cards, player_cards, dealer_total, player_total):
    """
    Displays final hand summaries for both dealer and player
    along with the result message.
    """
    print('==============')
    prompt(f"Dealer has {hand(dealer_cards)}, total: {dealer_total}")
    prompt(f"Player has {hand(player_cards)}, total: {player_total}")
    print('==============')

    display_results(dealer_total, player_total)


def play_twenty_one():
    """
    Main function to play the game of Twenty-One.
    The game continues until either the player or dealer reaches 5 wins,
    declaring a match victory. 
    The user can then choose to play again or quit.
    """
    player_wins = 0
    dealer_wins = 0

    while True:
        clear_screen()
        prompt('Welcome to Twenty-One!')

        deck = initialize_deck()
        player_cards = pop_two_from_deck(deck)
        dealer_cards = pop_two_from_deck(deck)

        player_total = total(player_cards)
        dealer_total = total(dealer_cards)

        prompt(f"Dealer has {dealer_cards[0]} and ?")
        prompt(f"You have: {hand(player_cards)}, total: {player_total}")

        # Player's Turn
        prompt("Your turn...")
        player_survived, player_total = player_turn(deck, player_cards)

        if not player_survived:
            dealer_total = total(dealer_cards)
        else:
            prompt(f"You stayed at {player_total}")
            prompt("Dealer's turn...")
            _, dealer_total = dealer_turn(deck, dealer_cards)
            prompt(f"Dealer stays at {dealer_total}")

        # Final summary & result
        show_end_of_round(dealer_cards, player_cards, dealer_total, player_total)

        result = detect_result(dealer_total, player_total)
        if result in ['PLAYER', 'DEALER_is_busted']:
            player_wins += 1
        elif result in ['DEALER', 'PLAYER_is_busted']:
            dealer_wins += 1


        # Show current score
        print(f"Scoreboard: Player {player_wins} | Dealer {dealer_wins}\n")

        # Match check
        if player_wins == MATCH_WIN_COUNT:
            prompt("You won the match! Even though you will lose in the long run...\n")
            player_wins = dealer_wins = 0
            if play_again():
                time.sleep(PAUSE_TIME)
                continue
            break
        if dealer_wins == MATCH_WIN_COUNT:
            prompt("Dealer won the match. Better learn to count cards!")
            player_wins = dealer_wins = 0
            if play_again():
                time.sleep(PAUSE_TIME)
                continue
            break

        # Ask if user wants to keep playing round-to-round
        if play_again():
            time.sleep(PAUSE_TIME)
            continue
        break

play_twenty_one()
