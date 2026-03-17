import random

# Player input
player_choice = input('.. enter \n 1 for rock \n 2 for paper \n 3 for scissor \n .....')
choice = int(player_choice)

# Validation
if choice < 1 or choice > 3:
    print('start again')
else:
    # map number to word
    names = {'1': 'rock', '2': 'paper', '3': 'scissor'}
    print(f'player chose {names[player_choice]}')

# Computer choice
computer_choice = random.choice(['1', '2', '3'])
print(int(computer_choice))
print(f'computer chose {names[computer_choice]}')

# Winner logic
if player_choice == computer_choice:
    print('its a draw')
elif player_choice == '1' and computer_choice == '3':
    print('player won')
elif player_choice == '2' and computer_choice == '1':
    print('player won')
elif player_choice == '3' and computer_choice == '2':
    print('player won')
else:
    print('computer won')

'''rock beats scissor, scissor beats paper, paper beats rock'''
