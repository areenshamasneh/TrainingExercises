import random


class Number:
    # Define constants for the game
    MIN_VALUE = 1
    MAX_VALUE = 100
    PROXIMITY_THRESHOLD = 5

    def __init__(self):
        # Randomly generate a number to guess within the defined range
        self.value = random.randint(self.MIN_VALUE, self.MAX_VALUE)

    def is_close(self, guess):
        # Check if the guessed number is within the proximity threshold
        return abs(guess - self.value) <= self.PROXIMITY_THRESHOLD


class Game:
    MESSAGES = {
        "welcome": lambda min_val, max_val: f"Guess a number between {min_val} and {max_val}: ",
        "out_of_bounds": lambda min_val, max_val: f"Please enter a number between {min_val} and {max_val}.",
        "invalid_input": "Invalid input! Please enter a valid number.",
        "congratulations": lambda num: f"Congratulations! You've guessed the number {num}.",
        "very_close_higher": "Very close! But a bit higher.",
        "very_close_lower": "Very close! But a bit lower.",
        "higher": "Higher!",
        "lower": "Lower!",
    }

    def __init__(self):
        # Create a new Number instance for the game
        self.number = Number()

    def get_guess(self):
        while True:
            try:
                guess = int(
                    input(self.MESSAGES["welcome"](Number.MIN_VALUE, Number.MAX_VALUE))
                )
                # Check if the guess is within the valid range
                if guess < Number.MIN_VALUE or guess > Number.MAX_VALUE:
                    print(
                        self.MESSAGES["out_of_bounds"](
                            Number.MIN_VALUE, Number.MAX_VALUE
                        )
                    )
                    continue
                return guess
            except ValueError:
                print(self.MESSAGES["invalid_input"])

    def provide_feedback(self, guess):
        # Provide feedback based on the user's guess
        if guess == self.number.value:
            return self.MESSAGES["congratulations"](self.number.value)

        if self.number.is_close(guess):
            return (
                self.MESSAGES["very_close_higher"]
                if guess < self.number.value
                else self.MESSAGES["very_close_lower"]
            )

        return (
            self.MESSAGES["higher"]
            if guess < self.number.value
            else self.MESSAGES["lower"]
        )

    def play(self):
        while True:
            guess = self.get_guess()
            feedback = self.provide_feedback(guess)
            print(feedback)
            if guess == self.number.value:
                break


def main():
    # Loop to allow the user to play multiple times
    while True:
        game = Game()
        game.play()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    main()
