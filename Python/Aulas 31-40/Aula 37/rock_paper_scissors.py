import random

def game():
    choices = ["Rock","Paper","Scissors"]
    computer = random.choice(choices)
    player = None
    end_condition = None

    while player not in choices:
        player = str(input("Rock, paper or scissors?: ")).capitalize()
        if player not in choices:
            print("Type Rock paper or scissors only:\n")

    if player == computer:
        end_condition = 0

    elif player == "Rock":
        if computer == "Paper":
            end_condition = 1
        elif computer == "Scissors":
            end_condition = 2

    elif player == "Paper":
        if computer == "Rock":
            end_condition = 2
        elif computer == "Scissors":
            end_condition = 1

    elif player == "Scissors":
        if computer == "Rock":
            end_condition = 1
        elif computer == "Paper":
            end_condition = 2
    
    print("\n\nPlayer: ", player)
    print("Computer:", computer)

    if end_condition == 0:
        print("\nTie game!\n")
    elif end_condition == 1:
        print("\nYou lost! :(\n")
    elif end_condition == 2:
        print("\nYou win!!! :D\n")

    play_again = str(input("Do you want to play again? Yes/No: ")).lower()
    if play_again == "yes":
        game()
    else:
        print("\nThank you for playing!")

game()
