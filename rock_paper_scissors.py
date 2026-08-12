import random

VALID_CHOICES = {"rock", "paper", "scissors"}
INPUT_ALIASES = {"r": "rock", "p": "paper", "s": "scissors"}


def determine_winner(player_choice: str, computer_choice: str) -> str:
    if player_choice == computer_choice:
        return "tie"
    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"
    return "computer"


def main() -> None:
    player_score = 0
    computer_score = 0

    print("Welcome to Rock Paper Scissors!")
    print("Type rock/paper/scissors (or r/p/s) to play. Type quit to stop.")

    while True:
        player_input = input("Your choice: ").strip().lower()

        if player_input == "quit":
            print("Thanks for playing!")
            break

        player_choice = INPUT_ALIASES.get(player_input, player_input)

        if player_choice not in VALID_CHOICES:
            print("Invalid choice. Please type rock/paper/scissors, r/p/s, or quit.")
            continue

        computer_choice = random.choice(tuple(VALID_CHOICES))
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "tie":
            print("This round is a tie!")
        elif winner == "player":
            player_score += 1
            print("You won this round!")
        else:
            computer_score += 1
            print("Computer won this round!")

        print(f"Score -> You: {player_score} | Computer: {computer_score}")

    print(f"Final score -> You: {player_score} | Computer: {computer_score}")


if __name__ == "__main__":
    main()
