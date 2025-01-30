# A Bank offers the following rate of interest for fixed deposit:
#
#                         Time(Years)                                                Rate(%)
#                         <1                                                       9.0
#                         1 to 2                                                 10.0
#                         2 to 3                                                 11.0
#                         >3                                                       12.0
#
# The amount A after n years is calculated by using the formula:
#                                     A = P(1 + r / 100)^n
# Where P = principal amount deposited
#             R = rate of interest
#             N = number of years
# Write a program to accept the deposited amount, number of years the amount is to be deposited for n and compute accrued amount for an investor.

def fixed_deposit(p, n):
    if n < 1 and n> 0:
        r = 9
    elif n >= 1 and n < 2:
        r = 10
    elif n >=2 and n < 3:
        r = 11
    elif n >= 3:
        r = 12
    else:
        print("Enter a valid duration in years")
    Amount = p * (1 + r / 100) ** n
    print(f"Rate of interest applied is '{r}%' per annum")
    return round(Amount, 2)

P = int(input("Enter the principal amount deposited: "))
N = float(input("Enter the time duration for which you wish to deposit the money: "))

total_amount = fixed_deposit(P, N)
print(f"Accured Amount after '{N}' years equals '{total_amount}'")


"""Output:
Enter the principal amount deposited: 10000
Enter the time duration for which you wish to deposit the money: 2.5
Rate of interest applied is '11%' per annum
Accured Amount after '2.5' years equals '12980.98'
"""

