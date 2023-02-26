print("1 is technically not a prime number.")
print("2 is a prime number!")

#In other cases, we create a list of divisors, and divide the input number.
#If the number is divisible by the divisor, end the for loop.
#If the number is not divisible until (num - 1), tell the user it is a prime number.
for num in range (3, 1000): 
    for divisor in range(2, num):
        if num % divisor == 0:
            break
        else:
            if divisor == (num - 1):
                print(f"{num} is a prime number!")

 
            
                

         
