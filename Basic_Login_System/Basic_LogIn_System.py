import sys

# Initially, create two lists containing the usernames and passwords of users
userName = ["user1","user2"]
passWord = ["pass1","pass2"]

# Total attempts allowed for the user to Log In (You can change it according to your needs)
tries = 3


# Algorithm for the LogIn system

# First, create a loop that will terminate when the number of tries reaches 0
while tries > 0:

    # Commands to get the username and password from the user (from the terminal)
    name = input("Enter your username: ")
    pw = input("Enter your password: ")


    # Check if the username entered by the user is correct
    if name == userName[0]:

        # If the username is correct, check the password entered
        if pw == passWord[0]:
            print("Welcome user1")

            # If both username and password are correct, break the loop
            break

        # If the password is wrong but the username is correct, execute the following else block
        else:
            print("Wrong password")

            tries -= 1

            print("You have ", tries, " tries left")


    # In case there are multiple entries in the lists, we can repeat the check for username and password
    # (as shown below)


    # Check if the username entered by the user is correct
    elif name == userName[1]:

        # If the username is correct, check the password entered
        if pw == passWord[1]:
            print("Welcome user2")

            # If both username and password are correct, break the loop
            break

        # If the password is wrong but the username is correct, execute the following else block
        else:
            print("Wrong password")

            tries -= 1

            print("You have ", tries, " tries left")


    # If the username is wrong, execute the following else block directly
    else:
        print("Wrong username")
        tries -= 1

        print("You have ", tries, " tries left")


# After the loop, check if tries reached 0
# If so, the program will terminate indicating no more tries left
if tries == 0:
    print("You have no more tries left")

    # Command to exit the program
    sys.exit()


# If tries are still more than 0, the program continues and shows the following message
print("You have successfully logged in")
