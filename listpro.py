'''
Problem Statement:

You are given a list of integers. Write a Python program to perform the following tasks:

Split into Even and Odd Lists: Separate the list into two new lists — one containing all the even numbers and the other containing all the odd numbers.
Sort Both Lists: Sort both the even and odd lists in descending order.
Merge the Lists: Merge the sorted even and odd lists back together, where all the even numbers appear before the odd numbers.
Calculate Product: Calculate the product of all numbers in the final merged list.
Example:

Input: [3, 6, 2, 7, 8, 5]

Output:

Even numbers: [8, 6, 2]
Odd numbers: [7, 5, 3]
Merged list: [8, 6, 2, 7, 5, 3]
Product: 10080
'''
a = [3, 6, 2, 7, 8, 5]
even = []
odd = []
for i in a:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.sort(reverse=True)
odd.sort(reverse=True)
merged = even + odd
product = 1
for i in merged:
    product *= i
print('Even numbers:', even)
print('Odd numbers:', odd)
print('Merged list:', merged)
print('Product:', product)