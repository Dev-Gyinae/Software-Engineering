# High Low Game
import random
print("Welcome to the High-Low Game!")
Difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if Difficulty == "easy":
    attempts = 10
elif Difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Defaulting to 'easy'.")
    attempts = 10

number = random.randint(1,100)
print(f"You have {attempts} attempts to guess the number between 1 and 100.")
while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        break
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining. Try again.")
    else:
        print(f"Game Over! The correct number was {number}.")

