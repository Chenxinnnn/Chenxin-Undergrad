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

p1, h1 = collatz(9)
print(p1, h1) # 20 52

p2, h2 = collatz(7)
print(p2, h2) # 17 52

p3, h3 = collatz(27)
print(p3, h3) # 112 9232

is_prime(5)

#Let the users input and validate their input
start = int(input("Enter starting number: "))
while True:
    if start > 0:
        break
    else:
        print("Invalid, try again")
        start = int(input("Enter starting number: "))
            
end = int(input("Enter ending number: "))
while True:
    if end > 0:
        if start < end:
            break
        else:
            print("Invalid, try again")
            end = int(input("Enter ending number: "))
    else:
        print("Invalid, try again")
        end = int(input("Enter ending number: "))

#Print out the result
print("")
for num in range (start, end+1):
    period, highest = collatz(num)
    if is_even(num) == True:
        if is_prime(num) == True:
            print(f"{num} is ... even prime collatz_period: {period} collatz_highest: {highest}")
        elif is_perfect(num) == True:
            print(f"{num} is ... even perfect collatz_period: {period} collatz_highest: {highest}")
        elif is_abundant(num) == True:
            print(f"{num} is ... even abundant collatz_period: {period} collatz_highest: {highest}")
        else:
            print(f"{num} is ... even collatz_period: {period} collatz_highest: {highest}")
    else:
        if is_prime(num) == True:
            print(f"{num} is ... odd prime collatz_period: {period} collatz_highest: {highest}")
        elif is_perfect(num) == True:
            print(f"{num} is ... odd perfect collatz_period: {period} collatz_highest: {highest}")
        elif is_abundant(num) == True:
            print(f"{num} is ... odd abundant collatz_period: {period} collatz_highest: {highest}")
        else:
            print(f"{num} is ... odd collatz_period: {period} collatz_highest: {highest}")
