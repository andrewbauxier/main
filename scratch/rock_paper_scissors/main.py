"""
Project Name:   rock_paper_scissors
Module Name:    main
Author:         Andrew Auxier
Company:        N/A
Description:    

    Start here
"""
# imports go here
import random


def main():
    """Begin app, sets toggle bool to loop on tie, grabs choices then decides outcome"""
    game_continues = True
    while game_continues:
        play_choice = get_player_choice()
        computer_choice = get_computer_choice()
        game_continues = final_result(play_choice, computer_choice)


def get_player_choice():
    """receive input for player choice"""
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        play_choice = input("What is your choice? Rock, paper, or scissors?\t").lower()
        if play_choice in valid_choices:
            print("\nYou chose:", play_choice.capitalize())
            return play_choice.capitalize()
        else:
            print("That is not a valid choice. Please choose again.")


def get_computer_choice():
    """Randomly generate choice for computer"""
    comp_choice_num = random.randint(1, 3)
    if comp_choice_num == 1:
        comp_choice = "Rock"
    elif comp_choice_num == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print("The computer chose:", comp_choice, "\n")
    return comp_choice


def final_result(play_choice, comp_choice):
    if play_choice == comp_choice:
        print("It's a Tie!")
    elif play_choice == "rock":
        if comp_choice == "scissors":
            print("Rock beats scissors, you win!")
            return False


if __name__ == "__main__":
    main()
