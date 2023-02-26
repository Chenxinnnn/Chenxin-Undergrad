valid = 0
my_list = []
while valid < 3:
    number = input("Enter a number: ")
    if number.isdigit():
        int_number = int(number)
        valid += 1
        my_list.append(int_number)
    else:
        print("Invalid, try again")

my_list.sort()
for i in my_list:
    print(i, end = " ")
