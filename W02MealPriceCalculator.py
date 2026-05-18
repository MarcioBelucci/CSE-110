# I added a question about a tip. If the customers want to give a tip for the service team, the value will be added to the total.
# I put if and else to adapt the system's answer.
price_child = float(input("What is the price of a child's meal? "))
price_adult = float(input("What is the price of an adult's meal? "))
count_child = int(input("How many children are there? "))
count_adult = int(input("How many adults are there? "))

child_total = price_child * count_child
adult_total = price_adult * count_adult
subtotal = child_total + adult_total

print(f"\nSubtotal: ${subtotal:.2f}")

tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = (subtotal * tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

tip_question = input("\nWould you like to contribute with a tip for our service team? ")
if tip_question == "yes":
    tip = float(input("Tip: $"))
    total = total + tip
    print(f"Total: ${total:.2f}")
    payment_amount = float(input("\nWhat is the payment amount? "))
    change = payment_amount - total
    print(f"Change: ${change:.2f}")

else:
    payment_amount = float(input("\nWhat is the payment amount? "))
    change = payment_amount - total
    print(f"Change: ${change:.2f}")