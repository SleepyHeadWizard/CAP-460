balance = int(input("Enter the balance amount: "))
if 5000 <= balance <= 10000:
    interest_rate = 0.10  
    
elif 4000 <= balance < 5000:
    interest_rate = 0.08  
    
elif 3000 <= balance < 4000:
    interest_rate = 0.07 
    
elif 2000 <= balance < 3000:
    interest_rate = 0.05  
else:
    interest_rate = 0.00  
interest_amount = balance * interest_rate
total_balance = balance + interest_amount
result = {
    "Original Balance": balance,
    "Interest Rate": interest_rate * 100,  
    "Interest Amount": interest_amount,
    "Total Balance": total_balance
}
print(result)