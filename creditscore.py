credit_score = float(input("Enter credit score: "))
annual_income = float(input("Enter annual income: "))
debt_to_income_ratio = float(input("Enter debt-to-income ratio: "))
if credit_score >= 650 and annual_income >= 30000 and debt_to_income_ratio < 0.4:
    print("Loan Approved")
else:
    print("Loan Denied")