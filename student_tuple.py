'''You are building a simple student score tracker where each student’s name and their respective scores in different subjects are stored in a tuple. You need to store data like this: ("John", 85, 90, 92) for each student. 
 
Task: Write a program that takes input for 3 students, where each student’s data is a tuple containing their name and three scores. Then, calculate and print each student's average score.'''
# use loop to take input for 3 students
# calculate average score for each student
# print average score for each student

students = []
for i in range(3):
    name = input('Enter student name: ')
    score1 = int(input('Enter score 1: '))
    score2 = int(input('Enter score 2: '))
    score3 = int(input('Enter score 3: '))
    student = (name, score1, score2, score3)
    students.append(student)
    
for j in students:
    avg = round(sum(j[1:]) / 3,2)
    print(j[0], 'average score:', avg)
    