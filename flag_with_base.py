''' This program prints a flag with a triangle base.

    *************
    *************
    *************
    *************
    *
    *
    *
    *
    *
    *
    *
    ***
   *****
  *******
 *********
***********
'''
# for flag
for i in range(4):
    print(" " * 5 + "*" * 10)
    
# for flag pole
for i in range(7):
    print(" " * 5 + "*")
    
# for triangle base
for i in range(5):
    print(" " * (5 - i) + "*" * (2 * i + 1))
