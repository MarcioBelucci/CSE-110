import random
play = "yes"
while play == "yes":
    number = random.randint(1, 100)
    guess = 0
    count = 0
    while guess != number:
        guess = int(input("What is your guess? "))
        count += 1
        if guess < number:
            print("Lower")
        elif guess > number:
            print("Higher")
        else:
            print("You guessed it!")
    print(f"It took you {count} guesses")
    play = input("Would you like to play again (yes/no)? ")
print("Thank you for playing. Goodbye.")