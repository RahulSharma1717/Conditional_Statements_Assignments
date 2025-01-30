# Write a menu driven program for making a simple calculator.

menu = input("""Enter the operation you wish the calculator to perform
                 1) For Addition of two numbers input 'ADD'
                 2) For Substraction of two numbers input 'SUB'
                 3) For Multiplication of two numbers input "MUL'
                 4) For Division of two numbers input "DIV'
                 """).upper()

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if menu == 'ADD':
    addition = num_1 + num_2
    print(addition)
elif menu == "SUB":
    substraction = num_1 - num_2
    print(substraction)
elif menu == "MUL":
    multiplication = num_1 * num_2
    print(round(multiplication, 3))
elif menu == "DIV":
    if num_2 == 0:
        print("Division by Zero Error")
    else:
        division = num_1 / num_2
        print(round(division, 3))
else:
    print("Input a valid operation")


"""Output:
Enter the operation you wish the calculator to perform
                 1) For Addition of two numbers input 'ADD'
                 2) For Substraction of two numbers input 'SUB'
                 3) For Multiplication of two numbers input "MUL'
                 4) For Division of two numbers input "DIV'
                 div
Enter the first number: 9
Enter the second number: 0
Division by Zero Error"""

"""Output:
Enter the operation you wish the calculator to perform
                 1) For Addition of two numbers input 'ADD'
                 2) For Substraction of two numbers input 'SUB'
                 3) For Multiplication of two numbers input "MUL'
                 4) For Division of two numbers input "DIV'
                 mul
Enter the first number: 56.3247
Enter the second number: 78.958412
4447.309
"""