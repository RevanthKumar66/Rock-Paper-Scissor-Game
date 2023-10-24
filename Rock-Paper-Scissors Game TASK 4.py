import random

def get_user_input():
    print("Enter your choice: (rock/paper/scissors)")
    user_choice = input().lower()
    return user_choice

def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print("You chose:", user_choice)
    print("The computer chose:", computer_choice)
    print(result)

def play_again():
    print("Do you want to play again? (yes/no)")
    return input().lower() == 'yes'

def main():
    while True:
        user_choice = get_user_input()
        computer_choice = generate_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        if not play_again():
            break

if __name__ == "__main__":
    main()