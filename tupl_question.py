'''You have tuples representing employee details in the form (employee_id, name, department, salary). Write a Python program that:

Retrieves and prints the employee with the highest salary using tuple functions.
Counts how many employees are in the "Sales" department.
Converts the tuple of employee details to a list, updates an employee's department, and converts it back to a tuple.'''

# employee= [(1, 'John', 'Sales', 50000), (2, 'Jane', 'Marketing', 60000), (3, 'Mike', 'Sales', 70000), (4, 'Sara', 'Marketing', 80000)]
employee = (1, 'John', 'Sales', 50000), (2, 'Jane', 'Marketing', 60000), (3, 'Mike', 'Sales', 70000), (4, 'Sara', 'Marketing', 80000)

ex=max(employee)
print('Employee with highest salary: ',ex)
    
count = 0
for i in employee:
    if i[2] == 'Sales':
        count += 1
print('Number of employee in Sales department: ',count)

employee_list = list(employee)
employee_list[1] = (2, 'Jane', 'Sales', 60000)
employee = tuple(employee_list)
print(employee)

