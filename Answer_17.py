# Write a program to take a digit and print it is In words(only 0 - 9)

digit = int(input("Enter a digit from 0-9: "))

if digit >= 0 and digit <= 9:
    if digit == 0:
        print('Zero')
    elif digit == 1:
        print('One')
    elif digit == 2:
        print('Two')
    elif digit == 3:
        print('Three')
    elif digit == 4:
        print('Four')
    elif digit == 5:
        print('Five')
    elif digit == 6:
        print('Six')
    elif digit == 7:
        print('Seven')
    elif digit == 8:
        print('Eight')
    elif digit == 9:
        print('Nine')
else:
    print('Digit is either less than 0 or greater than 9')