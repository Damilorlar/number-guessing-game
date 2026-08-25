from utils import get_valid_guess, get_difficulty,greet

import random
print(greet())

difficulty = get_difficulty()

minimum = difficulty["min"]
maximum = difficulty["max"]
attempts = difficulty["attempts"]



print(f"Guess a number between {minimum} and {maximum}")
print(f"You have {attempts} attempts.")

number = random.randint(minimum, maximum)
while attempts > 0:
    guess=get_valid_guess()
    attempts -= 1
    if (guess < number):
                print("Guess Higher")
    elif (guess > number):
                print("Guess Lower")
    elif guess == number:
        print("You guess correctly.")
        break
    else:
        print("You have reach your limit")

