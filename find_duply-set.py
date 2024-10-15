'''Scenario: You are developing a system to manage user registrations on a website. Sometimes, users register multiple times with the same email. 
Given a list of email addresses, use a set to filter out duplicate emails. 
Write a function to check if a specific email already exists in the system. 
Display the unique set of registered email addresses. 
Bonus: Count the number of duplicates removed.'''

email=['abcd@yahoo.com','xyz@gmail.com','abc@yahoo.com','hello@gmail.com','abc@yahoo.com']

filtered_email=set(email)

print('Unique email addresses:',filtered_email)

print('Number of duplicates removed:',len(email)-len(filtered_email))

while True:
    check_email=input('\nEnter email to check:')
    if check_email in filtered_email:
        print('Email already exists.')
    else:
        print('Email does not exist.')
        break
    
