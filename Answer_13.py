# Write a program to accept percentage from the user and display the grade according to the following criteria:

marks = float(input("Enter the %age of marks you received: "))

if marks >= 90:
    print("Grade awarded is 'A'")
elif 80 <= marks < 90:
    print("Grade awarded is 'B'")
elif 60 <= marks < 80:
    print("Grade awarded is 'C'")
else:
    print("Grade awarded is 'D'")


"""Output:
Enter the %age of marks you received: 67
Grade awarded is 'C'
"""