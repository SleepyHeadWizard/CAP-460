'''Scenario 1: Email Formatter
You have a file called emails.txt where each line contains a name and an email address separated by a comma (e.g., Alice,alice@example.com).

Write a function to format each line into a friendly greeting message (e.g., "Hello, Alice! Your email is alice@example.com.") and save it to a file called formatted_emails.txt.
Implement a function to extract all unique email domains (e.g., example.com) from the file and write them to email_domains.txt.
Bonus: Write a function that counts how many email addresses belong to each domain and save the counts in a file called domain_counts.txt.'''

f=open('emails.txt','r')
