#LAB ACT 3
def check_number():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
    master = input("Do you want to check another number? (yes/no): ")
    if master == 'yes' or master == 'y':
        check_number()
    else:
        print("Number checking skipped.")
    
check_number()

#PEÑAFIEL, R-JAY E. 12-CPE-01
#STILL LEARNING ABOUT PYTHON