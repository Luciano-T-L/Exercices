score1 = float(input("Insert the first test grade: "))
score2 = float(input("Insert the second teste grade: "))
score3 = float(input("Insert the third teste grade: "))

final_score = (score1 + score2 + score3*2)/4

if 0 <= score1 <= 10 and 0 <= score2 <= 10 and 0 <= score3 <= 10:    
    if final_score >= 6.0:
        print(f"Final score = {final_score}. You pass!")
    else:
        print(f"Final score = {final_score}. You fail!")
else:
    print("Invalid score")