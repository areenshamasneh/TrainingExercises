import random


class NumberGenerator:
    MIN_VALUE = 1
    MAX_VALUE = 100
    PROXIMITY_THRESHOLD = 5

    @staticmethod
    def generate():
        # Randomly generate a number to guess within the defined range
        return random.randint(NumberGenerator.MIN_VALUE, NumberGenerator.MAX_VALUE)


class Checker:
    def __init__(self, number):
        self.number = number

    def is_close(self, guess):
        # Check if the guessed number is within the proximity threshold
        return abs(guess - self.number) <= NumberGenerator.PROXIMITY_THRESHOLD

    def is_guessed(self, guess):
        # Check if the guessed number is correct
        return guess == self.number

    def higher_or_lower(self, guess):
        # Determine if the guess is higher or lower than the target number
        return "higher" if guess < self.number else "lower"


class Validation:
    @staticmethod
    def validate_guess_type(guess):
        # Validate that the input can be converted to an integer
        try:
            int(guess)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_guess_bounds(guess):
        # Validate that the guess is within the allowed range
        return NumberGenerator.MIN_VALUE <= guess <= NumberGenerator.MAX_VALUE


class IO:
    MESSAGES = {
        "welcome": lambda: f"Guess a number between {NumberGenerator.MIN_VALUE} and {NumberGenerator.MAX_VALUE} (or 'q' to quit): ",
        "invalid_input": "Invalid input! Please enter a valid number.",
        "out_of_bounds": lambda: f"Please enter a number between {NumberGenerator.MIN_VALUE} and {NumberGenerator.MAX_VALUE}.",
        "congratulations": lambda num: f"Congratulations! You've guessed the number {num}.",
        "very_close_higher": "Very close! But a bit higher.",
        "very_close_lower": "Very close! But a bit lower.",
        "higher": "Higher!",
        "lower": "Lower!",
    }

    @staticmethod
    def get_guess():
        return input(IO.MESSAGES["welcome"]())

    @staticmethod
    def print_message(message):
        print(message)


class GamePlay:
    def __init__(self):
        self.number = NumberGenerator.generate()
        self.checker = Checker(self.number)
        self.validation = Validation()
        self.io = IO()
        self.is_running = True
        self.user_quit = False

    def provide_feedback(self, guess):
        if self.checker.is_guessed(guess):
            self.is_running = False
            return self.io.MESSAGES["congratulations"](self.number)

        if self.checker.is_close(guess):
            return (
                self.io.MESSAGES["very_close_higher"]
                if guess < self.number
                else self.io.MESSAGES["very_close_lower"]
            )

        return self.io.MESSAGES[self.checker.higher_or_lower(guess)]

    def play(self):
        while self.is_running:
            guess_input = self.io.get_guess()
            if guess_input.strip().lower() == "q":
                self.is_running = False
                self.user_quit = True
                break
            if not self.validation.validate_guess_type(guess_input):
                self.io.print_message(self.io.MESSAGES["invalid_input"])
                continue
            guess = int(guess_input)
            if not self.validation.validate_guess_bounds(guess):
                self.io.print_message(self.io.MESSAGES["out_of_bounds"]())
                continue
            feedback = self.provide_feedback(guess)
            self.io.print_message(feedback)


class Game:
    def __init__(self):
        self.attempts = 0
        self.wins = 0

    def start(self):
        while True:
            gameplay = GamePlay()
            gameplay.play()
            self.attempts += 1
            if not gameplay.user_quit:
                self.wins += 1
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                break

    def show_stats(self):
        print(f"Total attempts: {self.attempts}")
        print(f"Total wins: {self.wins}")


def main():
    game = Game()
    game.start()
    game.show_stats()


if __name__ == "__main__":
    main()
