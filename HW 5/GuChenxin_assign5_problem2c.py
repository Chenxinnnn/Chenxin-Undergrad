#First let the user input their start and end number and validate the value.
start = int(input("Start number: "))
end = int(input("End number: "))
while True:
    if start >0 and end >0:
        if start < end:
            break
        else:
            print("End number must be greater than start number")
            print("")
            start = int(input("Start number: "))
            end = int(input("End number: "))
    else:
        print("Start and end must be positive")
        print("")
        start = int(input("Start number: "))
        end = int(input("End number: "))

#Then for numbers in the given range, find the prime numbers.
print("")
for num in range (start, end + 1):
    if num == 2:
        print("2")
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                break
            else:
                if divisor == (num - 1):
                    print(f"{num}")   
