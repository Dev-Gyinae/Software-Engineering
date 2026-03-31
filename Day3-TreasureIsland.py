# Modulo

# statement = int(input("enter a number to check if it's odd or even\n"))

# if statement % 2 == 0:
#     print("it's an even number")
# else:
#     print("it's an odd number")

#######################################################################

# BMI CALCULATOR
# print('Welcome to BMI calculator')

# height = float(input("What is your height in m:\n"))
# weight = float(input("What is your weight in kg:\n"))

# BMI = round(weight / height**2, 2)

# if BMI < 18.5:
#     print(f'Your BMI is {BMI} which is less than 18.5 so you are underweight')
# elif BMI < 25:
#     print(f'Your BMI is {BMI}Your weight is normal')
# elif BMI < 30:
#     print(f'Your BMI is {BMI} You are fat ')
# elif BMI < 35:
#     print(f'Your BMI is {BMI} you are really fat')
# else:
#     print(f'God damn! Your BMI is {BMI}')

#######################################################################

# Leap Year Calculator 
# so 4 years is a standard but for 100 years to pass it must also pass 400 years

# year = int(input('Enter a year:\n'))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not Leap')
#     else:
#         print("Leap year")
# else:
#     print('Not Leap')

#######################################################################

# Pizza Order

# print('Welcome to Code Pizza')


# size = input("Which size of Pizza:\n 'S', 'M', 'L': \n ").lower()
# add_pepperoni = input("Do you want Pepperoni? 'Y','N'\n").lower()
# add_cheese = input("Do you want Pepperoni? 'Y','N'\n").lower()

# if size == str('s'):
#     bill = 15
# elif size == str('m'):
#     bill = 20
# elif size == str('l'):
#     bill = 25

# if add_pepperoni == str('y'):
#     if size == str('s'):
#         bill += 2
#     else:
#         bill += 3

# if add_cheese == str('y'):
#     bill += 1

# print(f"Your final bill is: ${bill}")   


#####################################################################3
# Love Calculator

# print("Welcome to the Love Calculator")

# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower() 
# combined_names = name1 + name2
# true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
# love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')
# love_score = int(str(true_count) + str(love_count))

# t_count = combined_names.count('t')
# r_count = combined_names.count('r')
# u_count = combined_names.count('u')
# e_count = combined_names.count('e') 

# l_count = combined_names.count('l')
# o_count = combined_names.count('o')
# v_count = combined_names.count('v')
# e_count = combined_names.count('e')

# print(f"Count of 't': {t_count}")
# print(f"Count of 'r': {r_count}")
# print(f"Count of 'u': {u_count}")          
# print(f"Count of 'e': {e_count}")
# print(f"Count of 'l': {l_count}")
# print(f"Count of 'o': {o_count}")
# print(f"Count of 'v': {v_count}")
# print(f"Count of 'e': {e_count}")   


# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:    print(f"Your score is {love_score}.")  


##############################################################################

# Treasure Island

print("Welcome to Treasure Island.Your mission is to find the treasure")

Starter = input(" Choose your path: \n Left or Right ").lower()

if Starter == "right":
    choice = input("You are infront of a lake what do you? \n A: Swim \n B: Wait for the boat ").lower()
    if choice == "b":
        door = input("You are ashore choose 'Red Door' , 'Blue Door', or 'Green Door'").lower()
        if door == "blue door":
            print('Congrats you found the one piece')
        elif door == "green door":
            print('You got caught in a gengitsu. Game Over')
        elif door == 'red door':
            print('You had to fight Brock Lesnar! Game Over')
        else:
            print('You got killed by Edward Black Beard Teach')
    else:
        print("Game Over! You got eaten by a crocodile")
else:
    print("You fell into a pit! Try Again")