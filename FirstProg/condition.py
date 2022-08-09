your_marks =int( input("what is your marks in programming: "))

def show_grade(grade):
    print(f"you got:{grade} ")

if your_marks>=80:
    show_grade("you got A+")
elif your_marks<80 and your_marks>70:
    show_grade("you got A ")
elif your_marks<70 and your_marks>60:
    show_grade("you got A- ")

print("Finished")