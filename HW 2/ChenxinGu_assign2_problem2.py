#ChenxinGu_Sep25_Section003_ChenxinGu_assign2_problem2.py

#Start the program by letting the user to enter an integer
#Change the date type into integer and then create a line break.
num = int(input("Enter a 3 digit number between 000 and 999: "))
print("")

#Use division to seperate the three digits in the input integer.
#The 1 position number could be intepreted as the the integer mod 10.
#Divide the number by ten and take the integer part (e.g. 123 / 10 = 12.3, take 12)
#And we can get the 10 position number by using this number mod 10 again.
#The 100 position number could be easily gained by diving the original number by 100 and take the integer part.
digit_1 = num % 10
digit_divided_by_10 = int(num / 10)
digit_10 = digit_divided_by_10 % 10
digit_100 = int(num / 100)

#Print out the calculated results using the format in the quote. 
print(f"Digit in the 1's place: {digit_1:>3}")
print(f"Digit in the 10's place: {digit_10:>2}")
print(f"Digit in the 100's place: {digit_100:>1}")

#Putting the digits together is a string addition, so we change the data type into string.
#Do the addition seperately and define the calculated results.
str_dig_1 = str(digit_1)
str_dig_10 = str(digit_10)
str_dig_100 = str(digit_100)
combination_1 = str(digit_100) + str(digit_10) + str(digit_1)
combination_2 = str(digit_100) + str(digit_1) + str(digit_10)
combination_3 = str(digit_10) + str(digit_100) + str(digit_1)
combination_4 = str(digit_10) + str(digit_1) + str(digit_100)
combination_5 = str(digit_1) + str(digit_10) + str(digit_100)
combination_6 = str(digit_1) + str(digit_100) + str(digit_10)

#In order to do multiplication, we change the calculated result back to integer.
Int_combination_1 = int(combination_1)
Int_combination_2 = int(combination_2)
Int_combination_3 = int(combination_3)
Int_combination_4 = int(combination_4)
Int_combination_5 = int(combination_5)
Int_combination_6 = int(combination_6)

#Now do double.
Double_combination_1 = Int_combination_1 * 2
Double_combination_2 = Int_combination_2 * 2
Double_combination_3 = Int_combination_3 * 2
Double_combination_4 = Int_combination_4 * 2
Double_combination_5 = Int_combination_5 * 2
Double_combination_6 = Int_combination_6 * 2

#And then do triple.
Triple_combination_1 = Int_combination_1 * 3
Triple_combination_2 = Int_combination_2 * 3
Triple_combination_3 = Int_combination_3 * 3
Triple_combination_4 = Int_combination_4 * 3
Triple_combination_5 = Int_combination_5 * 3
Triple_combination_6 = Int_combination_6 * 3

#First create a line break and print out the result.
#We want the format be clear, so use the format function.
#Starting in line two, since we don't know how many digits does the calculated reslut have, we use "<" to let them skick to the left.
print("")
print("Combination", format("Doubled",">10"), format("Tripled",">14"))
print(format(combination_1,"<14s"), format(Double_combination_1,"<14d"), Triple_combination_1)
print(format(combination_2,"<14s"), format(Double_combination_2,"<14d"), Triple_combination_2)
print(format(combination_3,"<14s"), format(Double_combination_3,"<14d"), Triple_combination_3)
print(format(combination_4,"<14s"), format(Double_combination_4,"<14d"), Triple_combination_4)
print(format(combination_5,"<14s"), format(Double_combination_5,"<14d"), Triple_combination_5)
print(format(combination_6,"<14s"), format(Double_combination_6,"<14d"), Triple_combination_6)

#Finished!
