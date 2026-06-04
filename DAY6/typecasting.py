# Type Casting in Python means converting one data type into another data type.


# Type Casting in Python

name = "Monu"
age = "20"
height = "5.8"
is_student = "True"

print("Before Type Casting")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print()

# Type Casting
age = int(age)
height = float(height)
is_student = bool(is_student)

print("After Type Casting")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print()

print("Student Information")
print("Name :", name)
print("Age :", age)
print("Height :", height)
print("Student Status :", is_student)

# print()


