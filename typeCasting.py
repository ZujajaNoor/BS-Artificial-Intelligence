#What does the following Python code do? Explain the type conversion that happens in this program.

age = 20
item = 5
print("age : ",age)
print("items : ", item)

age = float(age)
item = float(item)
print("age : ",age)
print("items: ", item)

#ANSWER
#In this program, two integer variables, are initialized with the values 20 and 5.
#Their values are first printed as integers. Then, the float() function is used to convert the data type of both variables
# from int to float. After conversion, their values are printed again. The numerical values remain the same, but their
# data types change. Therefore, 20 becomes 20.0 and 5 becomes 5.0.
#So, this program demonstrates type conversion from integer to floating point in Python.
