#Write a Python program that takes hours worked and hourly rate as input from the user, then calculates and displays
#the gross pay

hours = int(input("How much hours did you work? "))
hourly_Rate = int(input("How much per hour you earn? "))
grossPay = hours*hourly_Rate

print(f"The total money you earned {grossPay}")