# import random

# names_string = input("Give me everybody's names, separated by a comma. \n")

# names = names_string.split(", ")

# # selected = names[random.randint(0, len(names))]

# selected = random.choice(names)

# print(f"{selected} is paying for the meal")


###############################################3333
# RPS - Version 1

import random

Game_Names = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(1,3)
print("Welcome to Rock, Paper, Scissors")
Player = input("Enter Your Name: \n")
player_choice =  int(input("Choose '1: for Rock, 2: for Paper, 3: for Scissors:\n'"))


if player_choice < 1 or player_choice > 3:
     print("Wrong Input! Game Over!")
else:
    if player_choice == computer_choice:
        print(f"You both chose {Game_Names[player_choice -1]} It's a Tie")
    elif player_choice == 1 and computer_choice == 3:
        print(f"{Player} Wins: {Player} Chose: {Game_Names[player_choice -1]} and Computer Chose: {Game_Names[computer_choice - 1]}!")
    elif player_choice == 2 and computer_choice == 1:
        print(f"{Player} Wins: {Player} Chose: {Game_Names[player_choice -1]} and Computer Chose: {Game_Names[computer_choice - 1]}!")
    elif player_choice == 3 and computer_choice == 2:
        print(f"{Player} Wins: {Player} Chose: {Game_Names[player_choice -1]} and Computer Chose: {Game_Names[computer_choice - 1]}")
    else:
        print(f"Computer Wins: Computer Chose: {Game_Names[computer_choice - 1]} and {Player} Chose: {Game_Names[player_choice -1]}!")
