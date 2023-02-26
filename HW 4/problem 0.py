num1 = int(input("Number 1: "))
while num1<0 :
    print("Invalid, try again")
    num1 = int(input("Number 1: "))

# excellent job using 2 data validation loops for this! -Craig
num2 = int(input("Number 2: "))
while num2<num1:
    print("Invalid, try again")
    num2 = int(input("Number 2: "))


x = num1
while x<=num2:
    print(x,"*"*x)
    x+=1

y = num2
while y>=num1:
    print(y , "*"*y)
    y-=1
