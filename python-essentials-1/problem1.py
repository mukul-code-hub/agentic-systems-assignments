# Solve Number operator with Error Handling
#Take two number as input from user and perform addition, subtraction, multiplication and division and handle the error if user.
str1 = input("Enter first number: ")
str2 = input("Enter second number: ")
try:
    int1 = int(str1)
    int2 = int(str2)
    sum = int1 + int2
    print("Sum:", sum)

    division = int1 / int2
    print("Division:", division)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")