import random


class Number:
    MIN_VALUE = 1
    MAX_VALUE = 100
    PROXIMITY_THRESHOLD = 5

    def __init__(self):
        # Randomly generate a number to guess within the defined range
        self.value = random.randint(self.MIN_VALUE, self.MAX_VALUE)

    def is_close(self, guess):
        # Check if the guessed number is within the proximity threshold
        return abs(guess - self.value) <= self.PROXIMITY_THRESHOLD


class Checker:
    @staticmethod
    def is_valid(guess):
        return Number.MIN_VALUE <= guess <= Number.MAX_VALUE


class IO:
    MESSAGES = {
        "welcome": lambda: f"Guess a number between {Number.MIN_VALUE} and {Number.MAX_VALUE}: ",
        "invalid_input": "Invalid input! Please enter a valid number.",
        "out_of_bounds": lambda: f"Please enter a number between {Number.MIN_VALUE} and {Number.MAX_VALUE}.",
        "congratulations": lambda num: f"Congratulations! You've guessed the number {num}.",
        "very_close_higher": "Very close! But a bit higher.",
        "very_close_lower": "Very close! But a bit lower.",
        "higher": "Higher!",
        "lower": "Lower!",
    }

    @staticmethod
    def get_guess():
        while True:
            try:
                guess = int(input(IO.MESSAGES["welcome"]()))
                return guess
            except ValueError:
                print(IO.MESSAGES["invalid_input"])

    @staticmethod
    def print_message(message):
        print(message)


class Validation:
    @staticmethod
    def validate_guess(guess):
        if not Checker.is_valid(guess):
            IO.print_message(IO.MESSAGES["out_of_bounds"]())
            return False
        return True


class Game:
    def __init__(self):
        # Create a new Number instance for the game
        self.number = Number()
        self.is_running = True  # Track the game's running status

    def provide_feedback(self, guess):
        # Provide feedback based on the user's guess
        if guess == self.number.value:
            self.is_running = False
            return IO.MESSAGES["congratulations"](self.number.value)

        if self.number.is_close(guess):
            return (
                IO.MESSAGES["very_close_higher"]
                if guess < self.number.value
                else IO.MESSAGES["very_close_lower"]
            )

        return (
            IO.MESSAGES["higher"] if guess < self.number.value else IO.MESSAGES["lower"]
        )

    def play(self):
        while self.is_running:
            guess = IO.get_guess()
            if Validation.validate_guess(guess):
                feedback = self.provide_feedback(guess)
                IO.print_message(feedback)


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
