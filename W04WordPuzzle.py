# I added two new features. The first is to give the players the option to play again when they guess the secret word. If they choose "no," the game will display a message thanking them for playing.
# The second is a message to advise the player if they took 10 guesses.
play = "yes"
while play == "yes":
    secreat = "mosiah"
    letter_secreat = list(secreat)
    guess = ""
    hint = "_ " * len(secreat)
    count = 0 
    print("Welcome to the word guessing game!")
    print(f"\nYour hint is: {hint}")
    while guess != secreat:
        count += 1
        guess = input("What is your guess? ").lower()    
        if len(guess) == len(secreat):
            hint = ""
            for i in range(len(guess)):
                letter = guess[i]
                letter_secreat = secreat[i]
                if letter == letter_secreat:
                    hint += letter.upper() + " "
                elif letter in secreat:
                    hint += letter.lower() + " "
                else:
                    hint += "_ "
            print(f"Your hint is: {hint}") 
        else:        
            print("Sorry, the guess must have the same number of letters as the secret word.\n")   
        if count == 10 and guess != secreat:
            print("\nPlease, pay attention! You already took 10 guesses.\n")
    print("\nCongratulations! You guessed it!")
    print(f"It took you {count} guesses.")
    play = input("Would you like to play again (yes/no)? ").lower()
print("Thank you for playing. See you next time.")