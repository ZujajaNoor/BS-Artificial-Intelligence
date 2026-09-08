#Write a Python program that takes two numbers as input and calculates the first number raised to the power of the
# second number.

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
exponent = 1

for i in range(num2):
    exponent *= num1

print(str(num1) + "^" + str(num2) + " = " + str(exponent3))