'''Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

account_balance = 0
while True:
    print('Enter transaction in the format: D/W amount')
    transaction = input('Enter transaction:')
    if not transaction:
        break
    transaction_type, amount = transaction.split(' ')
    if transaction_type == 'D':
        account_balance += int(amount)
        print('Net amount:',account_balance)
    elif transaction_type == 'W':
        account_balance -= int(amount)
        print('Net amount:',account_balance)
    else:
        print('Invalid transaction type. Try again.')

