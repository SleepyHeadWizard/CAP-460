a = int(input("Enter first number"))
b = int(input("Enter second number"))

while(a!=b):
    if(a>b):
        a-=b
    else:
        b-=a
        print("gcd = ",a)       