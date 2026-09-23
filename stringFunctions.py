# Take a student's name and display:
# Name in uppercase
# Name in lowercase
# Number of characters
# First character
# Last character

stdName = input("Enter your name: ")
print(f"Your name in capital letters: {stdName.upper()}")
print(f"Your name in small letters: {stdName.lower()}")
print(f"Your name's contain {len(stdName)} letters")
print(f"Your name's first letter: {stdName[0]}")
print(f"Your name's last letter: {stdName[-1]}")