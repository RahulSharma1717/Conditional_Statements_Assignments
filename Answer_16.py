# Calculate income tax for the given income by adhering to the below rules
# Taxable Income        Rate (in %)
# First Rs.1,00,000         0
# Next Rs. 1,00,000        10
# The remaining            20

income = int(input("Enter your yearly income: "))

if income <= 100000:
    tax = 0
    print(f"Tax on income {income} is {tax}")

elif 100000 < income <= 200000:
    tax = (income - 100000) * 10/100
    print(f"Tax on income {income} is {tax}")

else:
    tax = 20/100*(income-200000) +  10/100*(100000)
    print(f"Tax on income {income} is {tax}")


"""Output:
Enter your yearly income: 230000
Tax on income 230000 is 16000.0
"""