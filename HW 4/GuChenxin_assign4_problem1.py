#Chenxin Gu, Oct 12th, Section 3, ChenxinGu_assign4_problem1.py
print("Jelly Bean Jar Simulator")
print("")

#let the user input an validate his answer.
while True:
    beantype = str.upper(input("Pick a color! (R)ed, (O)range, (Y)ellow, (G)reen, (B)lue, (I) or (V)iolet: "))
    if len(beantype) != 1:
        print("Invalid select, try again")
    elif beantype in "ROYGBIV":
        break
    else:
        print("Invalid select, try again")

import random
word = "ROYGBIV"
count = 0
count_double = 0
count_neighbor = 0
count_firstlast = 0
print("Thanks, here we go!")

#Let the computer generate two random selection.
while True:
    Choice1 = random.choice(word)
    Choice2 = random.choice(word)
    count += 1

    #When computer guess correctly what the user inputs, break the loop.
    if Choice1 == Choice2 == beantype:
        print(f"{count}. {Choice1} and {Choice2} doubles! your bean came out twice!")
        count_double += 1
        break

    #When double occurs, tell the users the computer got doubles.
    elif Choice1 == Choice2:
        print(f"{count}. {Choice1} and {Choice2} doubles!")
        count_double += 1

    #When neighbor occurs, tell the users the computer got neighbor.    
    elif Choice1 == "R" and Choice2 == "O":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice1 == "O" and Choice2 == "Y":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice1 == "Y" and Choice2 == "G":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice1 == "G" and Choice2 == "B":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice1 == "B" and Choice2 == "I":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice1 == "I" and Choice2 == "V":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice2 == "R" and Choice1 == "O":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice2 == "O" and Choice1 == "Y":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice2 == "Y" and Choice1 == "G":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice2 == "G" and Choice1 == "B":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice2 == "B" and Choice1 == "I":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1
    elif Choice2 == "I" and Choice1 == "V":
        print(f"{count}. {Choice1} and {Choice2} neighbors!")
        count_neighbor += 1

    #When first&last occurs, tell the users the computer got first&last.
    elif Choice1 == "R" and Choice2 == "V":
        print(f"{count}. {Choice1} and {Choice2} first & last!")
        count_firstlast += 1
    elif Choice1 == "V" and Choice2 == "R":
        print(f"{count}. {Choice1} and {Choice2} first & last!")
        count_firstlast += 1
        
    #If none of these occurs
    else:
        print(f"{count}. {Choice1} and {Choice2}")

#Conclude the outputs
double_percentage = count_double / count * 100
neighbor_percentage = count_neighbor / count * 100
firstlast_percentage = count_firstlast / count * 100

#Print out the results
print("")
print("------")
print("Total picks:", count)
print(f"Doubles: {count_double} ({double_percentage:.2f}%)")
print(f"Neighbors: {count_neighbor} ({neighbor_percentage:.2f}%)")
print(f"First/Last: {count_firstlast} ({firstlast_percentage:.2f}%)")




    


                         

