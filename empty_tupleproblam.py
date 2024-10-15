'''Write a Python program to remove an empty tuple(s) from a list of tuples. 
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')] 
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''


list=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_list=[]
for i in list:
    if len(i) != 0:
        new_list.append(i)     
print(new_list)