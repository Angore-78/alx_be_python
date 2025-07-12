Monthly_income = int(input("Enter your monthly income:"))
Monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = Monthly_income - Monthly_expenses
#Assuming the annual interest rate is 5%
Projected_savings = monthly_savings * 12 +(monthly_savings * 12 * 0.05)
print(f"Your monthly savings are {monthly_savings}")
print(f"Your Projected savings after one year, with interest, is: {Projected_savings}")