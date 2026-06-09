favorite_letter= input("What is your favorite letter? ").lower()
word = "Commitment"
for i in range(len(word)):
    letter = word[i]
    if letter == favorite_letter:
        print("_", end="")
    else:
        print(letter.lower(), end="")