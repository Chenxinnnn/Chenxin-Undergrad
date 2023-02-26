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
        new += char.upper()
        for i in range(num):
            add = random.randint(65, 90)
            new += chr(add)
    return new

#Function 6
def delete_characters(word, num):
    new = ""
    for char in range(0, len(word)-1, num+1):
        new += word[char]
    return new

#Start letting user to input
pattern = input("Enter an encoding pattern, 'end' to end: ").upper()
while True:
    if pattern == "END":
        print("Program ending")
        break
    word = input("Enter a word to encode/decode: ").upper()
    for char in pattern:
        if char == "A":
            word = add_letters(word, 1)
            print("* Added 1 letter:", word)
        elif char == "X":
            word = delete_characters(word, 1)
            print("* Deleted 1 character:", word)
        elif char == "F":
            word = flip(word)
            print("* Flipped:", word)
        elif char == "U":
            word = ascii_shift(word, 1)
            print("* ASCII shift up:", word)
        elif char == "D":
            word = ascii_shift(word, -1)
            print("* ASCII shift down:", word)
        elif char == "L":
            word = shift_left(word)
            print("* Shifted left:", word)
        elif char == "R":
            word = shift_right(word)
            print("* Shifted right:", word)
        else:
            print(f"* '{char}' is an invalid command, ignoring")
    print("Final encoding / decoding:", word)
    print("")
    pattern = input("Enter an encoding pattern, 'end' to end: ").upper()

    
        

