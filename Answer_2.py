# Apple considers any iPhone with a battery health of 80% or above, to be in optimal condition.
# Given that your iPhone has XX% battery health, find whether it is in optimal condition.
# Take Battery Health from User and print YES if in optimal condition and NO if not.

battery_health = int(input("Enter your iPhone battery's health: "))

if battery_health >= 80:
    print("YES, your iPhone's battery is in optimal condition")
else:
    print("NO, the phone battery needs to be checked, please visit service center")


"""Output:
Enter your iPhone battery's health: 45
NO, the phone battery needs to be checked, please visit service center
"""
