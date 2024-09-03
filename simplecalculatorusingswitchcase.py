num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
  result = num1 + num2
elif operator == '-':
  result = num1 - num2
elif operator == '*':
  result = num1 * num2
elif operator == '/':
  if num2 == 0:
    print("Error: Division by zero")
  else:
    result = num1 / num2
else:
  print("Invalid operator")

if result is not None:
  print("Result:", result)
