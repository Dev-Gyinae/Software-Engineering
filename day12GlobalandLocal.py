# Global scope is mostly denoted by capital letters

# Guess the number 
import random

def check_guess(guess, num_choice, attempts):
    if guess > num_choice:
        print("📈 Too high")
        return attempts - 1
    elif guess < num_choice:
        print("📉 Too low")
        return attempts - 1
    else:
        print(f"🎉 You got it! The answer was {num_choice} 🎉")
        return 0

def play_game():
    print("\n" + "="*50)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    print("="*50)
    
    EASY = 10
    HARD = 5
    
    # Difficulty selection with validation
    while True:
        difficulty = input('\nChoose a difficulty: "easy" or "hard": ').lower()
        if difficulty == "easy":
            attempts = EASY
            break
        elif difficulty == "hard":
            attempts = HARD
            break
        else:
            print("Invalid input! Please type 'easy' or 'hard'.")
    
    num_choice = random.randint(1, 100)
    
    # Game loop
    while attempts > 0:
        print(f"\n💡 You have {attempts} attempts remaining.")
        
        # Input validation for guess
        while True:
            try:
                guess = int(input("🔢 Make a guess: "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please guess a number between 1 and 100!")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        attempts = check_guess(guess, num_choice, attempts)
        
        if attempts == 0:
            if guess != num_choice:
                print(f"\n💀 You've run out of guesses. You lose! The number was {num_choice} 💀")
            break

# Play the game
play_game()

# Ask to play again
while True:
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print("\nThanks for playing! Goodbye! 👋")
        break
    else:
        print("Invalid input! Type 'y' or 'n'.")