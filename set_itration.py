# Write a Python program to iterate over sets.
# Write a Python program to remove item(s) from a given set if not present print not available.
val={1,2,3,4,5,6,7,8,9,10}
for i in val:
    print(i)
    
if 5 in val:
    val.remove(5)
    print("\n",val)
else:
    print('not available')
    
