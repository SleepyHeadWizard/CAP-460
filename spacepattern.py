#write a python code to print this pattern-
#     *
#    **
#   ***
#  **** 
# *****
n = 5  # Set the number of rows

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


            
