#Start with an empty list and add in each new input (check if the data is valid)
my_list = []
total = 0
for i in range(7):
    while True:
        day_sales = input(f"Sales for day {i+1}: ")
        if day_sales.isdigit():
            days_sales = int(day_sales)
            if days_sales >= 0:
                my_list.append(days_sales)
                total += days_sales 
                break
            
        print("Sorry, that is not a valid number. Please try again.")
        
print(my_list)
average = total / 7
highest = max(my_list)
lowest = min(my_list)
print("")
print(f"Total sales: {total}")
print(f"Average sales per day: {average:.2f}")
print(f"Highest sales day: {highest} (day {my_list.index(highest) + 1})")
print(f"Lowest sales day: {lowest} (day {my_list.index(lowest) + 1})")

