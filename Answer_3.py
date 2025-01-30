# While purchasing certain items, a discount of 10 % is offered if the quantity purchased is more than 1000.
# If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

quantity = int(input("Enter the quantity of item: "))
price = float(input("Mention the price of the item: "))

if quantity > 1000:
    total_expense = (quantity * price) - (quantity * price) * 10/100

else:
    total_expense = (quantity * price)

print(f"Total expense is {total_expense}")


"""Output:
Enter the quantity of item: 999
Mention the price of the item: 10
Total expense is 9990.0


Enter the quantity of item: 1001
Mention the price of the item: 10
Total expense is 9009.0
"""