#Depending on different months, validate the dates.

# function:     valid_date
# input:        two integers
# processing:   determine if the input integers is a valid date or not
# output:       boolean

def valid_date(a, b) :
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        if 1 <= b <= 31:
            return True
        else:
            return False
    elif a == 4 or a == 6 or a == 9 or a == 11:
        if 1 <= b <= 30:
            return True
        else:
            return False
    elif a == 2:
        if 1 <= b <= 28:
            return True
        else:
            return False
    else:
        return False
    
print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False

