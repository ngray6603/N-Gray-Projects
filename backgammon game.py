# April 17, 2024
# Nicole Gray
# Final Project

# When beginning the project, the following questions were considered:
# 1) What is the input data?
# The input data for the backgammon game will be the starting value for each hand, which will range from 4-22
# 2) What is the output of the problem?
# The output will be the results of the table. It will declare if the player wins, loses, or has a draw.
# The results the value when the player chooses to hit or stand with the dealer.
# There will also be values from win, loss, draw when the player hits or stands.
# 3) How can I solve it using functions, classes, loops or else statements?
# This can be solved with the function action for hitting, standing and when cards are dealt.
# Classes will be used for the player, dealer, and cards
# Loops will be used to go through the hands to determine the results
# Condition statements will be used for the rules
# 4) What is the structure for this program code?
# The structure will have classes for the player, dealer, and cards.
# The function will be dealing the cards and loops will be playing multiple hands of the game
# The condition will be the game rules that are used throughout.

# Python definitions:
# Define a class for the deck of cards
# Import the random module to shuffle the deck of cards
# April 17, 2024
# Nicole Gray
# Final Project
# April 17, 2024
# Nicole Gray
# Final Project

import random
import matplotlib.pyplot as plt

# Define the ranks and suits of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


# Define a function to create and shuffle a deck of cards
def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


# Define a function to calculate the value of a card hand
def calculate_hand_value(hand):
    total_value = 0
    num_aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            total_value += 10
        elif card[0] == 'A':
            total_value += 11
            num_aces += 1
        else:
            total_value += int(card[0])
    while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1
    return total_value


# Define a function to display a hand
def display_hand(hand, player_name):
    print(player_name + "'s Hand:", [card[0] for card in hand])
    print(player_name + "'s Hand Value:", calculate_hand_value(hand))


# Define a function for the player's turn
def player_turn(deck, player_hand, computer_hand):
    print("Dealer's Hand:", [card[0] for card in computer_hand])
    print("Dealer's Hand Value:", calculate_hand_value(computer_hand))
    display_hand(player_hand, "Player")

    while calculate_hand_value(player_hand) < 17:
        player_hand.append(deck.pop())
        display_hand(player_hand, "Player")


# Define a function for the computer's turn
def computer_turn(deck, computer_hand):
    while calculate_hand_value(computer_hand) < 17:
        computer_hand.append(deck.pop())


# Define a function to determine the winner
def determine_winner(player_hand, computer_hand):
    player_value = calculate_hand_value(player_hand)
    computer_value = calculate_hand_value(computer_hand)

    if player_value > 21:
        return "Computer Wins"
    elif computer_value > 21:
        return "You Win"
    elif player_value > computer_value:
        return "You Win"
    elif player_value < computer_value:
        return "Computer Wins"
    else:
        return "Draw"


# Main function to run the game
def play_blackjack(num_games):
    player_wins = 0
    computer_wins = 0
    draws = 0
    for _ in range(num_games):
        deck = create_deck()

        player_hand = [deck.pop(), deck.pop()]
        computer_hand = [deck.pop(), deck.pop()]

        player_turn(deck, player_hand, computer_hand)
        computer_turn(deck, computer_hand)

        outcome = determine_winner(player_hand, computer_hand)
        if outcome == "You Win":
            player_wins += 1
        elif outcome == "Computer Wins":
            computer_wins += 1
        else:
            draws += 1

    print("Results after", num_games, "games:")
    print("Player Wins:", player_wins)
    print("Computer Wins:", computer_wins)
    print("Draws:", draws)

    # Generate a chart
    labels = ['Player Wins', 'Computer Wins', 'Draws']
    values = [player_wins, computer_wins, draws]

    plt.bar(labels, values)
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.title('Blackjack Simulation Results')
    plt.show()


# Run the game with 100,000 simulations
if __name__ == "__main__":
    play_blackjack(100000)