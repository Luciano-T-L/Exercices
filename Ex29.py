salary = float(input("Insert the salary: "))
loan = float(input("Insert the loan value: "))

if loan > salary*0.2:
    print("Loan denied")
else:
    print("Loan allowed")