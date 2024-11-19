'''You are building a calculator application that allows users to input two numbers and perform arithmetic operations such as addition, subtraction, multiplication, and division. However, before performing any calculations, the program must validate that both inputs are numbers. If the inputs are not numerical (e.g., the user enters text or special characters), the program raises a TypeError to indicate invalid input.'''

# Write a Python program that prompts the user to input two numbers and raises a TypeError,valueError and ZeroError exception if the inputs are not numerical.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    d = a+b
    e = a-b
    f = a*b
    c = a/b
except TypeError:
    print("Invalid input. Please enter a valid integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("The result of the division is: ", c)
    print("The result of the addition is: ", d)
    print("The result of the subtraction is: ", e)
    print("The result of the multiplication is: ", f)
finally:
    print("The program has ended.")