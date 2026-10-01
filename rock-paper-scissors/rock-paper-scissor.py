# ========================
# Rock Paper Scissors Game
# ========================

import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {ROCK: "👊", PAPER: "📄", SCISSORS: "✂"}

choices = tuple(emojis.keys())


def get_user_input():
    while True:
        user_choice = input("Rock, paper, or scissors? (r / p / s): ").lower().strip()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def display_choices(user_choice, computer_choice):

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    user_winning_criteria = (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)
    )

    if user_choice == computer_choice:
        return "Tie"
    elif user_winning_criteria:
        return "You win! 🎉"
    else:
        return "You lose! 😭"


def get_continue_input():
    while True:
        answer = input("Continue? (y/n): ").lower().strip()

        if answer in ("y", "n"):
            return answer

        print("Invalid input! Please enter 'y' or 'n'.")


def play_game():
    wins = 0
    losses = 0
    ties = 0

    while True:
        user_choice = get_user_input()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win! 🎉":
            wins += 1
        elif result == "You lose! 😭":
            losses += 1
        else:
            ties += 1

        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Ties: {ties}")

        if get_continue_input() == "n":
            break


def main():
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
