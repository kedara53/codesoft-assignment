import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '4':
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        choices_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice = choices_map[choice]
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        display_result(user_choice, computer_choice, winner)
        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == '__main__':
    main()
