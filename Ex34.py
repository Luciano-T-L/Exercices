print("Chose a operation:")
print("sum (1)")
print("substraction (2)")
print("multiplication (3)")
print("division (4)")

operation = input(">")
first = float(input("Insert the first number: "))
second = float(input("insert the second number: "))

if operation == "1":
    print(f"The sum is: {first + second}")
elif operation == "2":
    print(f"The substraction is: {first - second}")
elif operation == "3":
    print(f"The multiplication is: {first * second}")
elif operation == "4":
    print(f"The division is: {first / second}")
else:
    print("Something went wrong")
