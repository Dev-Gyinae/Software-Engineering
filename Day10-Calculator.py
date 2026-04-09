#Calculator

def add(x, y):
    return x + y    
def subtract(x, y):
    return x - y    
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")



# Docstring

# The docstring is a string literal that occurs as the first statement in a module,
# function, class, or method definition. It is used to document the purpose and usage of the code.
# In this example, the docstring for the add function explains that it adds two numbers.
# It is denoted by triple quotes (""" """) and can be accessed using the __doc__ attribute of the function.

# Example of a docstring for the add function:
# def add(x, y):
#     """This function adds two numbers."""
#     return x + y