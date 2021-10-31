base_salary = float(input("insert the base salary: "))
bonus = base_salary * 0.05
taxes = base_salary * 0.07
total = base_salary + bonus - taxes

print(f"The worker will receive {total} dollars")
