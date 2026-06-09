people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest = 99
youngest_name = ""
for line in people:
    parts = line.split()

    name = parts[0]
    age = int(parts[1])

    print(f"The name is {name} and the age is {age}")
    if age < youngest:
        youngest = age
        youngest_name = name
print(f"The person who is youngest is: {youngest_name}. {youngest} years old.")
