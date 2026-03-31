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