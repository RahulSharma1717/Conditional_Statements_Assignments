# Write a program to take number input between 1 to 7 and print the day associated to that number such as 1 for Sunday, 2 for Monday, etc.

weekdays = ["", 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

i = 0
while i < 10:
    number = int(input("Enter number from 1-7: "))
    if number >= 1 and number <=7:
        print(f"Number entered is '{number}' corresponding to the day '{weekdays[number]}'")
    else:
        print("Enter a number from 1 to 7")
    i += 1


"""Output:
Enter number from 1-7: 5
Number entered is '5' corresponding to the day 'Thursday'
Enter number from 1-7: 7
Number entered is '7' corresponding to the day 'Saturday'
Enter number from 1-7: 1
Number entered is '1' corresponding to the day 'Sunday'
Enter number from 1-7: 8
Enter a number from 1 to 7
"""