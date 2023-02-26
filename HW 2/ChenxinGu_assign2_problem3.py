#ChenxinGu_Sep25_Section003_ChenxinGu_assign2_problem3.py

#Start the program with printing the title and a line break
print("Minecraft block distance calculator")
print("")

#Let unsers input their position, then define the viaralbes.
#Change the variables into integers at the same time for later calculation.
#Create a line break after this part.
Player1_x = int(input("Enter player 1's x position: "))
Player1_y = int(input("Enter player 1's y position: "))
Player1_z = int(input("Enter player 1's z position: "))
Player2_x = int(input("Enter player 2's x position: "))
Player2_y = int(input("Enter player 2's y position: "))
Player2_z = int(input("Enter player 2's z position: "))
Player3_x = int(input("Enter player 3's x position: "))
Player3_y = int(input("Enter player 3's y position: "))
Player3_z = int(input("Enter player 3's z position: "))
print("")

#Do the calculation for distance between Player1 and Player2.
#First calculate x, y, z distance between Player1 and Player2.
#Then calculate the straightline distance between Player1 and Player2.
Player_12_x = abs(Player1_x - Player2_x)
Player_12_y = abs(Player1_y - Player2_y)
Player_12_z = abs(Player1_z - Player2_z)

Player_12 = (Player_12_x**2 + Player_12_y**2 + Player_12_z**2) **0.5

#Do the calculation for distance between Player2 and Player3.
#First calculate x, y, z distance between Player2 and Player3.
#Then calculate the straightline distance between Player2 and Player3.
Player_23_x = abs(Player2_x - Player3_x)
Player_23_y = abs(Player2_y - Player3_y)
Player_23_z = abs(Player2_z - Player3_z)

Player_23 = (Player_23_x**2 + Player_23_y**2 + Player_23_z**2) **0.5

#Do the calculation for distance between Player1 and Player3.
#First calculate x, y, z distance between Player1 and Player3.
#Then calculate the straightline distance between Player1 and Player3.
Player_13_x = abs(Player1_x - Player3_x)
Player_13_y = abs(Player1_y - Player3_y)
Player_13_z = abs(Player1_z - Player3_z)

Player_13 = (Player_13_x**2 + Player_13_y**2 + Player_13_z**2) **0.5

#Print out our calculation result in a form by using format function.
#Since we are not sure how many digits does the variables have, use "<" to let the variables stick to the left side and control spaces.
#Also, we want out calculated distance show up to have two dicimal places with commas, we also include this in the format function.
print(format("Players","<9"), format("X Distance","<14"), format("Y Distance","<14"), format("Z Distance","<14"), "Straight Line Distance")
print(format("1 & 2","<9"), format(Player_12_x,"<14,"), format(Player_12_y,"<14,"), format(Player_12_z,"<14,"), format(Player_12,",.2f"))
print(format("1 & 3","<9"), format(Player_13_x,"<14,"), format(Player_13_y,"<14,"), format(Player_13_z,"<14,"), format(Player_13,",.2f"))
print(format("2 & 3","<9"), format(Player_23_x,"<14,"), format(Player_23_y,"<14,"), format(Player_23_z,"<14,"), format(Player_23,",.2f"))
                                                                              
