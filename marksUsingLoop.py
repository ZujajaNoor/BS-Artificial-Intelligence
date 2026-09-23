# Ask the user for the marks of 5 subjects.
# Calculate:
# Total marks
# Percentage
# Grade
# Pass/Fail
# Use a loop to enter the marks.

total = 500
obtained = 0
for i in range(1, 6):
    totMarks = int(input(f"Enter marks of subject {i}: "))
    obtained+= totMarks

per = (obtained/total)*100

if totMarks > 40:
    result = "PASS"
    if per <= 100 and per >= 80:
        grade = "A+"

    elif per < 80 and per >= 70:
        grade = "A"

    elif per < 70 and per >= 60:
        grade = "B"

    elif per < 60 and per >= 50:
        grade = "C"

    else:
        grade = "D"

else:
    result = "FAIL"
    grade = "F"

print("\n=====MARKSHEET=====")
print("Obtained Marks(out of 500)= " + str(obtained))
print("Percentage= " + str(per))
print("Result= " + result)
print("Grade= " + grade)