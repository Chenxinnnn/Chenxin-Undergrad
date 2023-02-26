num = int(input("How many prices would you like to collect? "))
while True:
    if 0 < num:
        break
    print("Must be positive, try again")
    print("")
    num = int(input("How many prices would you like to collect? "))

print("")
print("Thanks, here we go!")
print("")

total = 0
for i in range(1, num+1):
    price = int(input(f"Enter price #{i}: "))
    while True:
        if price > 0:
            break
        print("No negative prices allowed, try again")
        print("")
        price = int(input(f"Enter price #{i}: "))
    total += price
average = total / num

print("")
print("----Report----")
print("Total:", total)
print("Average:", format(average,".2f"))
