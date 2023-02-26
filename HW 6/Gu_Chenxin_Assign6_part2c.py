def is_even(a) :
    if a % 2 == 0:
        return True
    else:
        return False

def is_odd(a) :
    if a % 2 == 0:
        return False
    else:
        return True

def is_prime(a) :
    if a == 1:
        return False
    elif a == 2:
        return True
    else:
        for divisor in range(2, a):
            if a % divisor == 0:
                return False
            else:
                if divisor == (a - 1):
                    return True

def is_perfect(a) :
    Sum = 0
    for divisor in range(1, a):
        if a % divisor == 0:
            Sum += divisor
    if Sum == a:
        return True
    else:
        return False        

def is_abundant(a) :
    Sum = 0
    for divisor in range(1, a):
        if a % divisor == 0:
            Sum += divisor
    if Sum > a:
        return True
    else:
        return False

def collatz(a):
    period = 1
    highest = a
    while True:
        if a == 1:
            return period, highest

        elif a % 2 == 0:
            a /= 2
            if a > highest:
                highest = int(a)
            period += 1
        
        elif a % 2 != 0:
            a *= 3
            a += 1
            if a > highest:
                highest = int(a)
            period += 1
            
#Give out the choices and let the users choose, then validate their answer
print("1 - Find all prime numbers within a given range")
print("2 - Find all perfect numbers within a given range")
print("3 - Find all abundant numbers within a given range")
print("4 - Compute the Collatz period and highest numbers for a given range")
print("5 - Chart all even, odd, prime, perfect, abundant numbers within a given range along with their Collatz info")
print("6 - Quit")
print("")
choice = int(input("Your choice: "))
while True:
    if choice == 1:
        print("")
        start_prime = int(input("Enter a starting value: "))
        while True:
            if start_prime > 0:
                break
            print("Number is too low, try again")
            start_prime = int(input("Enter a starting value: "))

        end_prime = int(input("Enter ending number: "))
        while True:
            if end_prime > 0:
                if start_prime < end_prime:
                    break
                else:
                    print("Invalid, try again")
                    end_prime = int(input("Enter ending number: "))
            else:
                print("Invalid, try again")
                end_prime = int(input("Enter ending number: "))
        print("")
        print(f"All primes between {start_prime} and {end_prime}")
        print("##########")
        for num in range (start_prime, end_prime+1):
            if is_prime(num) == True:
                print(num)
        print("##########")

    #if the user chose 2
    elif choice == 2:
        print("")
        start_perfect = int(input("Enter a starting value: "))
        while True:
            if start_perfect > 0:
                break
            print("Number is too low, try again")
            start_perfect = int(input("Enter a starting value: "))

        end_perfect = int(input("Enter ending number: "))
        while True:
            if end_perfect > 0:
                if start_perfect < end_perfect:
                    break
                else:
                    print("Number is too low, try again")
                    end_perfect = int(input("Enter ending number: "))
            else:
                print("Invalid, try again")
                end_perfect = int(input("Enter ending number: "))
        print("")
        print(f"All perfect numbers between {start_perfect} and {end_perfect}")
        print("##########")
        for num in range (start_perfect, end_perfect+1):
            if is_perfect(num) == True:
                print(num)
        print("##########")

    #If the user chose 3
    elif choice == 3:
        print("")
        start_abundant = int(input("Enter a starting value: "))
        while True:
            if start_abundant > 0:
                break
            print("Number is too low, try again")
            start_abundant = int(input("Enter a starting value: "))

        end_abundant = int(input("Enter ending number: "))
        while True:
            if end_abundant > 0:
                if start_abundant < end_abundant:
                    break
                else:
                    print("Invalid, try again")
                    end_abundant = int(input("Enter ending number: "))
            else:
                print("Invalid, try again")
                end_abundant = int(input("Enter ending number: "))
        print("")
        print(f"All abundant numbers between {start_abundant} and {end_abundant}")
        print("##########")
        for num in range (start_abundant, end_abundant+1):
            if is_abundant(num) == True:
                print(num)
        print("##########")

    #if users chose 4
    elif choice == 4:
        print("")
        start_Collatz = int(input("Enter a starting value: "))
        while True:
            if start_Collatz > 0:
                break
            print("Number is too low, try again")
            start_Collatz = int(input("Enter a starting value: "))

        end_Collatz = int(input("Enter ending number: "))
        while True:
            if end_Collatz > 0:
                if start_Collatz < end_Collatz:
                    break
                else:
                    print("Invalid, try again")
                    end_Collatz = int(input("Enter ending number: "))
            else:
                print("Invalid, try again")
                end_Collatz = int(input("Enter ending number: "))
        print("")
        print(f"All Collatz periods & high values between {start_Collatz} and {end_Collatz}")
        print("")
        print("Number", format("Period", ">9"), format("High Value", ">13"))
        for num in range(start_Collatz, end_Collatz + 1):
            period, highest = collatz(num)
            print(f"{num:<10}{period:<10}{highest}")

    elif choice == 5:
        print("")
        start_analysis = int(input("Enter a starting value: "))
        while True:
            if start_analysis > 0:
                break
            print("Number is too low, try again")
            start_analysis = int(input("Enter a starting value: "))

        end_analysis = int(input("Enter ending number: "))
        while True:
            if end_analysis > 0:
                if start_analysis < end_analysis:
                    break
                else:
                    print("Invalid, try again")
                    end_analysis = int(input("Enter ending number: "))
            else:
                print("Invalid, try again")
                end_analysis = int(input("Enter ending number: "))
        print("")
        print(f"Number Analysis: {start_analysis} and {end_analysis}")
        print(format("Number","<9"), "Even", "Odd", "Prime", "Perfect", "Abundant", "Period/Highest")
        x = "x"
        for num in range(start_analysis, end_analysis+1):
            period, highest = collatz(num)
            if is_even(num) == True:
                if is_prime(num) == True:
                    print(f"{num:<10}{x:<10}{x:<22}{period}/{highest}")
                elif is_perfect(num) == True:
                    print(f"{num:<10}{x:<16}{x:<16}{period}/{highest}")
                elif is_abundant(num) == True:
                    print(f"{num:<10}{x:<24}{x:<8}{period}/{highest}")
                else:
                    print(f"{num:<10}{x:<32}{period}/{highest}")
            else:
                if is_prime(num) == True:
                    print(f"{num:<15}{x:<5}{x:<22}{period}/{highest}")
                elif is_perfect(num) == True:
                    print(f"{num:<15}{x:<11}{x:<16}{period}/{highest}")
                elif is_abundant(num) == True:
                    print(f"{num:<15}{x:<19}{x:<8}{period}/{highest}")
                else:
                    print(f"{num:<15}{x:<27}{period}/{highest}")

    #if the users choose option 6, end the program
    elif choice == 6:
        print("Program ending")
        break

    #If the user input an invalidate number
    else:   
        print("Unrecognized command, try again")
        
    print("")
    print("1 - Find all prime numbers within a given range")
    print("2 - Find all perfect numbers within a given range")
    print("3 - Find all abundant numbers within a given range")
    print("4 - Compute the Collatz period and highest numbers for a given range")
    print("5 - Chart all even, odd, prime, perfect, abundant numbers within a given range along with their Collatz info")
    print("6 - Quit")
    print("")
    choice = int(input("Your choice: "))
print("")

#if the user chooses to find prime numbers


