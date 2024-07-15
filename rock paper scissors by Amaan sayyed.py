import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (ROCK =r, PAPER =p, SCISSORS =s): ").strip().lower()
        if player_choice in ['r', 'p','s']:
            return player_choice
        else:
         print("Invalid input! Please enter either 'rock', 'paper', or 'scissors'.")

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        print("\nLet's play Rock, Paper, Scissors!")

        player_choice = get_player_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore - You: {player_score}  Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

# Start the game
play_game()