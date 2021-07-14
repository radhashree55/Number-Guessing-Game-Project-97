import random

chances = 0
number = random.randint(1, 9)

print("Number Guessing Game")
print("Guess a number (between 1-9), and see if it matches the Computer's number")

while chances < 5:

    guess = int(input("Enter your number: "))

    if guess == number:
        print("Wow! You guessed it right!")
        break

    if guess > number:
        print("Oops! Too HIGH...")
    if guess < number:
        print("Uh Oh! Too LOW...")
    chances = chances + 1

if not chances < 5:
    print("You LOSE! The number is,", number)
