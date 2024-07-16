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


def get_guess():
    while True:
        try:
            # Request user input and convert it to an integer
            guess = int(input(MESSAGES["welcome"]()))
            # Check if the guess is within the valid range
            if guess < MIN_NUMBER or guess > MAX_NUMBER:
                print(MESSAGES["out_of_bounds"])
                continue
            return guess
        except ValueError:
            print(MESSAGES["invalid_input"])


def provide_feedback(guess, number_to_guess):
    # Provide feedback based on the user's guess
    if guess == number_to_guess:
        return MESSAGES["congratulations"](number_to_guess)

    difference = guess - number_to_guess  # Calculate the difference

    # Provide proximity feedback if the guess is close
    if abs(difference) <= PROXIMITY_THRESHOLD:
        return MESSAGES["feedback"][
            "very_close_higher" if difference < 0 else "very_close_lower"
        ]

    # Provide higher/lower feedback based on the guess
    return MESSAGES["feedback"]["higher" if difference < 0 else "lower"]


def play_game():
    # Randomly generate the number to guess
    number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)

    while True:
        guess = get_guess()  # Get a guess from the user
        feedback = provide_feedback(guess, number_to_guess)
        print(feedback)

        # Check if the guess is correct to end the game
        if guess == number_to_guess:
            break


def main():
    # Loop to allow the user to play multiple times
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    main()
