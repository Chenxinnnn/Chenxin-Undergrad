#ChenxinGu_Sep25_Section003_ChenxinGu_assign2_problem0.py

#Let the users type in needed data and define the variables.
total_amount = float(input("How much money did you win? "))
people_num = int(input("How many people are splitting the winnings? "))
tax_rate = float(input("What is the tax rate on lottery winnings (i.e. 25 = 25%): "))

#Do the calculations.
each_person = total_amount/people_num
tax_per_person = each_person * (tax_rate/100) 
after_tax = each_person - tax_per_person

#Pirnt out a line break and all the results.
#Because we don't want spce between $ and the value, we choose to use f in print instead of print function.
#Because we want comma and two decimal places in our result, we define them in {}.
print("") 
print(f"In total you won ${total_amount:,.2f}") 
print(f"Split {people_num} ways that amounts to ${each_person:,.2f} per person")
print(f"Tax per person: ${tax_per_person:,.2f}")
print(f"Take home amount per person: ${after_tax:,.2f}")
