# Attention: any line starting with # is a comment and is not executed by the program

# Examples with input and typecasting (Read the theory first)

name = input("Enter your name: ")
print("Hello " + name)

age = input("Enter your age: ")
print("You are " + age + " years old")  # The variable age is of type string (i.e., text)

age = int(input("Enter your age: "))  # Convert the variable age to integer type
print(age)  # The variable age is now of type integer

# If we want to print it along with text, we need to convert it to string (again using typecasting)
print("You are " + str(age) + " years old")
