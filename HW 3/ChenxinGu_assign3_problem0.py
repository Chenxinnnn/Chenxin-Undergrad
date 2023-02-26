#Chenxin Gu, Oct 4nd, Section 3, ChenxinGu_assign3_problem0.py
width_1 = float(input("Enter the width for Rectangle #1: "))
length_1 = float(input("Enter the length for Rectangle #1: "))
width_2 = float(input("Enter the width for Rectangle #2 :"))
length_2 = float(input("Enter the length for Rectangle #2: "))

#Do the calculation
print("")
area_1 = width_1*length_1
area_2 = width_2*length_2

print("Rectangle #1 has an area of", area_1)
print("Rectangle #1 has an area of", area_2)

#If width equal to length, then it is a square
if width_1 == length_1:
   print("Rectangle #1 is a square!")
if width_2 == length_2:
   print("Rectangle #2 is a square!")
print("") 
  
#Do comparison
if area_1 > area_2:
    print("Rectangle #1 is larger than Rectangle #2")
elif area_1 < area_2:
    print("Rectangle #2 is larger than Rectangle #1")
else:
    print("Rectangle #1 and Rectangle #2 are the same size")
