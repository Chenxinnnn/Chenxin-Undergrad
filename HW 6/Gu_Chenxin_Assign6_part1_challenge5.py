def maximum(a,b) :
    if a >= b:
        Max = a
    else:
        Max = b
    return Max

def minimum(a,b) :
    if a <= b:
        Min = a
    else:
        Min = b
    return Min

#Divide into situations if c is larger than max(a, b) or if c is less than min(a, b)
#or, else
def simple_sort_version2(a,b,c) :
    if maximum(a,b) <= c:
        return minimum(a, b), maximum(a,b), c
    elif minimum(a,b) >= c:
        return c, minimum(a, b), maximum(a,b)
    else:
        return minimum(a, b), c, maximum(a,b)

        
a,b,c = simple_sort_version2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_version2(30,20,20)
print (a,b,c) # 20 20 30
