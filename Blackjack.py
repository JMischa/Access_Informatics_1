__author__ = "Mischa Jampen"
import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Define a function to create a deck of cards
def create_deck():
    deck = [{'Suit': suit, 'Rank': rank, 'Value': values[rank]} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Define a function to visualize a card
def visualize_card(card):
    suit = card['Suit'][0]
    rank = card['Rank'][0]
    return f"┌───────┐\n| {rank: <2}    |\n|   {suit}   |\n|    {rank: >2} |\n└───────┘"

# Define a function to display a hand
def display_hand(hand):
    for card in hand:
        print(visualize_card(card), end=' ')
    print()

# Define a function to calculate the hand value
def hand_value(hand):
    value = sum(card['Value'] for card in hand)
    num_aces = sum(1 for card in hand if card['Rank'] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Initialize the game
deck = create_deck()
player_hand = []
dealer_hand = []

# Deal two cards to the player and dealer
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# Main game loop
while True:
    print("\nPlayer's Hand:")
    display_hand(player_hand)
    player_value = hand_value(player_hand)
    print(f"Total Value: {player_value}")

    print("\nDealer's Hand:")
    print(visualize_card(dealer_hand[0]), "Unknown Card")
    
    if player_value == 21:
        print("Congratulations! You have a Blackjack!")
        break

    action = input("\nDo you want to Hit or Stand? ").lower()
    if action == 'hit':
        player_card = deck.pop()
        player_hand.append(player_card)
        print("You drew a card:\n", visualize_card(player_card))
        if hand_value(player_hand) > 21:
            print("Bust! You went over 21. Dealer wins.")
            break
    elif action == 'stand':
        while hand_value(dealer_hand) < 17:
            dealer_card = deck.pop()
            dealer_hand.append(dealer_card)
            print("Dealer drew a card:\n", visualize_card(dealer_card))
        print("\nDealer's Hand:")
        display_hand(dealer_hand)
        dealer_value = hand_value(dealer_hand)
        print(f"Total Value: {dealer_value}")

        if dealer_value > 21:
            print("Dealer busts! You win.")
        elif dealer_value > player_value:
            print("Dealer wins.")
        elif dealer_value < player_value:
            print("You win!")
        else:
            print("It's a push (tie)!")
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")
