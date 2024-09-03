a = input('enter your string: ')
upper = 0
lower = 0

for i in a:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower +=1
        
print('UPPER CASE', upper)
print('LOWER CASE', lower)