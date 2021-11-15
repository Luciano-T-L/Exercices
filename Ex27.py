num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))

if num1 > num2:
    print(f"{num1} is bigger than {num2}")
    print(f"The difference between the two numbers is: {num1 - num2} ")
elif num1 == num2:
    print(f"The two numbers are the same. There is no difference between them.")
else:
    print(f"{num2} is bigger than {num1}")
    print(f"The difference between the two numbers is: {num2 - num1} ")
