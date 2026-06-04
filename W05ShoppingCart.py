#I added some validation if the user wants to see or remove the items from their shopping charts without any items added before, they will receive a message that there isn't have any items. 
# Also, I put in options 2 and 3 the message showing how many items are in the shopping chart 
action = 0
items_list = []
prices_list =[]

print("Welcome to the Shopping Cart Program!")

while action != 5:
    print("\nPlease select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    action = int(input("Please enter an action: "))
    if action < 1 or action > 5:
        print("Sorry, that is not a valid item number.")
    else:
        human_count = 0
        remove = 0
        total = 0
        if action == 1:
            item_name = input("What item would you like to add? ").capitalize()
            if item_name != "":
                items_list.append(item_name)
                price = float(input(f"What is the price of '{item_name}'? $"))
                prices_list.append(price)
                print(f"'{item_name}' has been added to the cart.")
            else:
                print("Sorry, that is not valid item name.")
        
        elif action == 2:
            print("The contents of the shopping cart are:")
            for i in range(len(items_list)):
                item = items_list[i]
                price = prices_list[i]
                human_count = i + 1
                print(f"{human_count}. {item} - ${price:.2f}")

            if len(items_list) < 1:
                print("You don't have any item in your shopping cart.")
            else:
                print(f"You have {len(items_list)} items in your shopping cart.")

        elif action == 3:
            print("The contents of the shopping cart are:")
            for i in range(len(items_list)):
                item = items_list[i]
                price = prices_list[i]
                human_count = i + 1
                print(f"{human_count}. {item} - ${price:.2f}")

            if len(items_list) < 1:
                print("You don't have any item in your shopping cart.")
            else:
                print(f"You have {len(items_list)} items in your shopping cart.")

                remove = int(input("Which item would you like to remove? "))
                if remove < 1 or remove > len(items_list):
                    print("Sorry, that is not a valid item number.")      
                else:                
                    remove = remove - 1
                    items_list.pop(remove)
                    prices_list.pop(remove)
                    print("Item removed.")  
                    print(f"Now you already have {len(items_list)} items in your shopping cart.") 

        elif action == 4:
            for k in range(len(prices_list)):
                total += float(prices_list[k])
            print(f"The total price of the items in the shopping cart is ${total:.2f}")

        else:
            print("Thank you. Goodbye.")
