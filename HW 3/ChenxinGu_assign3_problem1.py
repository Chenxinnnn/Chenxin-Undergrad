#Chenxin Gu, Oct 4nd, Section 3, ChenxinGu_assign3_problem1.py
#First import the database.
import random

#Directly print in the introduction paragraph and breakout lines.
print("Buried Treasure!")
print("")
print("You are on a deserted island that is used by pirates")
print("to hide their treasure. The pirates are coming back")
print("soon, and you only have a short amount of time to find")
print("the treasure before they return and catch you trying")
print("to steal from them.")
print("")
print("Here's a map of the island - each '.' represents a spot")
print("where you can dig for treasure. When prompted, enter")
print("the ROW and COLUMN you wish to dig.  You have 3 chances")
print("to dig before the pirates return!")
print("")

#Use format to create the treasure map
print(f"{'NORTH':>17s}")
print(f"{'1 2 3 4 5 6 7':>21s}")
print(f"{'1 . . . . . . .':>21s}")
print(f"{'2 . . . . . . .':>21s}")
print(f"{'3 . . . . . . .':>21s}")
print("WEST  4 . . . . . . .  EAST")
print(f"{'5 . . . . . . .':>21s}")
print(f"{'6 . . . . . . .':>21s}")
print(f"{'7 . . . . . . .':>21s}")
print(f"{'SOUTH':>17s}")
print("")

#Let the computer create a random point
row = random.randint(1,7)
column = random.randint(1,7)

#Guess #1
#First let the users type in their guess and create a variable.
#Use if statement to seperate two situations.
#If the user guess both row and column correctly, end the program with a congratulation.
#Else, first print out the suggestion line, and use two if statements to seperately discuss columns and rows.
#So row and colomn do not have any impact on each other.
print("Guess #1")
row1 = int(input("Enter a ROW: "))
column1 = int(input("Enter a COLUMN: "))
print("")
if row1 == row and column1 == column:
    print("You found the treasure on Guess #1!  Congratulations!")
else:
    print("No treasure here!  Here are some hints for your next guess:")
    if row1 > row:
        print("Go NORTH")
    elif row1 < row:
        print("Go SOUTH")
    if column1 > column:
        print("Go WEST")
    elif column1 < column:
        print("Go EAST")
    print("")

    #Guess #2
    #This is same logic as Guess #1
    print("Guess #2")
    row2 = int(input("Enter a ROW: "))
    column2 = int(input("Enter a COLUMN: "))
    print("")
    if row2 == row and column2 == column:
        print("You found the treasure on Guess #2!  Nice job!")
    else:
        print("No treasure here!  Here are some hints for your next guess:")
        if row2 > row:
            print("Go NORTH")
        elif row2 < row:
            print("Go SOUTH")
        if column2 > column:
            print("Go WEST")
        elif column2 < column:
            print("Go EAST")
        print("")

        #Guess #3
        #Because we end up with at most three guesses, just print out the answer if the user does not guess correctly.
        print("Guess #3")
        row3 = int(input("Enter a ROW: "))
        column3 = int(input("Enter a COLUMN: "))
        print("")
        if row3 == row and column3 == column:
            print("You found the treasure on Guess #3!  Just in time!")
        else:
            print("No treasure here, and the pirates have returned to the island! You've been caught!")
            print("The treasure was at ROW", row, "and COLUMN", column)


                
                


