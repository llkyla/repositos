print("---------------")

# for loops
## syntax: for {item} in {iterable}

for i in range(9):
  print(i) # print from 0 to 8

print("---------------")

for i in range(2,7):
  print(i) # print from 2 to 6

print("---------------")

for i in range(1,9,2):
  print(i) # print 1 3 5 7 ; from 1 to 8 print gap 2

print("---------------")

for i in range(9,2,-1):
  print(i) # from 9 to 3 print in reverse

print("---------------")

departments = ['IOE', 'CHE', 'NERS', 'EECS', 'ME']
for i in range(len(departments)): # for i in 5(length of dict)
  print(departments[i]) # IOE CHE NERS EECS ME

print("---------------")

for department in departments: 
  print(department) # i = deptmt

for cheese in departments: 
  print(cheese) # i = cheese

print("---------------")

winter2018 = {410: 35, 419: 71, 441: 51, 449: 16, 436: 22, 463: 39} # dict var; key 410 val 35

for course in winter2018.keys(): # creates an iterable object with members 410, 419, 441, 449, 436, 463
                                 # course = {410 419 441 449 436 463}
  print(str(course) + ": " + str(winter2018[course])) # winter2018[course] <- give back val

print("=================")



# while loops
## syntax: while {logical condition}:

students = 0
while students <10: # while students are less than 10
  print("Not enough students!") # print this
  students += 1 # and increase students

print("Ten students!") # after while breaks (10 times later) print this



# control systems
## syntax: if {statement}:
##         elif {statement}:
##         else:

departments = ['IOE', 'CHE', 'NERS', 'EECS', 'ME']

if 'IOE' not in departments:
  print("added IOE")
  departments.append('IOE')

if 'MATSCIE' not in departments:
  print("added MATSCIE")
  departments.append('MATSCIE')

# or

departments = ['IOE', 'CHE', 'NERS', 'EECS', 'ME']
checkDepts = ['IOE', 'MATSCIE']
for new in checkDepts: # new = [IOE, MATSCIE]
  if new not in departments:
    print("added " + new)
    departments.append(new)

print("----------")

testDigit = 6

if testDigit < 8 and testDigit >= 5: # true
  testDigit = 9

if testDigit < 8 or testDigit > 10: # false
  testDigit = 6

print(str(testDigit))

print("----------")

testDigit = 9
if testDigit <= 5: # false
  print(testDigit)
elif testDigit == 8: #false
  testDigit = 9
else: # now happens
  testDigit = 6
  print(testDigit)

print("===========")



# continue and break
testDigit = 4
while True: # always true
  testDigit += 1

  if testDigit == 7: 
    continue
  print(testDigit)

  if testDigit == 10: 
    break
  


# functions 
departments = ['IOE', 'CHE', 'NERS', 'EECS', 'ME']

if 'IOE' not in departments:
  print("added IOE")
  departments.append('IOE')

if 'MATSCIE' not in departments:
  print("added MATSCIE")
  departments.append('MATSCIE')

print("-------")

# or

def checkDept(candidate,departments): # when run checkDept, input of fn are can- & dept-; f(x,y)
  
  if candidate not in departments:
    print("added " + candidate)
    departments.append(candidate) # candiate(var) w/o values 

candidates = ["IOE", "MATSCIE", "NAME"]
departments = ['IOE', 'CHE', 'NERS', 'EECS', 'ME']

for dept in candidates: # dept = elements in candidates
  checkDept(dept,departments)

print("-------")

def squared(number): # simply return x^2
  squared = number * number
  return(squared)

print(squared(9)) # fn can be inside print

