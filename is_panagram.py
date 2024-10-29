'''Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
#anagram

'''

string = input("Enter a string: ")

def is_panagram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
    return True

if is_panagram(string):
    print(f'"{string}" is a pangram')
else:
    print(f'"{string}" is not a pangram')