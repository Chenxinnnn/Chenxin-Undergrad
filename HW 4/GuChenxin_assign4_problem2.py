#Chenxin Gu, Oct 12th, Section 3, ChenxinGu_assign4_problem2.py
#Let the users input a positive integer, and validate the value.
integer_input = input("Enter a positive integer: ")
integer = int(integer_input)
while integer <= 0:
    print("Number must be positive, try again.")
    integer_input = input("Enter a positive integer: ")
    integer = int(integer_input)

#Let the users choose to show silent mode or not, and validate their answer.
while True:
    silent = str.lower(input("Silent mode? (yes/no): "))
    if silent == "yes" or silent == "no":        
        break
    print("Invalid option, try again.")
    
#First do the silent mode part, start with calculations.
#While calculation, record the highest value we have got.
if silent == "yes":
    period = 1
    highest = integer
    while True:
        if integer == 1:
            if integer > highest:
                highest = integer
            break

        elif integer % 2 == 0:
            integer /= 2
            if integer > highest:
                highest = integer
            period += 1
        
        elif integer % 2 != 0:
            integer *= 3
            integer += 1
            if integer > highest:
                highest = integer
            period += 1
    #Print out the results.
    print("")
    print("--------")
    print(f"Period for {int(integer_input):,}: {period:,}")
    print(f"Highest number reached: {int(highest):,}")

#Now do the part without silent mode.
#I don't know how to do the formating, so I just print out the result step by step.
elif silent == "no":
    period = 1
    highest = integer
    while True:
        if integer == 1:
            if integer > highest:
                highest = integer
            print(f"{period}. {int(integer)} -- stopping!")
            break

        elif integer % 2 == 0:
            integer /= 2
            if integer > highest:
                highest = integer
            print(f"{period}. {int(integer) * 2} -- even! {int(integer) * 2}/2 = {int(integer)}")
            period += 1
        
        elif integer % 2 != 0:
            integer *= 3
            integer += 1
            if integer > highest:
                highest = integer
            print(f"{period}. {int((integer - 1) / 3)} -- odd! {int((integer - 1) / 3)} * 3 + 1 = {int(integer)}")
            period += 1
            
    #Include a conclusion at the end.
    print("")
    print("--------")
    print(f"Period for {int(integer_input):,}: {period:,}")
    print(f"Highest number reached: {int(highest):,}")
        
