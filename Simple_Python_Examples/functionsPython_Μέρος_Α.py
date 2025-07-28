# Examples of functions in Python

# First Example

# A simple function that prints the word "Hello"

# This is the body of the function, it contains the function's code. If we don't call it, Python won't execute it.
# Pay attention to the syntax.
def hello():
    print("First Example")
    print("Hello")

# Here we call the function, so Python will execute the code inside it
hello()

# Second Example

# A function that returns a random number

# This is the body of the function, it contains the function's code. If we don't call it, Python won't execute it.
# Pay attention to the syntax.
def randomNumber():
    print("\nSecond Example")
    return 20

# Here we call the function, so Python will execute the code inside it
# WARNING! Since the function returns a value, we cannot just call it (like in the example above).
# We must either print it or use it in a command/variable.
print(randomNumber())

# Third Example

# A function that receives two values from the user and displays their sum

# This is the body of the function, it contains the function's code. If we don't call it, Python won't execute it.
# Pay attention to the syntax.
def sumOfTwoNumbers():
    print("\nThird Example")
    n1 = int(input("Give me the first number: "))  # Note: we added int because the input must be an integer
    n2 = int(input("Give me the second number: ")) # Note: we added int because the input must be an integer
    print(n1 + n2)  # Here we display their sum

# We can call it directly since it doesn't return a value
sumOfTwoNumbers()

# Fourth Example

# A function that receives two values from the user and returns their sum

# This is the body of the function, it contains the function's code. If we don't call it, Python won't execute it.
# Pay attention to the syntax.
def sumOfTwoNumbers():
    print("\nFourth Example")
    n1 = int(input("Give me the first number: "))  # Note: we added int because the input must be an integer
    n2 = int(input("Give me the second number: ")) # Note: we added int because the input must be an integer
    return n1 + n2  # Here we return their sum, which can be done in many ways

# Here we call the function, so Python will execute the code inside it
# WARNING! Since the function returns a value, we cannot just call it (like in the previous example).
# We must either print it or use it in a command/variable.
print(sumOfTwoNumbers())
