'''
convert faranheit to celsius and vice versa
'''
while True:
    temp = input("Enter the temperature you want to convert: ")
    if temp=="f":
        f = float(input("Enter the temperature in farenheit: "))
        c = (f-32)*5/9
        print(f"{f} F is {c} *C")
    elif temp=="c":
        c = float(input("Enter the temperature in celsius: "))
        f = (c*9/5)+32
        print(f"{c} C is {f} *F")