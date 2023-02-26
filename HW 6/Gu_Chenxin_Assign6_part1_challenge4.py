
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

def simple_sort_version1(a, b):
    return minimum(a, b), maximum(a,b)


a,b = simple_sort_version1(10,20)
print (a,b) # 10 20

a,b = simple_sort_version1(20,10)
print (a,b) # 10 20

a,b = simple_sort_version1(30,30)
print (a,b) # 30 30
