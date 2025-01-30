#     Write a python program that will check for the following conditions:
# ·         If the light is green – Car is allowed to go
# ·         If the light is yellow – Car has to wait
# ·         If the light is red – Car has to stop
# ·         Other signal – unrecognized signal. Example black, blue, etc…

signal = input('Enter the color of the signal: ').lower()

if signal == 'green':
    print("Car is allowed to go")
elif signal == 'yellow':
    print("Car has to wait")
elif signal == 'red':
    print("Car has to stop")
else:
    print(f"unrecognized signal {signal}")


"""Output:
Enter the color of the signal: WHITE
unrecognized signal white
"""