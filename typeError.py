'''Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.'''

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
except TypeError:
    print("Invalid input. Please enter a valid integer.")
    