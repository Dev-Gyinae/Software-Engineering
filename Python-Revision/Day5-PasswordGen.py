# even_number = 0
# for num in range(1, 101):
#     if num % 2 ==0:
#         even_number += num

# print(even_number)


######################################3
# Fizz Buzz

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizz buzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)

############################################3
# Password Generator 
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'
print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_num = ''
password_sym = ''
password_let = ''
for char in range(1, nr_letters + 1):
    password_let += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_sym += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_num += random.choice(numbers)

passw = (password_num + password_sym + password_let)  
print(f"your password is {passw}")

# shuffle requires a list
strong_pass_list = list(passw)
random.shuffle(strong_pass_list)
# join the list back to a string
strong_pass = ''.join(strong_pass_list)

print(f"your shuffled (strong) password is {strong_pass}")