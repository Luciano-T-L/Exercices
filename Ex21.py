value_per_hour = float(input("How much will be paid for the hour worked? "))
hours_worked = int(input("How many hours were worked? "))
additional = value_per_hour * hours_worked * 0.1
total_paid = (value_per_hour * hours_worked) + additional

print(f"The worker will recive: {total_paid} dollars")
