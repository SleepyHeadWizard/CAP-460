'''You are tasked with managing a list of students and their grades for a class. The application should allow users to perform the following tasks: 
 
Add a Student and Grade: Users can add a new student with their corresponding grade to the list. 
Update a Student's Grade: Users can update the grade of an existing student. 
Remove a Student: Users can remove a student from the list. 
Calculate the Average Grade: Users can calculate the average grade of all students. 
List Students Above a Certain Grade: Users can list all students who have a grade above a specified threshold.'''


print('Welcome to the Student List Manager!')

students = []
grades = []

while True:
	print("\nOptions:")
	print("1. Add a Student and Grade")
	print("2. Update a Student's Grade")
	print("3. Remove a Student")
	print("4. Calculate the Average Grade")
	print("5. List Students Above a Certain Grade")
	print("6. Exit")
	
	choice = input("Enter your choice (1-6): ")
	
	if choice == '1':
		student_name = input("Enter student name: ")
		student_grade = int(input("Enter student grade: "))
		students.append(student_name)
		grades.append(student_grade)
	
	elif choice == '2':
		student_name = input("Enter student name to update: ")
		if student_name in students:
			new_grade = int(input("Enter new grade: "))
			index = students.index(student_name)
			grades[index] = new_grade
		else:
			print("Student not found.")
	
	elif choice == '3':
		student_name = input("Enter student name to remove: ")
		if student_name in students:
			index = students.index(student_name)
			students.pop(index)
			grades.pop(index)
		else:
			print("Student not found.")
	
	elif choice == '4':
		if grades:
			average_grade = sum(grades) / len(grades)
		else:
			average_grade = 0
		print("Average Grade:", average_grade)
	
	elif choice == '5':
		threshold = int(input("Enter grade threshold: "))
		students_above_threshold = []
		for i in range(len(students)):
			if grades[i] > threshold:
				students_above_threshold.append(students[i])
		print("Students Above Threshold:", students_above_threshold)
	
	elif choice == '6':
		break
	
	else:
		print("Invalid choice. Please enter a number between 1 and 6.")
	
	print("\nCurrent Students and Grades:")
	print("Students:", students)
	print("Grades:", grades)
