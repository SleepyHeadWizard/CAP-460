# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

# Take input from the user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

prime = True

for number in numbers:
    if number <= 1:
        prime = False
        break
    if number == 2:
        continue
    if number % 2 == 0:
        prime = False
        break
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            prime = False
            break
    if not prime:
        break

print(prime)

