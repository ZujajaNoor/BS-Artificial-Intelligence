#Write a Python program to create an #advanced student marksheet. The program #should:
#1. Ask the user to enter the student's name and roll number.
#2. Input marks for 5 subjects.
#3. Calculate the total marks and percentage.
#4. Determine the grade according to:
#5. Check whether the student passed or failed
#6. If the student scores below 40 in any subject, declare the student a Fail regardless of the
verall percentage.
#7. Display a complete marksheet containing the student's information, such as name and
#roll no., subject marks, total, percentage, grade, and result.

stdName = input("Enter your name: ")
rollNo = input("Enter your roll no: ")
sub1 = int(input("Enter your IoT marks: "))
sub2 = int(input("Enter your ICT marks: "))
sub3 = int(input("Enter your OOP marks: "))
sub4 = int(input("Enter your DLD marks: "))
sub5 = int(input("Enter your Math marks: "))

obtain = sub1+sub2+sub3+sub4+sub5
per = (obtain/500)*100

if sub1 < 40 or sub2 < 40 or sub3 < 40 or sub4 < 40 or sub5 < 40:
    result = "FAIL"
    grade = "F"

else:
    result = "PASS"
    if per <= 100 and per >= 80:
        grade = "A+"

    elif per < 80 and per >= 70:
        grade = "A"

    elif per < 70 and per >= 60:
        grade = "B"

    elif per < 60 and per >= 50:
        grade = "C"
    
    elif per < 50 and per >= 40:
        grade = "D"
    
    else:
        result = "FAIL"
        grade = "F"
 
print("\n=====MARKSHEET=====")
print("Name = " + stdName)
print("Roll No = " + rollNo)
print("IoT Marks= " + str(sub1))
print("ICT Marks= " + str(sub2))
print("OOP Marks= " + str(sub3))
print("DLD Marks= " + str(sub4))
print("Math Marks= " + str(sub5))
print("Obtained Marks(out of 500)= " + str(obtain))
print("Percentage= " + str(per))
print("Result= " + result)
print("Grade= " + grade)