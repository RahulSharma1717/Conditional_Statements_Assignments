# A University allows students to sit in the exam despite of insufficient attendance if the student's attendance is short due to some medical cause.
# Take Input from User whether he had medical cause (Y/N) and print the message you are allowed if medical cause == Y otherwise print you are not allowed.

user_input = input("Enter whether you had a medical case, Answer 'Y' for yes and 'N' for no: ").upper()

if user_input == 'Y':
    print("You are allowed for the exam")
else:
    print("You are not allowed for the exam")


"""Output:
Enter whether you had a medical case, Answer 'Y' for yes and 'N' for no: y
You are allowed for the exam
"""