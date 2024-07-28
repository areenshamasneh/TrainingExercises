import random

# Define constants for the game
MIN_NUMBER = 1
MAX_NUMBER = 100
PROXIMITY_THRESHOLD = 5

MESSAGES = {
    "welcome": lambda: f"Guess a number between {MIN_NUMBER} & {MAX_NUMBER}: ",
    "invalid_input": "Invalid input! Please enter a valid number.",
    "out_of_bounds": f"Please enter a number between {MIN_NUMBER} & {MAX_NUMBER}.",
    "congratulations": lambda number: f"Congratulations! You've guessed the number {number}.",
    "feedback": {
        "very_close_higher": "Very close! But a bit higher.",
        "very_close_lower": "Very close! But a bit lower.",
        "higher": "Higher!",
        "lower": "Lower!",
    },
}


def get_input(prompt):
    return input(prompt)


def validate_guess(guess):
    """Validate if the guess is within the allowed range."""
    if not guess.isdigit():
        print(MESSAGES["invalid_input"])
        return None
    guess = int(guess)
    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        print(MESSAGES["out_of_bounds"])
        return None
    return guess


def provide_feedback(guess, number_to_guess):
    if guess == number_to_guess:
        return MESSAGES["congratulations"](number_to_guess)
    return check_proximity(guess, number_to_guess)


def check_proximity(guess, number_to_guess):
    """Check proximity and provide appropriate feedback."""
    difference = guess - number_to_guess
    if abs(difference) <= PROXIMITY_THRESHOLD:
        return MESSAGES["feedback"][
            "very_close_higher" if difference < 0 else "very_close_lower"
        ]
    return check_direction(guess, number_to_guess)


def check_direction(guess, number_to_guess):
    """Check if the guess is higher or lower than the target number."""
    return MESSAGES["feedback"]["higher" if guess < number_to_guess else "lower"]


def play_game():
    number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)

    while True:
        guess = None
        while guess is None:
            guess = validate_guess(get_input(MESSAGES["welcome"]()))
        feedback = provide_feedback(guess, number_to_guess)
        print(feedback)
        if guess == number_to_guess:
            break


def main():
    while True:
        play_game()
        if input("Do you want to play again? (yes/no): ").strip().lower() != "yes":
            break


if __name__ == "__main__":
    main()
