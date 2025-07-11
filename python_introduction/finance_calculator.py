income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

projected_savings = (income - expenses) * 12 + ((income - expenses) * 12 * 0.05)

print(f"Your monthly savings are ${income - expenses}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
