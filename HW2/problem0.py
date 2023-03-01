total_amount = float(input("How much money did you win?"))
people_num = int(input("How many people are splitting the winnings?"))
tax_rate = float(input("What is the tax rate on lottery winnings (i.e. 25 = 25%):"))

each_person = total_amount/people_num
tax_per_person = each_person * (tax_rate/100) 
after_tax = (total_amount - (total_amount * (tax_rate/100)))/4
print("") 
print(f"In total you won ${total_amount:,.2f}") 

print(f"Split {people_num} ways that amounts to ${each_person:,.2f} per person")

print(f"Tax per person: ${tax_per_person:,.2f}")

print(f"Take home amount per person: ${after_tax:,.2f}")
