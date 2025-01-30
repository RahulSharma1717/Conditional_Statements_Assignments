# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter you annual salary in rupees: "))
service = int(input("Enter the number of years you have served in the company: "))

bonus = 5/100*salary
if service >= 5:       # As the person who has worked for 5 years and few months will also mention his years of service as 5
    print(f"Net Bonus Amount received is {bonus}")
else:
    print("No Bonus")


"""Output:
Enter you annual salary in rupees: 800000
Enter the number of years you have served in the company: 8
Net Bonus Amount received is 40000.0
"""