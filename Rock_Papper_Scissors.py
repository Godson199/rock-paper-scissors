'''
Rock-Papper-Scissors is a simple two player game where, at a signal, players make figures with their hands
representing a rock, a piece of paper, or a pair of scissors.
The winner is determined according to the a set of rules.
......................................
Rules:
Rock smashes Scissors
Paper covers Rock
Scissors cut Paper

'''

import random

while True:
    user_action = input("Enter a choice (rock, papper, scissors): ").lower()

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players chose {user_action}. it's a tie! ")
    if user_action == "rock":
        if computer_action == "scissiors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers Rock! You lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Papper covers Rock! You win")
        else:
            print("scissors cuts paper! You lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper! You win")
        else:
            print("Rock smashes scissors! You lose")

    play_gain = input("Play Again? (yes/no): ").lower()
    if play_gain != "yes":
        print("Thanks for playing")
        break

