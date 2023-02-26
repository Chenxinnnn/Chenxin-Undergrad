def is_prime(a) :
    if a == 1:
        return "False"
    elif a == 2:
        return "True"
    else:
        for divisor in range(2, a):
            if a % divisor == 0:
                return "False"
            else:
                if divisor == (a - 1):
                    return "True"
                
def smallest_factor(a) :
    for divisor in range (2, a):
        if a % divisor == 0:
            return divisor
        
def is_perfect(a) :
    if a == 1:
        return "True"
    elif is_prime(a) == "True":
        return "False"
    else:
        factor_sum = 0
        next_factor = int(smallest_factor(a))
        remaining = int(a / smallest_factor(a))
        factor_sum += int(next_factor)
        while True:
            next_factor = smallest_factor(remaining)
            factor_sum += int(next_factor)
            if is_prime(next_factor) == "True":
                if a == factor_sum:
                    return "True"
                else:
                    return "False"

print(is_perfect(10))
