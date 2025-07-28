# Attention: any line starting with # is a comment and is not executed by the program

# Examples using the while statement
# Warning: if the loop is infinite, press Ctrl+C in the terminal to stop it

# Example 1

# Display the numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i = i + 1  # If this line is missing, the loop will be infinite


# Example 2
# With input

# Display the numbers from 1 up to the number the user provides
i = 1
number = int(input("Enter a number: "))
while i <= number:
    print(i)
    i = i + 1  # If this line is missing, the loop will be infinite
