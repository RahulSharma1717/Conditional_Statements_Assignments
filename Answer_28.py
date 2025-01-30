# Take three sides (number) from the user and tell whether the triangle is isosceles, scalene and equilateral triangle.


def classify_triangle():
    try:
        side1 = float(input("Enter the first side of the triangle: "))
        side2 = float(input("Enter the second side of the triangle: "))
        side3 = float(input("Enter the third side of the triangle: "))

        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if side1 == side2 == side3:
                return "The triangle is an Equilateral triangle."
            elif side1 == side2 or side1 == side3 or side2 == side3:
                return "The triangle is an Isosceles triangle."
            else:
                return "The triangle is a Scalene triangle."
        else:
            return "The given sides do not form a valid triangle."

    except ValueError:
        return "Invalid input! Please enter numeric values for the sides."


triangle_type = classify_triangle()
print(triangle_type)
