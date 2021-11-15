num = int(input("Insert a integer and positive number: "))

sum = 0

if num > 0:
    while num != 0:
        resto = num % 10
        sum += resto
        num = (num // 10)
    
    print(sum)

else:
    print("Invalid number")