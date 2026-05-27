secreat = "mosiah"
letter_secreat = list(secreat)
print("Welcome to the word guessing game!")
guess = ""
hint = "_" * len(secreat)
count = 0
while guess != secreat:
    count += 1
    print(f"\nYour hint is: {hint}")
    guess = input("What is your guess? ").lower()

    for i in range(len(guess)):
        letter = guess[i]
        letter_secreat = secreat[i]
        if letter == letter_secreat:
            print(letter.upper(), end="")
        #elif letter != letter_secreat:
        #    print(letter.lower(), end="")
        else:
            print("_", end="")            
    
print("\nCongratulations! You guessed it!")
print(f"It took you {count} guesses.")

#for i in range(len(word)):
#    letter = word[i]
#    if letter == favorite_letter:
#        print("_", end="")
#    else:
#        print(letter.lower(), end="")


# for s in range(len(secreat)):
        #letter_secreat = secreat[s]