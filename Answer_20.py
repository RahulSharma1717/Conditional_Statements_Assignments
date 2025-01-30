# Design a Program to input two integers num1, num2 and a character(opr). The Variable opr reads only one of the four characters(+,-,/,*).
# Your Program should perform the operation on the basis of operator on num1, num2.
# In case of subtraction, subtract smaller number from bigger number and in case of division divide the greater number by smaller numbers.

def math_operator(num1, num2, opr):
    if opr == '+':
        result = num1 + num2
        return result

    elif opr == '-':
        if num1 > num2:
            result = num1 - num2
            return result
        else:
            return "Invalid Input: Enter first number greater than second number"

    elif opr == '*':
        result = num1 * num2
        return result

    elif opr == '/':
        if num2 == 0:
            return "Division by Zero Error"
        elif num1 > num2:
            result = num1 / num2
            return result
        else:
            return "Invalid Input: Enter first number greater than second number"

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
opr = input("Choose a character from the following (+,-,/,*): ")

final_result = math_operator(num1, num2, opr)
print(final_result)