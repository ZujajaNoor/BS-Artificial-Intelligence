#Write a Python program that takes temperature in Celsius as input from the user and converts it to Fahrenheit.

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("The temperature in fahrenheit is: " + str(fahrenheit))