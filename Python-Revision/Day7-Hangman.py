# Hangman
import random

word = ["python", "programming", "hangman", "challenge", "developer", "algorithm", 
        "function", "variable", "syntax", "debugging", "iteration", "recursion", "inheritance", "polymorphism", "encapsulation", "abstraction", "data", "structure", "object", "oriented", "design", "pattern", "software", "engineering",
        "testing", "version", "control", "repository", "collaboration", "deployment", "cloud", "computing", "artificial", "intelligence", "machine", "learning", "deep", "neural", "network", "natural", "language", "processing"]
selected_word = random.choice(word)
life = 5

print("\n \nWelcome to Hangman: You have 5 guesses to complete this word challenge: \n")
print("Guess the word! - The word has", len(selected_word), "letters.\n")

# Create the dashes for the word
current_display = "_" * len(selected_word)
print(current_display)

# Game loop
while life > 0 and "_" in current_display:
    player_input = input("\nEnter a letter:\n").lower()
    
    # Check if letter is in the word
    if player_input in selected_word:
        # Update the display with the correct letter
        new_display = ''
        for string in range(len(selected_word)):
            if selected_word[string] == player_input:
                new_display += player_input
            else:
                new_display += current_display[string]
        current_display = new_display
        print(f"\nGood guess! {current_display}")
    else:
        life -= 1
        print(f"\nWrong guess! You have {life} lives left.")
        print(current_display)

# Game over message
if "_" not in current_display:
    print(f"\n🎉 Congratulations! You guessed the word: {selected_word}")
else:
    print(f"\n💀 Game Over! The word was: {selected_word}")