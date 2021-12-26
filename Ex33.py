lab = float(input("Insert the laboratory grade: "))

if lab > 10 or lab < 0:
    print("Invalid grade, try again")
    quit()

semester = float(input("Insert the semester grade: "))

if semester > 10 or semester < 0:
    print("Invalid grade, try again")
    quit()

final = float(input("Insert the final test grade: "))

if final > 10 or final < 0:
    print("Invalid grade, try again")
    quit()

final_grade = (lab * 2 + semester * 3 + final * 5) / 10

if 0 <= final_grade <= 2.9:
    print(f"The student failed. Final grade: {final_grade}")
elif 3 <= final_grade <= 4.9:
    print(f"The student can retake a test. Final grade: {final_grade}")
else:
    print(f"The student was approved. Final grade: {final_grade}")
