#Let the user input a number and validate if it is a positive integer.
num = int(input("Enter a positive number to test: "))
while True:
    if 0 < num:
        break
    print("Invalid number, try again.")
    num = int(input("Enter a positive number to test: "))

#First discuss the special situation if the user inputs 1 and 2.
print("")
if num == 1:
    print("1 is not a prime number.")
elif num == 2:
    print("2 is a prime number!")
#In other cases, we create a list of divisors, and divide the input number.
#If the number is divisible by the divisor, end the for loop and conclude.
#If the number is not divisible until (num - 1), tell the user it is a prime number.
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{i} is a divisor of {num}  ... stopping")
            print("")
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{i} is NOT a divisor of {num}  ... continuing")
            if i == (num - 1):
                print("")
                print(f"{num} is a prime number!")


         
