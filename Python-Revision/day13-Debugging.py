# Essential part of codding
# Debugging is the process of finding and fixing errors in your code.
# Common types of errors include:
# Syntax errors: These occur when you write code that does not follow the rules of the programming
# language. For example, forgetting to close a parenthesis or using the wrong indentation.
# Runtime errors: These occur when your code is running and encounters a problem. For example,
# trying to divide by zero or accessing an index that is out of range.
# Logical errors: These occur when your code runs without crashing but produces incorrect results.
# To debug your code, you can use print statements to check the values of variables at different
# points in your code. You can also use a debugger tool that allows you to step through
# your code line by line and inspect the values of variables.
# Here are some tips for debugging your code:
# 1. Read the error message carefully: The error message can give you clues about what went wrong and where to look in your code.
# 2. Use print statements: Insert print statements at different points in your code to check the values of variables and see where the error occurs.
# 3. Use a debugger: A debugger allows you to step through your code line by line and inspect the values of variables. This can help you identify where the error occurs and what is causing it.
# 4. Check your logic: If your code runs without crashing but produces incorrect results, check your logic to see if you are using the correct algorithms and data structures.
# 5. Take a break: Sometimes, stepping away from your code for a while can help you see the problem from a fresh perspective and come up with new ideas for how to fix it.
# Example of debugging code
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a / b 
# Test the function
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Cannot divide by zero

