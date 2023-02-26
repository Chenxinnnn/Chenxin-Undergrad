def add(a,b):
    return a+b

def sub(a,b) :
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def sqrt(a):
    return a**0.5

def square(a):
    return a**2

# 1. translate this expression:
# x = (3-4) + (1*2)
x = add(sub(3, 4), mult(1,2))
print(x)

# 2. translate this expression:
# x = 5 + 1 + 7 + 9 + 13 + 12
x = add(add(add(add(add(5, 1), 7), 9), 13), 12)
print(x)

# 3. translate this expression:
# x = (5 + 1) / (7 + 2 + 3)
x = div(add(5, 1), add(add(7, 2), 3))
print(x)

# 4. compute the distance between these two points
# point 1:
x1 = 0
y1 = 0
# point 2:
x2 = 100
y2 = 100
distance = sqrt(add(square(sub(x2, x1)), square(sub(y2, y1))))
print(distance)
