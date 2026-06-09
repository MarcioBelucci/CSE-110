grade = int(input("What is the grade? "))
letter_grade = ""

if grade >= 70:
    print("Congratulations you passed in the course!")
    if grade >= 90:
        if grade >= 93:
            letter_grade = "A"
        else:
            letter_grade = "A-"
    elif grade >= 80:
        letter_grade = "B"
        if grade < 83:
            letter_grade += "-"
        elif grade > 86:
            letter_grade += "+"
    else:
        letter_grade = "C"
   
else:
    print("Sorry you don't passed in the course!")
    if grade >= 60:
        letter_grade = "D"
        if grade < 63:
            letter_grade += "-"
        elif grade > 66:
            letter_grade += "+"
    else:
        letter_grade = "F"

print(f"Your grade is {letter_grade}")