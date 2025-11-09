# create a simple rock, paper, scissors game
# start with a welcome message
# provide simple instructions
# get user input
# generate computer choice
# determine the winner
# display the result
# ask user if they want to play again
# repeat play if they do, otherwise exit with a goodbye message
# only use one function

import random

def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = get_result(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break   

if __name__ == "__main__":
    rock_paper_scissors()