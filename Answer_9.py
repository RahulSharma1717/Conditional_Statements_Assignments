# Write a program to check whether a number entered by user is even or odd.

number = int(input("Enter the number: "))

if number % 2 == 0:
    print(f"Entered number '{number}' is even")
else:
    print(f"Entered number '{number}' is odd")


"""Output:
Enter the number: 85
Entered number '85' is odd
"""