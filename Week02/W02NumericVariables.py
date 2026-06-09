age = int(input("How old are you? "))
print(f"On your next birthday, you will be {age + 1}")

eggs = int(input("\nHow many egg cartons do you have? "))
print(f"You have {eggs * 12} eggs")

cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_per_person = cookies / people
print(f"Each person may have {float(cookies_per_person)} cookies")