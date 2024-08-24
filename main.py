import random
import time


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have to guess the correct number within the given chances.")


def number_guessing_game():

    difficulty_levels = {
        1: {"name": "Easy", "chances": 10},
        2: {"name": "Medium", "chances": 5},
        3: {"name": "Hard", "chances": 3},
    }

    print("Please select the difficulty level:")
    for key, value in difficulty_levels.items():
        print(f"{key}. {value['name']} ({value['chances']} chances)")

    difficulty_choice = int(input("Enter your choice: "))
    difficulty_level = difficulty_levels[difficulty_choice]

    print(f"Great! You have selected the {difficulty_level['name']} difficulty level.")
    print("Let's start the game!")

    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while attempts < difficulty_level["chances"]:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            end_time = time.time()
            print(
                f"Congratulations! You guessed the correct number in {attempts} attempts."
            )
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            break
        elif user_guess < secret_number:
            print("Incorrect! The number is greater than your guess.")
        else:
            print("Incorrect! The number is less than your guess.")

    if attempts == difficulty_level["chances"]:
        print(f"Sorry, you ran out of chances! The correct number was {secret_number}.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()


if __name__ == "__main__":
    number_guessing_game()
