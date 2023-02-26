# function:     maximum
# input:        two numerical values
# processing:   find the maximum number between the two input numbers
# output:       returns the maximum number

# function:     minimum
# input:        two numerical values
# processing:   find the minimum number between the two input numbers
# output:       returns the minimum number

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

a = 5
b = 10
c = 15
d = 20
e = 20

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)

ans8 = maximum(d,e) # d and e are the same, so either is considered the maximum
ans8 = minimum(d,e) # d and e are the same, so either is considered the minimum
print(ans8, ans8) # 20 20
