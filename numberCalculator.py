# Ask the user to enter 10 numbers.
# Calculate:
# Sum
# Average
# Largest number
# Smallest number
# Number of even numbers
# Number of odd numbers

sum = 0
odd = even = 0
print("\n/ENTER NUMBERS/")

for i in range(1,11):
    number = int(input(f"Number {i}: "))
    sum += number

    if number%2 == 0:
        even += 1
    else:
        odd += 1

    if i == 1:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

average = sum/i

print("\n=====Number Calculator=====")
print(f"Sum = {sum}")
print(f"Average = {average}")
print(f"Number of even integers = {even}")
print(f"Number of odd integers = {odd}")
print(f"Largest Number = {largest}")
print(f"Smallest Number = {smallest}")