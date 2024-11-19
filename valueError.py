'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.'''

try:
    a = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")