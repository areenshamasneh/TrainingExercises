import random

MIN_NUMBER = 1
MAX_NUMBER = 100
PROXIMITY_THRESHOLD = 5


def guess_number():
    while True:
        number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)
        while True:
            try:
                guess = int(
                    input(f"Guess a number between {MIN_NUMBER} & {MAX_NUMBER}: ")
                )
                if guess < MIN_NUMBER or guess > MAX_NUMBER:
                    print(
                        f"Please enter a number between {MIN_NUMBER} & {MAX_NUMBER}."
                    )
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess}.")
                break

            if abs(guess - number_to_guess) <= PROXIMITY_THRESHOLD:
                if guess < number_to_guess:
                    print("Very close! But a bit higher.")
                else:
                    print("Very close! But a bit lower.")
            elif guess < number_to_guess:
                print("Higher!")
            else:
                print("Lower!")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    guess_number()
