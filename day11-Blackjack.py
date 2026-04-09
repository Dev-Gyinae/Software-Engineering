# Blackjack Capstone Project
import random
import os

def clear():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a hand without modifying the original hand."""
    temp_hand = hand.copy()
    
    if sum(temp_hand) == 21 and len(temp_hand) == 2:
        return 0  # Blackjack
    
    if 11 in temp_hand and sum(temp_hand) > 21:
        temp_hand.remove(11)
        temp_hand.append(1)
    
    return sum(temp_hand)

def compare(player_score, dealer_score, player_hand, dealer_hand):
    """Compares the player's score with the dealer's score and returns the result."""
    # Check for Blackjack first
    if player_score == 0 and dealer_score == 0:
        return "Both have Blackjack! It's a draw! 🤝"
    elif player_score == 0:
        return "You win with a Blackjack! 🎉💰"
    elif dealer_score == 0:
        return "Dealer has Blackjack! You lose! 😱"
    elif player_score > 21:
        return "You went over. You lose! 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win! 🎉"
    elif player_score > dealer_score:
        return "You win! 🎉"
    elif player_score < dealer_score:
        return "You lose! 😭"
    else:
        return "It's a draw! 🤝"

def play_game():
    """Plays a single round of Blackjack."""
    print("Welcome to Blackjack!")
    
    player_hand = []
    dealer_hand = []
    
    # Deal initial cards
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())
    
    game_over = False
    
    # Player's turn
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f"\nYour hand: {player_hand}, current score: {player_score if player_score != 0 else 'Blackjack!'}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        
        # Check if player has Blackjack or busted immediately
        if player_score == 0:
            print("\n🎉 You have Blackjack! 🎉")
            game_over = True
        elif player_score > 21:
            print("\n💥 You busted! 💥")
            game_over = True
        else:
            should_continue = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True
    
    # Dealer's turn (only if player hasn't busted and doesn't have Blackjack)
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    if player_score <= 21 and player_score != 0:
        print("\n" + "="*40)
        print("Dealer's turn...")
        print("="*40)
        
        # Reveal dealer's full hand
        print(f"Dealer reveals: {dealer_hand}, score: {dealer_score if dealer_score != 0 else 'Blackjack!'}")
        
        # Dealer draws cards according to rules
        while dealer_score < 17 and dealer_score != 0:
            input("\nPress Enter to continue...")
            dealer_hand.append(deal_card())
            dealer_score = calculate_score(dealer_hand)
            print(f"Dealer draws a card: {dealer_hand[-1]}")
            print(f"Dealer's hand: {dealer_hand}, score: {dealer_score if dealer_score != 0 else 'Blackjack!'}")
    
    # Final scores and comparison
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    print("\n" + "="*40)
    print("FINAL RESULTS")
    print("="*40)
    print(f"Your final hand: {player_hand}, final score: {player_score if player_score != 0 else 'Blackjack!'}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score if dealer_score != 0 else 'Blackjack!'}")
    print("="*40)
    print(compare(player_score, dealer_score, player_hand, dealer_hand))
    print("="*40 + "\n")

# Main game loop
print("🎰 Welcome to Blackjack Casino! 🃏\n")

while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    if play_again == 'y':
        clear()
        play_game()
    elif play_again == 'n':
        print("\nThanks for playing! Goodbye! 👋")
        break
    else:
        print("Invalid input! Please type 'y' or 'n'.")