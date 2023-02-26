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
    
a1 = is_even(5)
a2 = is_even(6)
print (a1, a2) # False True

b1 = is_odd(5)
b2 = is_odd(6)
print (b1, b2) # True False

c1 = is_prime(5)
c2 = is_prime(17)
c3 = is_prime(21)
print (c1,c2,c3) # True True False

d1 = is_perfect(6)
d2 = is_perfect(7)
d3 = is_perfect(10)
print (d1,d2,d3) # True False False

e1 = is_abundant(12)
e2 = is_abundant(13)
e3 = is_abundant(14)
print (e1,e2,e3) # True False False
