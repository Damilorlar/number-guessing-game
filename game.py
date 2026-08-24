import random

number= random.randint(1,100)
guess = 0
limit = 0

while guess != number:
    guess = int(input("Enter Your guess:"))
    if (guess < number):
            print("Guess Higher")
    elif (guess > number):
            print("Guess Lower")
    else :
            print("You guess correctly.")
    limit +=1
    if limit == 3:
        print("You have reach your limit")
        break
  