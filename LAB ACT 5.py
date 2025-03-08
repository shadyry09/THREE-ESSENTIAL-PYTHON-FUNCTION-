#LAB ACT 5
def classify_age():
    age = int(input("Enter an age: "))

    if age < 0:
        print("Invalid age! Age cannot be negative.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

classify_age()

#PEÑAFIEL, R-JAY E. 12-CPE-01
#STILL LEARNING ABOUT PYTHON