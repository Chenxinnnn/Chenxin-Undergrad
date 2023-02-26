#Let the user input the number of students in class and validate the input.
Num_students = int(input("How many students are in your class? "))
while True:
    if 1 <= Num_students <= 100:
        break
    print("Invalid # of students, try again.")
    Num_students = int(input("How many students are in your class? "))

#Let the unser input number of tests in class and validate the input.    
print("")
Num_test = int(input("How many tests in this class? "))
while True:
    if 1 <= Num_test <= 100:
        break
    print("Invalid # of tests, try again.")
    Num_test = int(input("How many tests in this class? "))

print("")
print("Thanks, here we go!")
print("")

#set up a cumulative varialbe to count the total distribution of scores of the class.
Class_total = 0
A_count = 0
B_count = 0
C_count = 0
D_count = 0
F_count = 0
#For each student, we need the same operation. So we set up a for loop for students.
for Num_students in range(1, Num_students + 1):
    print(f"**** Student #{Num_students} ****")
    total = 0
    #For each test, we need to ask the user for their score.
    for Num_test in range(1, Num_test + 1):
        score = float(input(f"Enter score for test #{Num_test}: "))
        while True:
            if 0 <= score <= 100:
                break
            print("Invalid score, try again")
            score = float(input(f"Enter score for test #{Num_test}: "))
        total += score
    average = total / Num_test

    #Calculate the grade for the students.
    Class_total += average
    if 90 <= average <= 100:
        Grade = "A"
        A_count += 1
    elif 80 <= average < 90:
        Grade = "B"
        B_count += 1
    elif 70 <= average < 80:
        Grade = "C"
        C_count += 1
    elif 63 <= average < 70:
        Grade = "D"
        D_count += 1
    elif 0 <= average < 63:
        Grade = "F"
        F_count += 1
    print(f"Average score for student #{Num_students} is {average:.2f} ({Grade})")
    print("")

#Now calculate the class average.    
print("-----Report-----")
Class_average = Class_total / Num_students
if 90 <= Class_average <= 100:
    Class_Grade = "A"
elif 80 <= Class_average < 90:
    Class_Grade = "B"
elif 70 <= Class_average < 80:
    Class_Grade = "C"
elif 63 <= Class_average < 70:
    Class_Grade = "D"
elif 0 <= Class_average < 63:
    Class_Grade = "F"

#Print out the result.      
print(f"Average class score: {Class_average:.2f} ({Class_Grade})")
print(f"# of students who earned an 'A' average: {A_count}")
print(f"# of students who earned an 'B' average: {B_count}")
print(f"# of students who earned an 'C' average: {C_count}")
print(f"# of students who earned an 'D' average: {D_count}")
print(f"# of students who earned an 'F' average: {F_count}")
        
