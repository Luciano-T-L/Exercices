money_per_day = 30
days_worked = int(input("How many days did the plumer work? "))
taxes = 0.08
payment = money_per_day * days_worked
payment_less_taxes = payment - (payment * taxes)

print(f"The plumer will recive {payment_less_taxes} ")
