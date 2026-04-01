import random

# names_string = input("Give me everybody's names, separated by a comma. \n")

# names = names_string.split(", ")

# # selected = names[random.randint(0, len(names))]

# selected = random.choice(names)

# print(f"{selected} is paying for the meal")


###############################################3333
# RPS - Version 1
import random

# List of choices with proper formatting
choices = ["Rock", "Paper", "Scissors"]

print('Welcome to the RPC game')
player = input("What is your name? \n:: ")
print(f"Hello {player}, let's play Rock, Paper, Scissors!")

# Get player's choice
player_input = int(input("Select: \n '1' for rock \n '2' for paper \n '3' for scissors'\n:: "))
player_choice_name = choices[player_input - 1]

# Get computer's choice
computer_options = ["1", "2", "3"]
computer_choice_num = int(random.choice(computer_options))
computer_choice_name = choices[computer_choice_num - 1]

if player_input == computer_choice_num:
    print(f"It's a tie:\n {player} chose {player_choice_name} and Computer chose {computer_choice_name}")
elif player_input == 1 and computer_choice_num == 3:
    print(f"Player Won:\n {player} chose {player_choice_name} and Computer chose {computer_choice_name}")
elif player_input == 2 and computer_choice_num == 1:
    print(f"Player Won:\n {player} chose {player_choice_name} and Computer chose {computer_choice_name}")
elif player_input == 3 and computer_choice_num == 2:
    print(f"Player Won:\n {player} chose {player_choice_name} and Computer chose {computer_choice_name}")
else:
    print(f"Computer Won:\n {player} chose {player_choice_name} and Computer chose {computer_choice_name}")