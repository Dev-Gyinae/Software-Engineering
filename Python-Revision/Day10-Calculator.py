#Calculator
def add(x, y):
    """This function adds two numbers."""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y     

def divide(x, y):
    """This function divides two numbers."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


x = float(input("Enter first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the list above: ")
y = float(input("Enter second number: "))

calculation_function = operations[operation_symbol]
result = calculation_function(x, y)
print(f"{x} {operation_symbol} {y} = {result}")


# Docstring

# The docstring is a string literal that occurs as the first statement in a module,
# function, class, or method definition. It is used to document the purpose and usage of the code.
# In this example, the docstring for the add function explains that it adds two numbers.
# It is denoted by triple quotes (""" """) and can be accessed using the __doc__ attribute of the function.

# Example of a docstring for the add function:
# def add(x, y):
#     """This function adds two numbers."""
#     return x + y