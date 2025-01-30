# Write a program to check whether the last digit of the number is divisible by 3 or not.
# Take Number from user and your output must contain the number.

number = int(input("Enter the number: "))
last_digit = number % 10

if last_digit % 3 == 0:
    print(f"The number {number} is divisible by 3")
else:
    print(f"The number {number} is not divisible by 3")


"""Outout:
Enter the number: 459873123
The number 459873123 is divisible by 3
"""