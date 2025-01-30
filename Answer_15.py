# Write a program to check whether the given number is positive, zero or negative.

number = int(input("Enter an integer number: "))

if number > 0:
    print(f"Number entered {number} is a positive number ")
elif number == 0:
    print(f"Number entered is zero")
else:
    print(f"Number entered {number} is a negative number")


"""Output:
Enter an integer number: -42
Number entered -42 is a negative number
"""