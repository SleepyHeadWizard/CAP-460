'''
Write a Python function that accepts a string and counts the number of upper and lower case letters.

Sample String : 'The quick Brow Fox'

Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

string = 'The quick Brow Fox'

def count_fun_for_str(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

upper_count, lower_count = count_fun_for_str(string)
print(f"No. of Upper case characters : {upper_count}")
print(f"No. of Lower case Characters : {lower_count}")