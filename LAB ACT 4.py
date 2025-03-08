#LAB ACT 4
def assign_grade():
    score = int(input("Enter the student's score: "))

    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
    
    huntme = input("Do you want to check another score? (yes/no): ")
    if huntme == 'yes' or huntme == 'y':
        assign_grade()
    else:
        print("Grade checking skipped.")

assign_grade()

#PEÑAFIEL, R-JAY E. 12-CPE-01
#STILL LEARNING ABOUT PYTHON