a = input("Enter a string: ")
palindrom = True

for i in range(len(a) // 2):
    if a[i] != a[-1 - i]:
        palindrom = False
        break
if palindrom:
    print('YES')
else:
    print('NO')