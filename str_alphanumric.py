'''You are given a string containing both letters and digits. Write a Python program to perform the following tasks:

Separate Letters and Digits: Extract all the letters and digits from the string into two separate strings.
Count Vowels and Consonants: Count the number of vowels and consonants in the string of letters.
Find the Largest and Smallest Digit: Find the largest and smallest digits from the string of digits.
Reverse the Letters: Reverse the order of characters in the string of letters.
Check Palindrome: Check if the string of letters is a palindrome.
Example:

Input:
s = "a1b2c3de4fgh"
Output:

Letters: "abcdefgh"
Digits: "1234"
Vowels: 2, Consonants: 6
Largest digit: 4, Smallest digit: 1
Reversed letters: "hgfedcba"
Palindrome check: False'''

s = "a1b2c3de4fgh"
letters = []
digits = []
vowels = 0
consonants = 0
largest_digit = -1
smallest_digit = 10

for i in s:
    if i.isalpha():
        letters.append(i)
        if i in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif i.isdigit():
        digits.append(i)
        if int(i) > largest_digit:
            largest_digit = int(i)
        if int(i) < smallest_digit:
            smallest_digit = int(i)

letters_str = ''.join(letters)
digits_str = ''.join(digits)

print('Letters:', letters_str)
print('Digits:', digits_str)
print('Vowels:', vowels, ', Consonants:', consonants)
print('Largest digit:', largest_digit, ', Smallest digit:', smallest_digit)
print('Reversed letters:', letters_str[::-1])
print('Palindrome check:', letters_str == letters_str[::-1])