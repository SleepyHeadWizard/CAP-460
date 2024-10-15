'''You are working on a banking application that logs transactions. Each transaction is represented as a tuple containing the transaction ID, type ("deposit" or "withdraw"), and the amount. 
 
Task: Write a function that takes a list of transactions as input and returns the total deposit amount and total withdrawal amount separately.'''

trans=[(1, 'deposit', 100), (2, 'withdraw', 50), (3, 'deposit', 150), (4, 'withdraw', 20), (5, 'deposit', 200)]

sum_deposit=0
sum_withdraw=0

for i in trans:
    if i[1]=='deposit':
        sum_deposit+=i[2]
    else:
        sum_withdraw+=i[2]
        
print('Total deposit amount:',sum_deposit)
print('Total withdraw amount:',sum_withdraw)