#     An institution has decided to admit new candidates in different streams on the following criteria:
#
# Total Marks Obtained                               Streams Offered
#
# 300 and above                                          Science
# 200 and above but less than 300            Commerce
# Below 200 but not below 75                    Arts
# Otherwise                                                  Admission is not granted,
#                                                        You have to appear in qualifying examination
#
# Write a program to input total marks obtained in an examination and print the stream allotted on the basis of above criteria.

marks = int(input("Enter the Total Marks Obtained: "))
if marks >= 300:
    print(f"For {marks} total marks stream offered is Science")
elif marks >= 200 and marks < 300:
    print(f"For {marks} total marks stream offered is Commerce")
elif marks >= 75 and marks < 200:
    print(f"For {marks} total marks stream offered is Arts")
else:
    print(f"""For {marks} marks obtained Admission is not granted
You have to appear in qualifying examination""")


"""Output:
Enter the Total Marks Obtained: 250
For 250 total marks stream offered is Commerce"""

"""Output:
Enter the Total Marks Obtained: 50
For 50 marks obtained Admission is not granted
You have to appear in qualifying examination"""