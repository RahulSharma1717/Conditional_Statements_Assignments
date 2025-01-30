# Function to calculate the sum of digits recursively
def sum_of_digits(n):
    # Base case: if the number is a single digit, return the number itself
    if n < 10:
        return n
    # Recursive case: return the last digit plus the sum of the remaining digits
    return (n % 10) + sum_of_digits(n // 10)

# Example usage
number = 6789
print(f"The sum of the digits in {number} is: {sum_of_digits(number)}")
