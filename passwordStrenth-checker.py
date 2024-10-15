'''Password Strength Checker 
Scenario: Build a password strength checker that ensures a password contains a mix of characters. 
Use a set to keep track of character categories present in the password (e.g., lowercase, uppercase, digits, special characters). 
Check if the password contains at least one character from each required category. 
Display a message indicating whether the password is strong or weak. 
Bonus: Suggest missing character categories to improve password strength.'''


lowercase=set('abcdefghijklmnopqrstuvwxyz')
uppercase=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits=set('0123456789')
special=set('!@#$%^&*()_+')

while True:
    password=input('\nEnter password:')
    password_set=set(password)
    
    if len(password_set.intersection(lowercase))>0 and len(password_set.intersection(uppercase))>0 and len(password_set.intersection(digits))>0 and len(password_set.intersection(special))>0:
        print('Strong password.')
    else:
        print('Weak password.')
        missing=lowercase.union(uppercase).union(digits).union(special)-password_set
        print('Missing character categories:',missing)
    