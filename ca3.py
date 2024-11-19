'''Develop student grade management system for a school. The system should allow teachers to input student grades and perform various operations on the data.
Implement the following functionalities:
1.Add Student Grades:
Teachers should be able to input grades for different subjects for each student.
Store the data in a dictionary where the keys are student IDs and the values are lists of grades.
Apply TypeError: If the grade is entered as an incorrect type (e.g., a string instead of an integer or float).
2.Calculate Averages:
Calculate the average grade for each student across all subjects.
Appy ZeroDivisionError: If a student has no grades entered yet (division by zero error).
3.Grade Lookup:
Allow teachers to look up a student's grades by entering their ID.
Display the student's grades for all subjects.'''



students = {
            1223: {'maths': [25.0], 'english': [28.0]}, 
            1225: {'maths': [21.0], 'english': [30.0]}
            }

def add_student_grade(student_id, subject, grade):
    try:
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be an integer or float")
        if student_id not in students:
            students[student_id] = {}
        if subject not in students[student_id]:
            students[student_id][subject] = []
        students[student_id][subject].append(grade)
    except (TypeError,ValueError) as e:
        print(e, "Please enter a valid input")

def calculate_averages():
    try:
        for student_id, subjects in students.items():
            total_grades = 0
            total_count = 0
            for subject, grades in subjects.items():
                if len(grades) == 0:
                    raise ZeroDivisionError
                total_grades += sum(grades)
                total_count += len(grades)
            if total_count == 0:
                raise ZeroDivisionError
            overall_average = total_grades / total_count
            print(f"Student ID: {student_id}, Overall Average Grade: {overall_average}")
    except ZeroDivisionError:
        print("Division by zero is not allowed")

def grade_lookup(student_id):
    try:
        if student_id not in students:
            raise KeyError
        return students[student_id]
    except KeyError:
        return "Student not found"

while True:
    print(students)
    print("1. Add Student Grades")
    print("2. Calculate Averages")
    print("3. Grade Lookup")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_id = int(input("Enter student ID: "))
        subject = input("Enter subject: ")
        grade = float(input("Enter grade: "))
        add_student_grade(student_id, subject, grade)
    elif choice == 2:
        calculate_averages()
    elif choice == 3:
        student_id = int(input("Enter student ID: "))
        print(grade_lookup(student_id))
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")