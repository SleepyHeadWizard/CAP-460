number = bool(input("Enter a number: "))
original_number = number
reversed_number = 0

while number > 0:
  remainder = number % 10
  reversed_number = (reversed_number * 10) + remainder
  number = number // 10

if original_number == reversed_number:
  print(f"{original_number} is a palindrome")
else:
  print(f"{original_number} is not a palindrome")
