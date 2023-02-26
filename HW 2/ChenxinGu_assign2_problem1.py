#ChenxinGu_Sep25_Section003_ChenxinGu_assign2_problem1.py

#Start the program with the title, and be sure to contail all the line breaks.
#For the line "3 Year Bank Account Balance Forecast", use format in print to make it center under the *s.
print("**************************************************")
title="3 Year"
print(f"{title:>13s} Bank Account Balance Forecast")
print("**************************************************")
print("")
print("This program will project how much you could earn by investing money in")
print("a bank account that pays out interest on a yearly basis.")
print("")


#Let the users enter all the data we need and define the variables.
#Since we need to do calculation later, change all the data type into float.
#Include all the line breaks.
deposit1 = float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
interest_rate1 = float(input("Next, enter the expected interest rate for year 1. For example, enter 5 for 5%: "))
print("")

deposit2 = float(input("How much will you invest at the beginning of year 2? "))
interest_rate2 = float(input("What is the expected interest rate for year 2? "))
print("")

deposit3 = float(input("How much will you invest at the beginning of year 3? "))
interest_rate3 = float(input("What is the expected interest rate for year 3? "))
print("")


#Do the calculations.
Year1_starting_balance = 0.00
Year1_earned = deposit1 * (interest_rate1 / 100)
Year1_ending_balance = deposit1 + Year1_earned
Year2_starting_balance = Year1_ending_balance + deposit2
Year2_earned = Year2_starting_balance * (interest_rate2 / 100)
Year2_ending_balance = Year2_starting_balance + Year2_earned
Year3_starting_balance = Year2_ending_balance + deposit3
Year3_earned = Year3_starting_balance * (interest_rate3 / 100)
Year3_ending_balance = Year3_starting_balance + Year3_earned
Total_deposit = deposit1 + deposit2 + deposit3
Total_interest_earned = Year1_earned + Year2_earned + Year3_earned

#Then print out all the results.
#We want to make our output look like a form, so use the format function.
#Because we don't know how many digits does our results have, starting from the second line, use < to let the space count from the left side.
#We need the commas and decimal places to be fixed in our result, keep it in the format function.
print("--- YOUR FORECAST ---")
print("")
print("Year", format("Starting Balance",">26s"), format("Deposit",">15s"), format("Interest Earned",">20s"), format("Ending Balance",">20s"))
print(f"1{Year1_starting_balance:>30,.2f}{deposit1:>16,.2f}{Year1_earned:>21,.2f}{Year1_ending_balance:>21,.2f}")
print(f"2{Year1_ending_balance:>30,.2f}{deposit2:>16,.2f}{Year2_earned:>21,.2f}{Year2_ending_balance:>21,.2f}")
print(f"3{Year2_ending_balance:>30,.2f}{deposit3:>16,.2f}{Year3_earned:>21,.2f}{Year3_ending_balance:>21,.2f}")
print("")
print(f"Total deposited: ${Total_deposit:,.2f}")
print(f"Total interest earned: ${Total_interest_earned:,.2f}")

