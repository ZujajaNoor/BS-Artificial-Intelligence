# Write a Python program to find the smallest number in the following list using a for loop.
# my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
# Print the smallest number as the output.

my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

smallest = my_list[0]

for i in my_list:
    if i < smallest:
        smallest = i

print(f"Smallest Number: {smallest}")