# Write a program to take number input between 1 and 12 and print the month associated with it.

month = ["", 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

i = 0
while i < 12:
    number = int(input("Enter number from 1-12: "))
    if number >= 1 and number <= 12:
        print(f"Number entered is '{number}' corresponding to the Month '{month[number]}'")
    else:
        print("Enter a number from 1 to 12")
    i += 1


"""Output:
Enter number from 1-12: 25
Enter a number from 1 to 12
Enter number from 1-12: 5
Number entered is '5' corresponding to the Month 'May'
Enter number from 1-12: 12
Number entered is '12' corresponding to the Month 'December'
Enter number from 1-12: 11
Number entered is '11' corresponding to the Month 'November'
Enter number from 1-12: 1
Number entered is '1' corresponding to the Month 'January'
"""