# Attention: any line starting with # is a comment and is not executed by the program

# Examples using if, elif, else

# Example 1

if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")


# Example 2 with elif

if 5 > 2:
    print("5 is greater than 2")
elif 5 < 2:
    print("5 is less than 2")
else:
    print("5 is equal to 2")


# Example 3, with variables

a = 5
b = 2

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")


# Example 4, with variables and multiple elif

a = 5
b = 5

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is neither greater, nor less, nor equal to b")


# Example 5, with input

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is neither greater, nor less, nor equal to b")
