import datetime
import random
#Function 1
def ascii_shift(word, num):
    new_word = ""
    if num >= 0:
        shift_num = num % 26
        for char in word:
            if char.isupper():
                new_order = int(ord(char)) + shift_num
                if new_order < 65:
                    new_order = 91 - (65 - new_order)
                elif new_order >90:
                    new_order = 64 + (new_order - 90)
                new = chr(new_order)
                new_word += new
                
            else:
                new_word += char
    
    else:
        shift_num = num % (-26)
        for char in word:
            if char.isupper():
                new_order = int(ord(char)) + shift_num
                if new_order < 65:
                    new_order = 91 - (65 - new_order)
                elif new_order >90:
                    new_order = 64 + (new_order - 90)
                new = chr(new_order)
                new_word += new
            else:
                new_word += char
    
    return new_word


#Function 2
def shift_right(a):
    if a == "":
        return ""
    else:
        new = a[-1] + a[0: len(a)-1]
        return new

#Function 3
def shift_left(a):
    if a == "":
        return ""
    else:
        new = a[1:len(a)] + a[0]
        return new

#Function 4
def flip(a):
    if a == "":
        return ""
    elif len(a) % 2 == 0:
        new = a[len(a)//2 : len(a)+1] + a[0 : len(a)//2]
        return new
    else:
        new = a[len(a)//2+1 : len(a)] + a[len(a)//2] + a[0 : len(a)//2]
        return new

#Function 5
def add_letters(word, num):
    new = ""
    for char in word:
        new += char
        for i in range(num):
            add = random.randint(65, 90)
            new += chr(add).upper()
    return new

#Function 6
def delete_characters(word, num):
    new = ""
    for char in range(0, len(word)-1, num+1):
        new += word[char]
    return new


response1 = open("user_info.txt", "r")
data1 = response1.read()
response1.close()

datas1 = data1.split("\n")
username_list = []
password_list = []
for i in datas1:
    ii = i.split(",")
    try:
        username_list.append(ii[0])
        password_list.append(ii[1])
    except:
        print("", end = "")
  
def valid_username(username):
    if len(username) < 5:
        return False
    elif username.isalnum() == False:
        return False
    elif username[0].isdigit():
        return False
    else:
        return True

def valid_password(p):
    if len(p) < 5:
        return False
    elif p.isalnum() == False:
        return False
    elif p.isupper() or p.islower():
        return False
    elif p.isalpha() or p.isdigit():
        return False
    else:
        return True

def username_exists(u):
    if u == "":
        return False
    elif u in username_list:
        return True
    else:
        return False

def check_password(u, p):
    if u == "" or p == "":
        return False
    else:
        position = 0
        for username in username_list:
            if username == u:
                copassword = password_list[position]
                if copassword == p:
                    return True
            position += 1
        return False

def add_user(u, p):
    if username_exists(u) == False:
        newitem = u + "," + p + "\n"
        file_object = open("user_info.txt", "a")
        file_object.write(newitem)
        file_object.close()
        send_message("admin", u, "Welcome to your account!")
        return True
    else:
        return False

def send_message(s, r, m):
    d = datetime.datetime.now()
    month = d.month
    day = d.day
    year = d.year
    hour = d.hour
    minute = d.minute
    second = d.second
    if len(str(month)) == 1:
        month = "0" + str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    if len(str(second)) == 1:
        second = "0" + str(second)
    time = f"|{month}/{day}/{year} {hour}:{minute}:{second}|"
    new_line = s + time + m + "\n"
    try:
        file = open(f"messages/{r}.txt", "a")
        file.write(new_line)
        file.close()
        
    except:
        file = open(f'messages/{r}.txt', 'w')
        file.write(new_line)
        file.close()


def print_messages(u):
    file = open(f'messages/{u}.txt', 'r')
    alldata = file.read()
    file.close()
    if alldata == "":
        print("No messages in your inbox")
        return False
    else:
        alldatas = alldata.split("\n")
        time_list = []
        sender_list = []
        message_list = []
        message_number = 0
        for i in alldatas:
            
            message_number += 1
            ii = i.split("|")
            try:
                sender_list.append(ii[0])
                time_list.append(ii[1])
                message_list.append(ii[2])
                print(f"Message #{message_number} received from {ii[0]}")
                print(f"Time: {ii[1]}")
                print(ii[2])
                print("")
            except:
                print("", end = "")
        
def delete_messages(u):
    file = open(f"messages/{u}.txt", "w")
    file.write("")
    file.close()


#Create an administration account at the beginning of the program.
if username_exists("admin") == False:
    newitem = "admin" + "," + "password" + "\n"
    file_object = open("user_info.txt", "a")
    file_object.write(newitem)
    file_object.close()  

#Start letting the users to use the system
while True:
    signal = input("(l)ogin, (r)egister or (q)uit: ").lower()
    print("")
    #When user inputs r
    if signal == "r":
        print("Register for an account")
        u = input("Username (case sensitive): ")
        p = input("Password (case sensitive): ")
        if valid_username(u):
            if username_exists(u) == False:
                if valid_password(p):
                    add_user(u, p)
                    response1 = open("user_info.txt", "r")
                    data1 = response1.read()
                    response1.close()

                    datas1 = data1.split("\n")
                    username_list = []
                    password_list = []
                    for i in datas1:
                        ii = i.split(",")
                        try:
                            username_list.append(ii[0])
                            password_list.append(ii[1])
                        except:
                            print("", end = "")
                    print("Registration successful!")
                else:
                    print("Password is invalid, registration cancelled")
            else:
                print("Duplicate username, registration cancelled")
        else:
            print("Username is invalid, registration cancelled")
        print("")

    #When use inputs l
    elif signal == "l":
        print("Log In")
        login_u = input("Username (case sensitive): ")
        login_p = input("Password (case sensitive): ")
        if check_password(login_u, login_p):
            while True:
                print(f"You have been logged in successfully as {login_u}")
                choice = input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ").lower()
                #If the user chooses to send a message
                if choice == "s":
                    r = input("Username of recipient: ")
                    if r in username_list:
                        m = input("Type your message: ")
                        s = input("Would you like to encrypt your message? (y)es or (n)o: ").lower()
                        if s == "y":
                            pattern = input("Enter your encryption key (valid commands include 'AXFUDLR'): ").upper()
                            word = m    
                            invalid = ""
                            for char in pattern:
                                if char == "A":
                                    word = add_letters(word, 1)
                                elif char == "X":
                                    word = delete_characters(word, 1)
                                elif char == "F":
                                    word = flip(word)
                                elif char == "U":
                                    word = ascii_shift(word, 1)
                                elif char == "D":
                                    word = ascii_shift(word, -1)
                                elif char == "L":
                                    word = shift_left(word)
                                elif char == "R":
                                    word = shift_right(word)
                                else:
                                    invalid += char
                            if invalid != "":
                                print(f"'{invalid}' is(are) invalid command(s), ignoring")
                            send_message(login_u, r, word)
                            print("Message sent!")
            
                        elif s == "n":
                            send_message(login_u, r, m)
                            print("Message sent!")

                        else:
                            print("Invalid command, action cancelled")
                    else:
                        print("Unknown recipient")
                    print("")

                #If the user choose to read messages        
                elif choice == "r":
                    g = print_messages(login_u)
                    print("")
                    if g != False:
                        print("")
                        d = input("Would you like to decode one of your messages? (y)es or (n)o: ").lower()
                        if d == "y":
                            number = input("Which message number would you like to decode? ")
                            if number.isdigit() == False:
                                print("Invalid input, operation cancelled")
                                print("")
                            else:
                                file = open(f'messages/{login_u}.txt', 'r')
                                alldata = file.read()
                                file.close()
                                if alldata == "":
                                    print("No such message, operation cancelled")
                                else:
                                    alldatas = alldata.split("\n")
                                    time_list = []
                                    sender_list = []
                                    message_list = []
                                    message_number = 0
                                    for i in alldatas:
                                        message_number += 1
                                        ii = i.split("|")
                                        try:
                                            sender_list.append(ii[0])
                                            time_list.append(ii[1])
                                            message_list.append(ii[2])
                                        except:
                                            print("", end = "")
                        
                                    if int(number) >= message_number:
                                        print("No such message, operation cancelled.")
                                        print("")

                                    elif int(number) == 0:
                                        print("Invalid command, operation cancelled.")
                                        print("")

                                    else:
                                        
                                        pattern = input("Enter your decryption key (valid commands include 'AXFUDLR'): ").upper()
                                        word = message_list[int(number)-1]
                                        invalid = ""
                                        for char in pattern:
                                            if char == "A":
                                                word = add_letters(word, 1)
                                            elif char == "X":
                                                word = delete_characters(word, 1)
                                            elif char == "F":
                                                word = flip(word)
                                            elif char == "U":
                                                word = ascii_shift(word, 1)
                                            elif char == "D":
                                                word = ascii_shift(word, -1)
                                            elif char == "L":
                                                word = shift_left(word)
                                            elif char == "R":
                                                word = shift_right(word)
                                            else:
                                                invalid += char
                                        if invalid != "":
                                            print(f"'{invalid}' is(are) invalid command(s), ignoring")
                                        print(f"Decrypted message: {word}")
                                        print("")
                        elif d == "n":
                            print("")
                        else:
                            print("Invalid command, action cancelled")

                elif choice == "d":
                    delete_messages(login_u)
                    print("Your messages have been deleted")
                    print("")

                elif choice == "l":
                    print(f"Logging out as username {login_u}")
                    print("")
                    break
                
                else:
                    print("Invalid choice, try again.")
                    print("")
                    
        else:
            print("Invalid username or password, log-in cancelled")
            print("")

    #If the user choose to quit
    elif signal == "q":
        print("")
        print("Goodbye!")
        break

    #If the user input invalid choice
    else:
        print("Invalid choice, try again.")
        print("")
                
        
            
        
        
        
    
