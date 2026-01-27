import random

a = random.randint(1, 100)

while True:
    guess = input("Enter your guess (1-100) or Quit (Q):\n")

    if guess.upper() == "Q":
        print("Game Over")
        break
    if not guess.isdigit():
        print("Please enter a valid number.\n")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print("Enter between 1 and 100 only.\n")
    elif guess < a:
        print("Think higher.\n")
    elif guess > a:
        print("Think lower.\n")
    else:
        print("Correct! You guessed the number.")
        break
