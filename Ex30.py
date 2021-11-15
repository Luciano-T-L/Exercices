height = float(input("Insert the height: "))
gender = input("Insert the gender (M or F): ")

if gender == "M":
    print(f"Your ideal height is: {(72.7 * height) - 58}")
elif gender == "F":
    print(f"Your ideal height is {(62.1 * height) - 58}")
else:
    print("Invalid gender, try M for male or F for female.")