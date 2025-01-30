# In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
# Jerry is running at a speed of XX metres per second while Tom is chasing him at a speed of YY metres per second. Determine whether Tom will be able to catch Jerry.
# Note that initially Jerry is not at the same position as Tom.
# Take X of Jerry and Y of Tom from the user and make decision and
# print YES if tom can catch and NO if not.

X = float(input("Enter Jerry's Speed: "))
Y = float(input("Enter Tom's Speed: "))
print(f"Jerry is running at {X} metres per second")
print(f"Tom is chasing Jerry at {Y} metres per second")

if Y>X:
    print('YES, tom will catch jerry')
else:
    print('NO, tom will not be able to catch jerry')


"""Output:
Enter Jerry's Speed: 10
Enter Tom's Speed: 12
Jerry is running at 10.0 metres per second
Tom is chasing Jerry at 12.0 metres per second
YES, tom will catch jerry
"""