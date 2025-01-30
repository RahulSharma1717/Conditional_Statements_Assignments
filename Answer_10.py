# Write a program to check whether a given character is a vowel or a consonant.

char = input("Enter a charater: ")
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

if char in vowels.lower():
    print(f"Entered character '{char}' is a vowel")
elif char in consonants.lower():
    print(f"Entered character '{char}' is a consonant")
else:
    print("ERROR! Please enter an english alphabet")


"""Output:
Enter a charater: K
Entered character 'K' is a consonant
"""

