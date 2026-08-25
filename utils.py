#
def greet():
    return """
    =================================================
             Welcome to Number Guessing Game 
    =================================================
    """
   

def get_valid_guess():
    while True:
        try:
            text = int(input("Enter your guess: "))
            return text
        except ValueError:
            print("That's not a valid number. Try again.")


DIFFICULTIES = {
    "easy": {"min": 1, "max": 100, "attempts": 10},
    "medium": {"min": 1, "max": 150, "attempts": 7},
    "hard": {"min": 1, "max": 200, "attempts": 5}
}

def get_difficulty():
    print("Select difficulty: [1] Easy  [2] Medium  [3] Hard")
    while True:
        player_choice = input("> ")

        if player_choice == "1":
            return DIFFICULTIES["easy"]
        elif player_choice == "2":
            return DIFFICULTIES["medium"]
        elif player_choice == "3":
            return DIFFICULTIES["hard"]
        else:
            print("Pick a difficulty")

