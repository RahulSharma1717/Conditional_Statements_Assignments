# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :

units_used = float(input("Enter the number of Electricity units used: "))

if units_used <= 100:
    elec_bill = 0
    print(f"For first 100 units consumed electricity bill: {elec_bill}")

elif 100 < units_used <= 200:
    elec_bill = 5 * (units_used - 100)
    print(f"Electricity bill if units used are in between 100 to 200: {elec_bill}")

else:
    elec_bill = 10 * (units_used - 200) + 5 * 100
    print(f"Electricity bill if units used are more than 200: {elec_bill}")


"""Output:
Enter the number of Electricity units used: 246
Electricity bill for units used more than 200: 960.0
"""