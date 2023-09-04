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
    user_choice = get_choice()
    print(
        "\nYou chose:",
        user_choice,
    )
    comp_choice()


def get_choice():
    """TBD"""
    # code starts here
    valid_choices = ["rock", "paper", "scissors"]
    play_choice = input("What is your choice? Rock, paper, or scissors?\t").lower()
    while True:
        if play_choice in valid_choices:
            return play_choice.capitalize()
        else:
            print("That is not a valid choice. Please choose rock, paper, or scissors.")


def comp_choice():
    comp_choice_num = random.randint(1, 3)
    if comp_choice_num == 1:
        comp_choice = "Rock"
    elif comp_choice_num == 2:
        comp_choice = "Paper"
    elif comp_choice_num == 3:
        comp_choice = "Scissors"
    print("the computer chose: ", comp_choice, "\n")

def final_result():
    

if __name__ == "__main__":
    main()
