#Chenxin Gu, Yuxuan Du, Sep 17, Section 003, ChenxinGu_assign1_problem1.py

#List the steps of finishing the breakfast
#Use the variable to define all instruments and ingredients we need to use for making the breakfast
item1 = "first bread"
item2 = "another bread"
item3 = "hams"
item4 = "plate"
item5 = "toaster"
item6 = "milk"
item7 = "cup"
#Use the variable to define the numer of items we need to use
num_of_bread = 2
num_of_ham = 2
num_of_plate = 1
num_of_cup = 1
#Use the vaiable to define the time
time= 30

#Now we begin to make breakfast
#First, take out all ingredients that we need 
print("Take out",num_of_bread, " bread ,", num_of_ham, item3, "and a bottle of",item6,"from refrigerator")
print("Put bread and", item3, "on the", item5)
#Also, we need to take out all instruments that we would use
print("Take out", num_of_plate, item4,"and", num_of_cup, item7, "from cupboard")
print("Put", item4, "and", item7, "on the table")
#We should set the time and then use the toaster to help us to toast bread
print("Set the time that the toaster would work as:", time, end="s")
#Since we use the end argument on the below line, here we use " " to break it with another line
print(" ")
print('Push the "start" button on the', item5)
print("Pick up the", item1, "from the",item5, "when time runs out, and put it on the", item4)
print("Pick up the", item3, "and put them on the", item1)
print("Pick up", item2, "and put it on the top of the", item1, "with", item3)
#We can pour a bootle of milk to take with the sandwich
print("Pick up", item6, "and pour it into the", item7, "until it is full")
print("Put the sandwich and milk together on the table, then our breakfast is finished")


