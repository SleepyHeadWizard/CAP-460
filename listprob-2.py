'''Problem Statement: 
 
You are given a list of integers. Write a Python program to perform the following tasks: 
 
Remove Duplicates: Remove any duplicate elements from the list, maintaining the order of the first occurrence of each number. 
Sort the List: Sort the remaining elements of the list in ascending order. 
Sum of List: Find the sum of the list after removing duplicates and sorting. 
Find Max and Min: Find the maximum and minimum values in the list.'''

a = [3, 6, 2, 7, 8, 5, 3, 6, 2, 7, 8, 5]
b = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
sum = 0
for i in b:
    sum += i
print('List after removing duplicates:', b)
print('Sum of list:', sum)
print('Max:', max(b))
print('Min:', min(b))