#     A Scooter /motor cycle stand charges the following rates for the parking:
#
#        Hours                                         Rate
#
#       First 4hours                                  RS.5.00
# Every next hour upto 5 hours                   RS.3.00 per hour
# Any further hour above 9 hour                  RS.2.00 per hour
#
# Write a program to input the number of hours for which a two wheeler is parked. Calculate and print the parking charges to be paid by the customer.

parking_time = int(input("Enter the number of hours the two wheeler was parked: "))
if parking_time <= 4 and parking_time > 0:
    parking_charges = 5
    print(f"Parking charges for {parking_time} hrs of parking is Rs.{parking_charges}")
elif parking_time > 4 and parking_time <= 9:
    parking_charges = 5 + (parking_time - 4) * 3
    print(f"Parking charges for {parking_time} hrs of parking is Rs.{parking_charges}")
elif parking_time > 9:
    parking_charges = 5 + 5 * 3 + (parking_time - 9) * 2
    print(f"Parking charges for {parking_time} hrs of parking is Rs.{parking_charges}")
else:
    print("Please enter a valid input")


"""Output:
Enter the number of hours the two wheeler was parked: 24
Parking charges for 24 hrs of parking is Rs.50
"""
