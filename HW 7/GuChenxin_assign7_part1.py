#fist let the user enter a username
username = input("Enter a username: ")
#Use length function to determine its length
print("* Length of username:", len(username))
#Use the isalnum method to check if it contaions special characters
print("* All characters are alpha-numeric:", username.isalnum())
#Examine if the first and last characters are not digits
First = username[0]
Last = username[-1]
print("* First & last characters are not digits:", First.isdigit() == False and Last.isdigit() == False)

#Count the number of upper/lower-case alphabets.
uppers = 0
lowers = 0
for char in username:
    if char.isupper() == True:
        uppers += 1

    elif char.islower() == True:
        lowers += 1

print("* # of uppercase characters in the username:", uppers)
print("* # of lowercase characters in the username:", lowers)

#Count the number of digits in the username
digits = 0
for char in username:
    if char.isdigit() == True:
        digits += 1

print("* # of digits in the username:", digits)

#Set up the loop if the user name is not validate
while True:
    if 8 <= len(username) <= 15 and username.isalnum() == True and First.isdigit() == False and Last.isdigit() == False and uppers != 0 and lowers != 0 and digits != 0:
        break

    print("Username is invalid, please try again")
    print("")
    username = input("Enter a username: ")
    print("* Length of username:", len(username))
    print("* All characters are alpha-numeric:", username.isalnum())
    First = username[0]
    Last = username[-1]
    print("* First & last characters are not digits:", First.isdigit() == False and Last.isdigit() == False)

    uppers = 0
    lowers = 0
    for char in username:
        if char.isupper() == True:
            uppers += 1

        elif char.islower() == True:
            lowers += 1

    print("* # of uppercase characters in the username:", uppers)
    print("* # of lowercase characters in the username:", lowers)

    digits = 0
    for char in username:
        if char.isdigit() == True:
            digits += 1
    print("* # of digits in the username:", digits)

#Tell the user the username if valid if it meets all the conditions.
print("Username is valid!")
print("")

#The password part
password = input("Enter a password: ")
print("* Length of password:", len(password))
print("* Username is part of password:", username in password)

pass_uppers = 0
pass_lowers = 0
for char in password:
    if char.isupper() == True:
        pass_uppers += 1

    elif char.islower() == True:
        pass_lowers += 1

print("* # of uppercase characters in the password:", pass_uppers)
print("* # of lowercase characters in the password:", pass_lowers)

pass_digits = 0
for char in password:
    if char.isdigit() == True:
        pass_digits += 1

print("* # of digits in the username:", pass_digits)

special = "#$%&"
pass_special = 0
for char in password:
    if char in special:
        pass_special += 1
print("* # of special characters in the password:", pass_special)

#For invalid characters
invalid = 0
for char in password:
    if char not in special and char.isalnum()== False:
        invalid += 1
print("* # of invalid characters in the password:", invalid)

#for the duplicate part
index = -1
total_duplicate = 0
for char in password:
    index += 1
    duplicate = 0
    if password.count(char) > 1:
        if password.find(char) == index:
            duplicate += password.count(char)
            total_duplicate += password.count(char)
            print(f"* duplicate character: '{char}' occurs {duplicate} times")
            
while True:
    if len(password) >= 8 and (username not in password) and pass_uppers != 0 and pass_lowers != 0 and pass_digits != 0 and pass_special != 0 and invalid == 0 and duplicate == 0:
        break
    print("Password is invalid, please try again")
    print("")

    password = input("Enter a password: ")
    print("* Length of password:", len(password))
    print("* Username is part of password:", username in password)

    pass_uppers = 0
    pass_lowers = 0
    for char in password:
        if char.isupper() == True:
            pass_uppers += 1

        elif char.islower() == True:
            pass_lowers += 1

    print("* # of uppercase characters in the password:", pass_uppers)
    print("* # of lowercase characters in the password:", pass_lowers)

    pass_digits = 0
    for char in password:
        if char.isdigit() == True:
            pass_digits += 1

    print("* # of digits in the username:", pass_digits)

    special = "#$%&"
    pass_special = 0
    for char in password:
        if char in special:
            pass_special += 1
    print("* # of special characters in the password:", pass_special)

    #For invalid characters
    invalid = 0
    for char in password:
        if char not in special and char.isalnum()== False:
            invalid += 1
    print("* # of invalid characters in the password:", invalid)

    #for the duplicate part
    index = -1
    total_duplicate = 0
    for char in password:
        duplicate = 0
        index += 1
        if password.count(char) > 1:
            if password.find(char) == index:
                duplicate += password.count(char)
                total_duplicate += password.count(char)
                print(f"* duplicate character: '{char}' occurs {duplicate} times")
                
            
print("Password is valid!")        
