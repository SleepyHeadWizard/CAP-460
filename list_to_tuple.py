'''You are given a list of integers. Write a Python program to perform the following tasks:
 1.convert a list to a tuple.
 2.remove all prime numbers present in tuple.
 3.Reverse the tuple.
 4.Find the length of the tuple.'''

a = [3, 6, 2, 7, 8, 5]
b = tuple(a)
print('Tuple:', b)

c = []
for i in b:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            c.append(i)
            
d = list(b)
for i in c:
    d.remove(i)
b = tuple(d)
print('Tuple after removing prime numbers:', b)

print('Reversed tuple:', b[::-1])
print('Length of tuple:', len(b))