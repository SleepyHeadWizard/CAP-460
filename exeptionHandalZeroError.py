'''Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''

try:
    a = 10/0
except ZeroDivisionError:
    print("Division by zero is not allowed")