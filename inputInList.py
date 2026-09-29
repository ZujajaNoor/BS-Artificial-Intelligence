# Create an empty list:
# shopping = []
# Ask the user to enter 5 shopping items.
# Then display the complete shopping list.

shopping =[]
print("Enter 5 Shopping Items!")

for i in range(1, 6):
    items = input(f"Item {i}: ")
    shopping.append(items)

print(shopping)

