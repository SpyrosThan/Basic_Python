# Rock Paper Scissors game

# Import the random library for the computer's random choice
import random


print("Welcome to a Rock Paper Scissors game")
enter = input("\nPress any key to continue")


while True:
    print("Let's start the game!\n")
 
    print("------------------------------------------------------------")
    print("Choose one of the three: \n1.Rock \n2.Scissors \n3.Paper")
    print("------------------------------------------------------------")
    player_choice = int(input("Your choice: "))
    print("\n")

    # Computer's choice (random number from 1 to 3)
    game_choice = random.randint(1,3)

    # Case where user has entered the code to win
    if (player_choice == 3 or player_choice == 2 or player_choice == 1) and enter == "123":
        print("------------------------------------------------------------")
        print("You won!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case where user chooses rock and computer scissors
    elif player_choice == 1 and game_choice == 2:
        print("------------------------------------------------------------")
        print("You won!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case where user chooses rock and computer paper
    elif player_choice == 1 and game_choice == 3:
        print("------------------------------------------------------------")
        print("You lost!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case where user chooses scissors and computer rock
    elif player_choice == 2 and game_choice == 1:
        print("------------------------------------------------------------")
        print("You lost!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case where user chooses scissors and computer paper
    elif player_choice == 2 and game_choice == 3:
        print("------------------------------------------------------------")
        print("You won!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case where user chooses paper and computer rock
    elif player_choice == 3 and game_choice == 1:
        print("------------------------------------------------------------")
        print("You won!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case where user chooses paper and computer scissors
    elif player_choice == 3 and game_choice == 2:
        print("------------------------------------------------------------")
        print("You lost!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case of a tie
    elif player_choice == game_choice:
        print("------------------------------------------------------------")
        print("Tie!!!")
        print("------------------------------------------------------------\n\n\n")
        continue
    # Case of wrong choice
    else:
        print("------------------------------------------------------------")
        print("Wrong choice")
        print("------------------------------------------------------------\n\n\n")
        continue
