'''
This is a simple program that takes in a score and returns a grade based on the score.
grade: score
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: below 60
use conditional statement to implement the logic.
'''
while True:
    score = int(input("Enter the score: "))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
            
