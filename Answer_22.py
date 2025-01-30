#     Monthly Electricity bill is calculated as –
#
# Number of units Consumed                              Rate Per Unit
#
# <=100                                                only meter rent Rs 200/-
# For next 200 units                                   Rs. 1.00 per unit
# For next 200 units                                   Rs. 1.55 per unit
# For more than 500 units                              Rs. 2.10 per unit
#
# Write a program to take the consumer number, number of units consumed. Calculate bill amount.
# Print consumer number and total amount to be paid by the consumer. (Consumer number must be digits of length 5 and print appropriate message for incorrect input of consumer number).

def electricity_bill_generator():
    consumer_number = input("Please Enter your Customer ID: ")
    if len(consumer_number) == 5 and consumer_number.isdigit():
        print(f"{consumer_number} is Valid Consumer Number")
        units_consumed = float(input("Enter the Electricity Units Consumed in the month: "))
        if units_consumed <= 100 and units_consumed > 0:
            total_bill = 200
            return f"Total amount to be paid by the consumer is Rs.{total_bill}"
        elif units_consumed > 100 and units_consumed <= 300:
            total_bill = 200 + (units_consumed-100) * 1.00
            return f"Total amount to be paid by the consumer is Rs.{total_bill}"
        elif units_consumed > 300 and units_consumed <= 500:
            total_bill = 200 + 200 * 1.00 + (units_consumed-300) * 1.55
            return f"Total amount to be paid by the consumer is Rs.{total_bill}"
        elif units_consumed > 500:
            total_bill = 200 + 200 * 1.00 + 200 * 1.55 + (units_consumed-500) * 2.10
            return f"Total amount to be paid by the consumer is Rs.{total_bill}"
        else:
            return "Enter a Valid amount for Units Consumed"
    else:
         return "Consumer Number entered is incorrect, Please enter a valid 5-digit number"

bill = electricity_bill_generator()
print(bill)


"""Output:
Please Enter your Customer ID: 96321
96321 is Valid Consumer Number
Enter the Electricity Units Consumed in the month: 426
Total amount to be paid by the consumer is Rs.595.3
"""