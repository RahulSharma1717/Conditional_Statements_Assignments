# Write a python program to accept the percentage from the user and display the category according to the following criteria:
# Percentage              Category
#
# <40                            Failed
# >=40 and <55           Fair
# >= 55 and <65          Good
# >= 65                         Excellent

percentage_marks = float(input("Enter the percentage marks scored in the exam: "))

if percentage_marks < 40 and percentage_marks >= 0:
    print(f"Marks Entered '{percentage_marks}%'")
    print("The candidate has failed the exam")
elif percentage_marks >= 40 and percentage_marks < 55:
    print(f"Marks Entered '{percentage_marks}%'")
    print("The candidate's performance is Fair")
elif percentage_marks >= 55 and percentage_marks < 65:
    print(f"Marks Entered '{percentage_marks}%'")
    print("The candidate's performance is Good")
elif percentage_marks >= 65 and percentage_marks <= 100:
    print(f"Marks Entered '{percentage_marks}%'")
    print("The candidate's performance is Excellent")
else:
    print("Enter a valid percentage score")


"""Output:
Enter the percentage marks scored in the exam: 115
Enter a valid percentage score
"""

"""Output:
Enter the percentage marks scored in the exam: 56.5
Marks Entered '56.5%'
The candidate's performance is Good
"""