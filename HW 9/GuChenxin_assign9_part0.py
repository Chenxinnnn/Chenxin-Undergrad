#First read the class data file
response1 = open("class_data.txt", "r")
data1 = response1.read()
response1.close()

#Read the enrollment data file
response2 = open("enrollment_data.txt", "r")
data2 = response2.read()
response1.close()

#Analyze the data, spliting them
datas1 = data1.split("\n")
course_list = []
course_title = []
for i in datas1:
    ii = i.split(",")
    try:
        course_list.append(ii[0])
    except:
        print("", end = "")
    try:
        course_title.append(ii[1])
        
    except:
        print("", end = "")

datas2 = data2.split("\n")
enroll_list = []
lastname_list = []
firstname_list = []
for n in datas2:
    nn = n.split(",")
    try:
        enroll_list.append(nn[0])
    except:
        print("", end = "")
    try:
        lastname_list.append(nn[1])
    except:
        print("", end = "")
    try:
        firstname_list.append(nn[2])
    except:
        print("", end = "")

#Start the system. Let the users input
print("NYU Computer Science Registration System")
your_course = input("Enter a course (i.e. CS0002, CS0004): ").upper()
if your_course in course_list:
    people_enrolled = 0
    position = course_list.index(your_course)
    co_title = course_title[position]
    print(f"The title of this class is: {co_title}")
    real_index = 0
    name_list = []
    for enroll in enroll_list:
        name = ""
        if enroll == your_course:
            people_enrolled += 1
            name = lastname_list[real_index] + "," + firstname_list[real_index]
            name_list.append(name)
        real_index += 1
    print(f"The course has {people_enrolled} students enrolled")
    for x in name_list:
        print(f"* {x}")

else:
    print("Cannot find this course")
