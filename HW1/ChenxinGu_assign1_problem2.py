#Chenxin Gu, Yuxuan Du, Sep 17th, Section 003, ChenxinGu_assign1_problem2.py
#First define all the variables that we need to use in the program.
test_score_1 = 97
test_score_2 = 82
test_score_3 = 85

student_first_name = "Grace"
student_last_name = "Hopper"

bonus_points = 2

class_name = "'Introduction to Computer Programming' (no prior experience)"

#print the line of stars.
print("************************************************************")
#Because we have already defined the variable class_name, we can directly print it using the print function.
print(class_name)
#print the line of stars again.
print("************************************************************")
#print a line break.
print("")
#print student's name. Because there's no space between "Hopper" and the comma, we use the end argument to create the comma here.
print("Student:", student_last_name, end=", ")
print(student_first_name)
#print the test scores. We use the end argument again here.
print("Most recent test scores:",test_score_1, end=", ")
print(test_score_2,"and",test_score_3)
#calcuate the average score. Because the original answers came out to be a integer, and we need it to be a float, we use the float function to convert integer to float.
print("Average score:",float((test_score_1+test_score_2+test_score_3)/3))
#print the bonus point.
print("Class bonus points:", bonus_points)
#print the average score with bonus points added, and use the float function to make it a float.
print("Average score with bonus points added:", float((test_score_1+test_score_2+test_score_3)/3 +bonus_points))
