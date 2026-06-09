print("Please enter the items of the shopping list (type: QUIT to finish):")
shooping_list = []
item = ""
while item != "quit":
    item = input("Item: ").lower()
    if item != "quit":
        shooping_list.append(item)
        
print("\nThe shopping list is:")
for item in shooping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shooping_list)):
    item = shooping_list[i]
    print(f"{i}. {item}")

index_question = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

print("\nThe shopping list with indexes is:")

shooping_list[index_question] = new_item

for i in range(len(shooping_list)):
    item = shooping_list[i]
    print(f"{i}. {item}")