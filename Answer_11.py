# Write a program to check whether a given string is a valid email address (i.e., it contains exactly one "@" symbol and at least one "." after the "@").

mail_id = input("Enter your mail id: ")
count_at = mail_id.count('@')
index_at = mail_id.index('@')

if count_at == 1:
    dot_count = mail_id.count('.', index_at, len(mail_id))
    if dot_count >= 1:
        print(f"The entered mail id {mail_id} is valid")
    else:
        print(f"The entered mail id {mail_id} is invalid")
else:
    print(f"The entered mail id {mail_id} is invalid")



"""Output:
Enter your mail id: lostin.transition@gmail.com
The entered mail id lostin.transition@gmail.com is valid
"""