print("**************************************************")
title="3 Year"
print(f"{title:>13s} Bank Account Balance Forecast")
print("**************************************************")
print("")
print("This program will project how much you could earn by investing money in")
print("a bank account that pays out interest on a yearly basis.")
print("")

deposit1 = float(input("To begin, enter how much money you would like to initially invest (i.e. 5000): "))
interest_rate1 = float(input("Next, enter the expected interest rate for year 1. For example, enter 5 for 5%: "))
print("")

deposit2 = float(input("How much will you invest at the beginning of year 2? "))
interest_rate2 = float(input("What is the expected interest rate for year 2? "))
print("")

deposit3 = float(input("How much will you invest at the beginning of year 3? "))
interest_rate3 = float(input("What is the expected interest rate for year 3? "))
print("")

#Do the calculations
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

#print out the results
print("--- YOUR FORECAST ---")
print("")
print("Year", format("Starting Balance",">26s"), format("Deposit",">15s"), format("Interest Earned",">20s"), format("Ending Balance",">20s"))
print(f"1{Year1_starting_balance:>30,.2f}{deposit1:>16,.2f}{Year1_earned:>21,.2f}{Year1_ending_balance:>21,.2f}")
print(f"2{Year1_ending_balance:>30,.2f}{deposit2:>16,.2f}{Year2_earned:>21,.2f}{Year2_ending_balance:>21,.2f}")
print(f"3{Year2_ending_balance:>30,.2f}{deposit3:>16,.2f}{Year3_earned:>21,.2f}{Year3_ending_balance:>21,.2f}")
print("")
print(f"Total deposit: ${Total_deposit:,.2f}")
print(f"Total interest earned: ${Total_interest_earned:,.2f}")

