# Attention: any line starting with # is a comment and is not executed by the program

# Examples with the for statement

# Example 1
# Display the numbers from 0 to 5
for i in range(6):
    print(i)

# Attention, the statement range(1,6) does not include 6
# If we want 6 to be displayed, we must write range(1,7)

# Example 2
# Display the numbers from 1 to 5
for i in range(1,6):
    print(i)

# In range we provide two numbers, the first and the last one, to define the start and end

# Example 3
# Display the numbers from 1 to 5, adding 2 each time
for i in range(1,6,2):
    print(i)

# In range we provide three numbers: the first, the last, and the step, to define the start, end, and the increment at each repetition

# Example 4
for i in range(1,6):
    print(i+1)

# The above loop gives the variable i the values 1,2,3,4,5 and displays i+1, i.e. the values 2,3,4,5,6
