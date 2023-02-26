#Chenxin Gu, Oct 4nd, Section 3, ChenxinGu_assign3_problem3.py
#Start the program with the first question.
print("Which Toy Story Character Are You?")
print("")
print("Are you a natural leader?")
print("(a) Yes")
print("(b) No")
leader_answer = input("Your answer: ")
print("")

#Use if statement to give out the next question depending on user's answer.
if leader_answer == "a" or leader_answer == "A":
    print("Have you been known to get jealous?")
    print("(a) Yes")
    print("(b) No")
    jealous_answer = input("Your answer: ")
    print("")
    
    if jealous_answer == "a" or jealous_answer == "A":
        print("Do you admit your mistakes?")
        print("(a) Yes")
        print("(b) No")
        mistake_answer = input("Your answer: ")
        print("")

        if mistake_answer == "a" or mistake_answer == "A":
            print("Are you a fashionista?")
            print("(a) Yes")
            print("(b) No")
            fashionista_answer = input("Your answer: ")
            print("")

            if fashionista_answer == "a" or fashionista_answer == "A":
                print("You are KEN.")
            elif fashionista_answer == "b" or fashionista_answer == "B":
                print("You are WOODY.")
            else:
                print("Invalid answer, quitting program.")

        elif mistake_answer == "b" or mistake_answer == "B":
            print("Are you obsessed with hygiene?")
            print("(a) Yes")
            print("(b) No")
            hygiene_answer = input("Your answer: ")
            print("")

            if hygiene_answer == "a" or hygiene_answer == "A":
                print("You are STINKY PETE.")
            elif hygiene_answer == "b" or hygiene_answer == "b":
                print("you are LOTSO.")
            else:
                print("Invalid answer, quitting program.")

        else:
            print("Invalid answer, quitting program.")
            
    elif jealous_answer == "b" or jealous_answer == "B":
        print("Can you fly?")
        print("(a) Yes")
        print("(b) No")
        fly_answer = input("Your answer: ")
        print("")

        if fly_answer == "a" or fly_answer == "A":
            print("You are SARGE.")
        elif fly_answer == "b" or fly_answer == "B":
            print("You are BUZZ LIGHTYEAR.")
        else:
            print("Invalid answer, quitting program.")
            
    else:
        print("Invalid answer, quitting program.")
    

elif leader_answer == "b" or leader_answer == "B":
    print("Is your IQ above or below average?")
    print("(a) Above")
    print("(b) What's IQ?")
    IQ_answer = input("Your answer: ")
    print("")

    if IQ_answer == "a" or IQ_answer == "A":
        print("Do you like to stretch yourself?")
        print("(a) Yes")
        print("(b) No")
        strectch_answer = input("Your answer: ")
        print("")

        if strectch_answer == "a" or strectch_answer == "A":
            print("You are SLINKY.")

        elif strectch_answer == "b" or strectch_answer == "B":
            print("Are you outdoorsy?")
            print("(a) Yes")
            print("(b) No")
            outdoorsy_answer = input("Your answer: ")
            print("")

            if outdoorsy_answer == "a" or outdoorsy_answer == "A":
                print("You are JESSIE.")

            elif outdoorsy_answer == "b" or outdoorsy_answer == "B":
                print("Bacon or hashbrowns?")
                print("(a) Bacon")
                print("(b) Hashbrowns")
                food_answer = input("Your answer: ")
                print("")

                if food_answer == "a" or food_answer == "A":
                    print("You are MRS. POTATO HEAD.")
                elif food_answer == "b" or food_answer == "B":
                    print("You are HAMM.")
                else:
                    print("Invalid answer, quitting program.")

            else:
                print("Invalid answer, quitting program.")

        else:
            print("Invalid answer, quitting program.")
            
    elif IQ_answer == "b" or IQ_answer == "B":
        print("Do you at least use your head?")
        print("(a) Yes")
        print("(b) No")
        head_answer = input("Your answer: ")
        print("")

        if head_answer == "a" or head_answer == "A":
            print("You are REX.")
        elif head_answer == "b" or head_answer == "B":
            print("You are one of the GREEN ALIENS.")
        else:
            print("Invalid answer, quitting program.")
        
    else:
        print("Invalid answer, quitting program.")

else:
    print("Invalid answer, quitting program.")
#If the user inputs invalid answers, tell them it is invalid.
    
