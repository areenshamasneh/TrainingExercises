import random


class Number:
    MIN_VALUE = 1
    MAX_VALUE = 100
    PROXIMITY_THRESHOLD = 5

    def __init__(self):
        # Randomly generate a number to guess within the defined range
        self.value = random.randint(self.MIN_VALUE, self.MAX_VALUE)


class Checker:
    def __init__(self, number):
        self.number = number

    def is_close(self, guess):
        # Check if the guessed number is within the proximity threshold
        return abs(guess - self.number.value) <= Number.PROXIMITY_THRESHOLD

    def is_guessed(self, guess):
        # Check if the guessed number is correct
        return guess == self.number.value

    def higher_or_lower(self, guess):
        # Determine if the guess is higher or lower than the target number
        return "higher" if guess < self.number.value else "lower"


class Validation:
    def validate_guess_type(self, guess):
        # Validate that the input can be converted to an integer
        try:
            int(guess)
            return True
        except ValueError:
            return False

    def validate_guess_bounds(self, guess):
        # Validate that the guess is within the allowed range
        guess = int(guess)
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

    def get_guess(self):
        # Prompt the user for their guess
        return input(self.MESSAGES["welcome"]())

    @staticmethod
    def print_message(message):
        print(message)


class Game:
    def __init__(self):
        self.number = Number()
        self.checker = Checker(self.number)
        self.validation = Validation()
        self.io = IO()
        self.is_running = True

    def provide_feedback(self, guess):
        guess = int(guess)  # Convert the guess to an integer
        if self.checker.is_guessed(guess):
            self.is_running = False  # End the game if the guess is correct
            return self.io.MESSAGES["congratulations"](self.number.value)

        if self.checker.is_close(guess):
            return (
                self.io.MESSAGES["very_close_higher"]
                if guess < self.number.value
                else self.io.MESSAGES["very_close_lower"]
            )

        return self.io.MESSAGES[self.checker.higher_or_lower(guess)]

    def play(self):
        while self.is_running:
            guess = self.io.get_guess()  # Get the user's guess
            if not self.validation.validate_guess_type(guess):
                self.io.print_message(self.io.MESSAGES["invalid_input"])
                continue
            guess = int(guess)  # Convert guess to integer
            if not self.validation.validate_guess_bounds(guess):
                self.io.print_message(self.io.MESSAGES["out_of_bounds"]())
                continue
            feedback = self.provide_feedback(guess)  # Get feedback for the guess
            self.io.print_message(feedback)


def main():
    # Allow the user to play multiple times
    while True:
        game = Game()
        game.play()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    main()
