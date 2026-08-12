import random
import tkinter as tk

from rock_paper_scissors import INPUT_ALIASES, VALID_CHOICES, determine_winner


class RockPaperScissorsGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0

        tk.Label(
            root,
            text="Enter rock/paper/scissors (or r/p/s). Type quit to close.",
        ).pack(padx=10, pady=(10, 5))

        self.input_entry = tk.Entry(root, width=30)
        self.input_entry.pack(padx=10, pady=5)
        self.input_entry.bind("<Return>", self.play_round)

        tk.Button(root, text="Play Round", command=self.play_round).pack(pady=5)
        tk.Button(root, text="Quit", command=root.destroy).pack(pady=(0, 10))

        self.result_label = tk.Label(root, text="Make your move!")
        self.result_label.pack(padx=10, pady=5)

        self.score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0")
        self.score_label.pack(padx=10, pady=(0, 10))

    def play_round(self, _event=None) -> None:
        player_input = self.input_entry.get().strip().lower()

        if player_input == "quit":
            self.root.destroy()
            return

        player_choice = INPUT_ALIASES.get(player_input, player_input)
        if player_choice not in VALID_CHOICES:
            self.result_label.config(
                text="Invalid choice. Use rock/paper/scissors, r/p/s, or quit."
            )
            return

        computer_choice = random.choice(tuple(VALID_CHOICES))
        winner = determine_winner(player_choice, computer_choice)

        if winner == "tie":
            result = f"Computer chose {computer_choice}. It's a tie!"
        elif winner == "player":
            self.player_score += 1
            result = f"Computer chose {computer_choice}. You won this round!"
        else:
            self.computer_score += 1
            result = f"Computer chose {computer_choice}. Computer won this round!"

        self.result_label.config(text=result)
        self.score_label.config(
            text=f"Score -> You: {self.player_score} | Computer: {self.computer_score}"
        )
        self.input_entry.delete(0, tk.END)


def main() -> None:
    root = tk.Tk()
    RockPaperScissorsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
