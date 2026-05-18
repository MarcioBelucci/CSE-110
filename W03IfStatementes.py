#First Exercise: Comparing numbers
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))
if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

animal = input("\nWhat is your favorite animal? ").lower()

if animal == "cat":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite")

#Second Exercise: Qualifying for a loan
print("Rate from 1-10 the following questions:")
loan_value = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment = int(input("How large is your down payment? "))
loan_decision = True

if loan_value >= 5:
    if credit_history >= 7 and income >= 7:
        loan_decision = True
    elif credit_history >= 7 or income >= 7:
        if payment >= 5:
            loan_decision = True
        else:
            loan_decision = False
    else:
        loan_decision = False

else:
    if credit_history < 4:
        loan_decision = False
    else:
        if income >= 7 or payment >= 7:
            loan_decision = True
        elif income >= 4 and payment >= 4:
            loan_decision = True
        else: 
            loan_decision = False

if loan_decision:
    print("The decision is yes.")
else:
    print("The decision is no.")