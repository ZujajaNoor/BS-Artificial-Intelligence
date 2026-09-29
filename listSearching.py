# Create a list of student names:
# students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
# Ask the user to enter a student name.
# If the name exists, display:
# Student Found
# Otherwise:
# Student Not Found

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
stdName = input("Enter your name: ")
found = False

for std in students:
    if stdName.lower() == std.lower():
        found = True
        break

if found:
    print("Student found.")
else:
    print("Student not found!")