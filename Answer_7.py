# Write a program to display ‘Hello’ if the number entered by user is multiple of 5 otherwise prints ‘Bye’.

input_number = int(input("Enter the required number: "))

if input_number % 5 == 0:
    print('Hello')
else:
    print('Bye')


"""Output:
Enter the required number: 63
Bye
"""