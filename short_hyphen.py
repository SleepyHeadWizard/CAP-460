'''
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

''' 
string = input("Enter a hyphen-separated sequence of words: ")

def sort_hyphen(s):

    return '-'.join(sorted(s.split('-')))

print(sort_hyphen(string))
