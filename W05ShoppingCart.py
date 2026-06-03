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
        if action == 1:
            item_name = input("What item would you like to add? ").lower()
            if item_name != "":
                items_list.append(item_name)
                price = float(input(f"What is the price of '{item_name}'? "))
                prices_list.append(price)
            else:
                print("Sorry, that is not valid item name.")
        
        elif action == 2:
            print("The contents of the shopping cart are:")
            for i in range(len(items_list)):
                item = items_list[i]
                price = prices_list[i]
                human_count = i + 1
                print(f"{human_count}. {item} - {price}")

        elif action == 3:
            print("The contents of the shopping cart are:")
            for i in range(len(items_list)):
                item = items_list[i]
                price = prices_list[i]
                human_count = i + 1
                print(f"{human_count}. {item} - {price}")

            remove = int(input("Which item would you like to remove? "))
            if remove != items_list[i]:
                print("Sorry, that is not a valid item number.")
            else:
                remove = remove - 1
                items_list.pop(remove)
                prices_list.pop(remove)
                print("Item removed.")

        #elif action == 4:
        
        #else:








#print(items_list)
#print(prices_list)
