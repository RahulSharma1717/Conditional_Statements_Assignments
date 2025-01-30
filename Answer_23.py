# Write a menu driven program for three options. (Take input of option from user).
# i)            Area of circle
# ii)           Area of Rectangle
# iii)          Area of Square
# Print the area along with sides.

import math
pi = math.pi

def area_of_circle(radius):
    return round(pi*(radius**2), 3)

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_square(side):
    return round(side**2, 3)

# Menu
menu = input("""Enter 'C' if you wish to calculate area of Circle
Enter 'R' if you wish to calculate area of Rectangle
Enter 'S' if you wish to calculate area of Square: """).upper()

if menu == 'C':
    radius = float(input("Enter the radius of the circle: "))
    circle = area_of_circle(radius)
    print(f"Area of the circle is {circle}")
elif menu == 'R':
    length = float(input("Enter the length of the side of rectangle: "))
    breadth = float(input("Enter the breadth of the side of rectangle: "))
    rectangle = area_of_rectangle(length, breadth)
    print(f"Area of the rectangle is {rectangle}")
elif menu == 'S':
    side = float(input("Enter the length of the side of the square: "))
    square = area_of_square(side)
    print(f"Area of the square is {square}")
else:
    print("Invalid Input")


"""Output:
Enter 'C' if you wish to calculate area of Circle
Enter 'R' if you wish to calculate area of Rectangle
Enter 'S' if you wish to calculate area of Square: s
Enter the length of the side of the square: 5.8945713
Area of the square is 34.746
"""