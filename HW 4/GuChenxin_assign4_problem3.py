#Chenxin Gu, Oct 12th, Section 3, ChenxinGu_assign4_problem3.py
#Let the use input a size, and validate the value.
size = int(input("Enter size for your pattern (3-9): "))
while size < 3 or size > 9:
    print("Invalid size, try again")
    size = int(input("Enter size for your pattern (3-9): "))

#Let the use input a character, and validate the input character.
char = input("Enter a single character for your pattern: ")
while len(char) != 1:
    print("Invalid character, try again")
    char = input("Enter a single character for your pattern: ")

#Use while loop and cumulative variable to create the pattern.
#This is a simple pattern with all lines the same.
print("")
print("Pattern #1")
print("")
count1 = 0
while count1 < size:
    print(size * char)
    count1 += 1

#Seperate the first and last line. They are both size * char.
#The other middle lines are of char plus space.
print("")
print("Pattern #2")
print("")
print(size * char)
count2 = 0
while count2 < (size - 2):
    print(char + (size - 2) * " " + char)
    count2 += 1
print(size * char)

#This is a pattern that treats even lines and odd lines differently.
#So in while loop, we add a if statement to separate the two kinds of patterns.
print("")
print("Pattern #3")
print("")
count3 = 0
while count3 < size:
    if count3 % 2 == 0:
        print(char * size)
    else:
        print(" " * size + char * size)
    count3 += 1

#This is a pattern filled with line numbers. So we make use of cumulative variables.
print("")
print("Pattern #4")
print("")
count4 = 0
while count4 < size:
    print(char + str(count4) * size + char)
    count4 += 1

#This pattern also differs with respect to line number.
#So we again use cumulative variable.
print("")
print("Pattern #5")
print("")
count5 = 0
while count5 < size:
    print(" " * (size - 1 - count5) + char * size)
    count5 += 1




