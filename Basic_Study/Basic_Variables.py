# Variables
count = 37 # integer
averageClasses = 12.333 # float
college = "Engineering" # string
departments = ["IOE", "CHE", "ME"] #list
abbreviations = {"IOE": "Industrial & Operations Engineering", 
                 "CHE": "Chemical Engineering", "ME": "Mechanical Engineering"} # dictionary; 1st:key 2nd:value

## string, list, dic can be indexed by []
print(college[2]) # 0 1 2 3 ...
print(abbreviations["IOE"]) # indexing the dictionary by the key returns the accompanying value

print(abbreviations["IOE"]) # key of dictionary
print(abbreviations[departments[0]]) #1st component of departments


# Methods ; 이거 다시 봐야함
abbreviations.get("ME","Not Found")
departments.sort()
print(departments)



# Integer
print("Average Classes: " + str(averageClasses)) # originally float

intAvgClasses = int(averageClasses)

print("Integer: " + str(intAvgClasses)) # print int part

intAvgClasses += 1

print("Average Classes Incremented: " + str(intAvgClasses)) # += int



# Floats
## Declare func: float()
## Notable method: na

samint = float(1e-3)
print(samint)

roundedAvg = round(averageClasses,2)
# or: averageClasses = round(averageClasses,2)
print("Before: "+ str(averageClasses))
print("After: "+ str(roundedAvg))



# String
## Declare func: string()
## Notable method: .split(), .strip(), .rstrip().

print(college[1]) # print 1 of college
print(college[0:3]) # print from 0 to 3
print(college[::-1]) # print backward

# split
number = "123-456-7--890"
print(number.split("-",1)) # split till 1st '-' (number shows how much)

room = "IOE 1610"
print(room.split()) # split when blanckspace

examp = "py thon"
print(examp.split())

# strip
courseName = "    Data Processing         "
print(courseName.strip()) # remove blankspace from the given string

course = "IOE373IOE"
print(course.strip("IOE"))

print(course.rstrip("IOE")) # only remove from right, 제일 오른쪽 string 있어야함



# List
## Declare fn: list()
## Notable method: .append(), .sort(), len() (function)

exampleList = ["North Campus", 310, 333, 34.6, "Engineering"]
anotherList = [430, 432, 434, 436, 438, 440, exampleList]
print(anotherList)

print("First: " + str(anotherList[6]))
print("Then: " + str(anotherList[6][0])) # ???

courses = [201, 202, 265, 310, 333, 366, 373]
print(str(len(courses))) # length of list

courses.append(265) # add 265 to the list
print(str(len(courses)))
print(courses)

courses.sort(reverse=True) # .sort <- sorts the list in ascending order
print(courses)

# courses.sort(key=function)

courses.reverse()
print(courses)

courses.insert(0, 200) # at 0 put 200
print(courses)

print(courses.pop()) # output last one
print(courses) # output everything but the last one

print(courses.count(265)) # how many 265?

del courses[2:]
print(courses)

courses.extend([400, 411]) # list append
print(courses)



# Dictionary
## Declare fn: dict()
## Notable methods: .keys()

abbreviations = {"IOE": "Industrial & Operations Engineering", "CHE": "Chemical Engineering", "ME": "Mechanical Engineering"}
print(abbreviations.keys()) # dict_keys(['IOE', 'CHE', 'ME]) ; 1st elements or LHS of :

for entry in abbreviations.keys(): # entry = [IOE, CHE, ME]
  print(abbreviations[entry]) # gives val of entry
                              # Industrial & Operations Engineering 
                              # Chemical Engineering
                              # Mechanical Engineering

ioeCoreCourses = [201, 202, 265, 310, 316, 333, 366, 373]
cheCoreCourses = [230, 330, 341, 342, 343, 344, 360]

coreCourses = {"IOE": ioeCoreCourses, "CHE": cheCoreCourses}

print(coreCourses) # {'IOE': [201, 202, 265, 310, 316, 333, 366, 373], 
                   # 'CHE': [230, 330, 341, 342, 343, 344, 360]}


ioe201Enrollment = {"Fall 2018": 151,  "Winter 2019": 90, "Fall 2019": 149,  "Winter 2020": 78}
ioe202Enrollment = {"Fall 2018": 150,  "Winter 2019": 86, "Fall 2019": 148,  "Winter 2020": 71}
ioe265Enrollment = {"Fall 2018": 132,  "Winter 2019": 124, "Fall 2019": 137,  "Winter 2020": 136}

ioeEnrollment = {201: ioe201Enrollment, 202: ioe202Enrollment, 265: ioe265Enrollment}

print(ioeEnrollment) # {201: {'Fall 2018': 151, 'Winter 2019': 90, 'Fall 2019': 149, 
                     # 'Winter 2020': 78}, 202: {'Fall 2018': 150, 'Winter 2019': 86, 
                     # 'Fall 2019': 148, 'Winter 2020': 71}, 265: {'Fall 2018': 132, 
                     # 'Winter 2019': 124, 'Fall 2019': 137, 'Winter 2020': 136}}
print(ioeEnrollment[201]["Fall 2018"]) # 151


