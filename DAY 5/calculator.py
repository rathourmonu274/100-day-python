# this is the simple calculator using arithmatic operations

num1 = float(input("Enter the first number here = "))
num2 = float(input("Enter the second number here = "))
print("Enter 1 for 'Addition'"
      "\nEnter2 for 'Subtraction' "
      "\nEnter 3 for 'Multiply' "
      "\nEnter 4 for 'Division'")

Enter_number = int(input("Enter number from 1 to 4 :"))

if Enter_number == 1:
    print("Addition of your first and second number is :", num1+num2)
elif Enter_number == 2:
    print("Subtraction of your first and second number is :", num1-num2)
elif Enter_number == 3:
    print("Multiply of your first and second number is :", num1*num2)
elif Enter_number == 4:
    print("Division your first and second number is :", num1 / num2)
else:
    print("Invalid Number")