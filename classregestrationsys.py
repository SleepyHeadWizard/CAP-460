'''Class Registration System You are managing class registrations for a university. There are two sets: one containing the names of students registered for "Math 101" and another for "Physics 101". You need to:
• Find students who are registered for both courses.
• Find students who are registered only for Math 101.
• Add a new student to both courses.
• Remove a student from Physics 101


Input

math_students = {"Mrigendra", "Biren", "Amit"}
physics_students = {"Biren", "Guddu", "Arjun"}
new_student = "Sonu"
student_to_remove = "Guddu"'''

math101 = {"Mrigendra", "Biren", "Amit"}
physics101 = {"Biren", "Guddu", "Arjun"}
new_student = "Sonu"
student_to_remove = "Guddu"

choice=0

while choice!=5:
    print('\n1. Find students who are registered for both courses.')
    print('2. Find students who are registered only for Math 101.')
    print('3. Add a new student to both courses.')
    print('4. Remove a student from Physics 101.')
    print('5. Exit')
    choice=int(input('Enter choice:'))

    if choice==1:
        print('Students registered for both courses:',math101.intersection(physics101))
    elif choice==2:
        print('Students registered only for Math 101:',math101-physics101)
    elif choice==3:
        math101.add(new_student)
        physics101.add(new_student)
        print('New student added to both courses.')
    elif choice==4:
        if student_to_remove in physics101:
            physics101.remove(student_to_remove)
            print('Student removed from Physics 101.')
        else:
            print('Student not found in Physics 101.')
    elif choice==5:
        break
    else:
        print('Invalid choice. Try again.')