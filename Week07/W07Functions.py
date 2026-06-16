def display_regular(user_input):
    """
    Purpose: This function will show the input as it is
    """
    print(user_input)

def display_uppercase(user_input):
    """
    Purpose: This function will show the input in uppercase
    """
    user_input = user_input.upper()
    print(user_input)

def display_lowercase(user_input):
    """
    Purpose: This function will show the input in lowercase
    """
    user_input = user_input.lower()
    print(user_input)
    
message = input("What is your message? ")
display_regular(message)
display_uppercase(message)
display_lowercase(message)