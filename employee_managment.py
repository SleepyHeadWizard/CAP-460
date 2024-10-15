'''You are designing an employee management system where you need to store employees’ names, IDs, department, and salary in tuples. You need to:

Display the list of all employees.
Sort employees based on their salary.
Update an employee’s department.
Find the average salary of employees in a specific department.'''

empolyee_list=[('John',1,'HR',50000),('Jane',2,'IT',60000),('Alice',3,'HR',70000),('Bob',4,'IT',80000)]

choice=0
while choice!=5:
    print('1. Display all employees')
    print('2. Sort employees by salary')
    print('3. Update employee department')
    print('4. Find average salary of employees in a department')
    print('5. Exit')
    choice=int(input('Enter your choice:'))
    
    if choice==1:
        for i in empolyee_list:
            print(i)
    elif choice==2:
        sorted_empolyee = []
        for i in range(len(empolyee_list)):
            for j in range(len(empolyee_list)):
                if empolyee_list[i][1] < empolyee_list[j][1]:
                    empolyee_list[i], empolyee_list[j] = empolyee_list[j], empolyee_list[i]
        sorted_products = empolyee_list
        print(sorted_products)
    elif choice==3:
        id=int(input('Enter employee ID:'))
        for i in empolyee_list:
            if i[1]==id:
                i[2]=input('Enter new department:')
    elif choice==4:
        department=input('Enter department:')
        total=0
        count=0
        for i in empolyee_list:
            if i[2]==department:
                total+=i[3]
                count+=1
        if count>0:
            print('Average salary:',total/count)
        else:
            print('No employees in this department.')
    elif choice==5:
        print('Exiting...')
    else:
        print('Invalid choice. Please try again.')