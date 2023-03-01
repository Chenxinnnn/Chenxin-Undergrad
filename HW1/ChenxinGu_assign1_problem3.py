#ChenxinGu, YuxuanDu, Sep 17th, Section 003, ChenxinGu_assign1_problem3.py
#Create a input for users to enter their names, and save each as a variable.
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

#Create a line break
print("")
#Print the string deirectly using the print function.
print("Here are your names in every possible order:")
print("--------------------------------------------")

#Create a line break
print("")
#Because there's no space between name and the comma, we use the eng argument
print("1.", name1, end=", ")
print(name2, end=", ")
print(name3)

#Create a line break
print("")
#Because all names are separated by "**", we use the end argument to add "**" before the first name, and we use the separate argument to create "**" between names
print("2. *", end="*")
print(name1, name3, name2, sep="** **", end="**")
#Create a line break
print("")
print("")
#Because there's no slash between 3. and name two, we use end function to print 3. seperately with names.
print("3", end=". ")
#Use sep argument to use "-" to seperate names.
print(name2, name1, name3, sep="-")

#Create a line break
print("")
print("4.", name2)
print(name3)
print(name1)

#Create a line break
print("")
print("5.", name3)
#Because we want to make a space no matter how long the name is, we use format to control the position of the space. 
#And there's a ! at the end of the name without a space, so we use the end argument again.
print(format('', '<2s'), name2, end="!")
#Start a new line.
print("")
#Again use format function to control the position of the space " ", and let the names line up.
print(format('', '<2s'), name1)

#Create a line break
print("")
#Use end function to delete the space between slash and name 3.
print("6. --", end="-")
print(name3)
#Use format function to control the position of the slashes. Because there are 5 slashes despite the one in end argument, and there are 3 spaces at the top left, so in total is >8.
print(format('-----', '>8s'),end="-")
print(name1)
#Similar the the line above, there are 11 bits at the top left despite the end "-".
print(format('--------', '>11s'),end="-")
print(name2)

