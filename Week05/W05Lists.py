names_list = []
friends = ""

while friends != "end":
    friends = input("Type a name of a friend: ").lower()
    if friends != "end":
        names_list.append(friends)

print("\nYour friends are:")
for name in names_list:
    print(f"{name.capitalize()}")