list_numbers = []
new_number = 1
sum = 0
average = 0
largest = 0
smallest = 9999
print("Enter a list of numbers, type 0 when finished.")
while new_number != 0:
    new_number = int(input("Enter number: "))
    if new_number != 0:
        list_numbers.append(new_number)
        sum += new_number
        if new_number > largest:
            largest = new_number
        if new_number < smallest and new_number > 0:
            smallest = new_number

average = sum / len(list_numbers)
print(f"The sum is: {sum}")
print(f"The average is: {average:.2f}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")