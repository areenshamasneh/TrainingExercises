import random

MIN_NUMBER = 1
MAX_NUMBER = 100
PROXIMITY_THRESHOLD = 5


class GuessNumber:
    def __init__(self):
        self.number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)

    def __str__(self):
        return f"Guess a number between {MIN_NUMBER} & {MAX_NUMBER}: "

    def __call__(self):
        while True:
            try:
                guess = int(input(str(self)))
                if guess < MIN_NUMBER or guess > MAX_NUMBER:
                    print(
                        f"Please enter a number between {MIN_NUMBER} & {MAX_NUMBER}."
                    )
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if guess == self.number_to_guess:
                print(
                    f"Congratulations! You've guessed the number {self.number_to_guess}."
                )
                break

            if abs(guess - self.number_to_guess) <= PROXIMITY_THRESHOLD:
                if guess < self.number_to_guess:
                    print("Very close! But a bit higher.")
                else:
                    print("Very close! But a bit lower.")
            elif guess < self.number_to_guess:
                print("Higher!")
            else:
                print("Lower!")


def main():
    while True:
        game = GuessNumber()
        game()

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    main()
