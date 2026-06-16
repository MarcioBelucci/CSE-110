import math
def compute_area_square(side):
    
    square_area = side * side
    return square_area

def compute_area_rectangle(length, width):
    
    rectangle_area = length * width
    return rectangle_area

def compute_area_circle(radius):
    
    circle_area = math.pi * (radius ** 2)
    return circle_area
    
question = ""

while question != "quit":
    question = input("What kind of the shape do you want to calculate? Square, rectangle, circle or quit? ").lower()
    if question == "square":
        square = float(input("What is the length of a side of the square? "))
        print(f"The area of the square is: {compute_area_square(square):.1f}\n")

    elif question == "rectangle":
        rectangle_length = float(input("What is the length of rectangle? "))
        rectangle_width = float(input("What is the width of the rectangle? "))
        print(f"The area of the rectangle is: {compute_area_rectangle(rectangle_length, rectangle_width):.1f}\n")

    elif question == "circle":   
        circle = float(input("What is the radius of the circle? "))

        print(f"The area of the circle is: {compute_area_circle(circle):.2f}\n")

    else: 
        exit()