import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nWelcome to Rock-Paper-Scissors Game!")
        print("Enter 'rock', 'paper', or 'scissors'. To quit, enter 'quit'.")

        user_choice = input("Your choice: ").lower()

        if user_choice == "quit":
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nCurrent Scores:")
        print(f"You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
