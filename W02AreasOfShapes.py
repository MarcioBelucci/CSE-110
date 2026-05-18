#Square: The area is the length of a side squared.
#Rectangle: The area is the length multiplied by the width.
#Circle: The area is Pi (approximately 3.14) multiplied by the radius squared.
import math

square = float(input("What is the length of a side of the square? "))
square_area = square * square
print(f"The area of the square is: {square_area:.1f}")
rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width 
print(f"The area of the rectangle is: {rectangle_area:.1f}")
circle = float(input("What is the radius of the circle? "))
circle_area = math.pi * (circle ** 2)
print(f"The area of the circle is: {circle_area:.2f}")