#Let the user input the number of throws and validate the number.
num = int(input("Number of throws: "))
while True:
    if num >= 1:
        break
    print("Invalid, try again.")
    print("")
    num = int(input("Number of throws: "))
    print("")

#Import databases
import time
import random

#Start to count time and set of cumulative variables for each color.
start_time = time.time()
count_red = 0
count_green = 0
count_blue = 0
count_grey = 0
count_yellow = 0
count_miss = 0

#For each throw, let the computer create a random coordinate
for num in range(1, num + 1):
    x = random.uniform(0, 800)
    y = random.uniform(0, 500)

    #Use distance to determine if the throw is in green or blue region.
    distance_green = ((x - 400) ** 2 + (y - 150) ** 2) ** 0.5
    distance_blue = ((x - 400) ** 2 + (y - 300) ** 2) ** 0.5

    #The red region
    if 50 <= x <= 200 and 100 <= y <= 450:
        count_red += 1

    #The green and grey region
    elif distance_green <= 100:
        if distance_blue <= 100:
            count_grey += 1
        else:
            count_green += 1

    #The blue region
    elif distance_blue <= 100 and distance_green > 100:
        count_blue += 1
        
    #The yellow region
    elif 600 <= x <= 650 and 50 <= y <= 400:
        count_yellow += 1
    elif 700 <= x <= 750 and 50 <= y <= 400:
        count_yellow += 1
    elif 650 <= x <= 700 and 350 <= y <= 400:
        count_yellow += 1

    #The missed throws
    else:
        count_miss += 1

#Calculate percentage of each color
red_percentage = count_red / num * 100
green_percentage = count_green / num * 100
blue_percentage = count_blue / num * 100
grey_percentage = count_grey / num * 100
yellow_percentage = count_yellow / num * 100
miss_percentage = count_miss / num * 100

#End the time measure and print out the result
end_time = time.time()
time = end_time - start_time
print("")
print(f"Total time elapsed: {time:.2f} seconds")

#Conclude the result.
print("")    
print(f"Red{count_red :>17,d} ({red_percentage:.2f}%)")
print(f"Green{count_green :>15,d} ({green_percentage:.2f}%)")
print(f"Blue{count_blue :>16,d} ({blue_percentage:.2f}%)")
print(f"Grey{count_grey :>16,d} ({grey_percentage:.2f}%)")
print(f"Yellow{count_yellow :>14,d} ({yellow_percentage:.2f}%)")
print(f"Misses{count_miss :>14,d} ({miss_percentage:.2f}%)")
    
 
    
    
