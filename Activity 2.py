import random

while True:
    user_action = input("Enter a choice(rock, paper or scissors) ")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action} and the computer chose {computer_action}")
    if user_action == computer_action:
        print(f"Both sides selected {computer_action}")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock destroys scissors. You win😊.")
        else:
            print("Paper covers rock. You lose😒.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win! Scissors cuts paper😊.")
        else:
            print("You lose! Rock destroys paper😒.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win😊.")
        else:
            print("Scissors cuts paper! You lose😒.")
    else:
        print("Invalid input")
    play_again = input("Play again? (y/n) ")
    if play_again != "y":
        break
