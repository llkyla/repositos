# 120803
def solution(num1, num2):
    answer = num1 - num2
    return answer

# 120804
def solution(num1, num2):
    answer = num1 * num2
    return answer

# 120806
def solution(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer

# 120807
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    
    return answer

# 120805
def solution(num1, num2):
    answer = num1 // num2
    return answer

# 120802
def solution(num1, num2):
    answer = num1 + num2
    return answer

# 120810
def solution(num1, num2):
    answer = num1 % num2
    return answer

# 120814
def solution(n):
    if n % 7 == 0:
        answer = n // 7
    else:
        answer = (n // 7) + 1
    return answer

# 120816
def solution(slice, n):
    if n % slice == 0:
        answer = n // slice
    else:
        answer = n // slice + 1
        
    return answer

# 120817
import numpy as np

def solution(numbers):
    answer = np.mean(numbers)
    return answer

# 120819
def solution(money):
    num = money // 5500
    rem = money % 5500
    answer = [num, rem]
    return answer

# 120820
def solution(age):
    answer = 2022 - age + 1
    return answer

# 120821
def solution(num_list):
    num_list.reverse()
    return num_list

# 120822
def solution(my_string):
    answer = ''
    for i in range(1, len(my_string)+1):
        answer += my_string[-i]
    return answer

# 120824
def solution(num_list):
    
    even = 0
    odd = 0
    
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
            
    answer = [even, odd]
    
    return answer

# 120825
def solution(my_string, n):
    answer = ''
    for i in range(0, len(my_string)):
        # print(i, my_string[i])
        for j in range(n):
            answer += my_string[i]
    return answer

# 120826
def solution(my_string, letter):
    answer = ''
    for m in my_string:
        if m != letter:
            answer += m
    return answer

# 120829
def solution(angle):
    answer = 0
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    else:
        answer = 4
    return answer

# 120830
def solution(n, k):
    return (12000 * n) + (2000 * (k - (n // 10)))

# 120831
def solution(n):
    answer = 0
    for i in range(0, n+1, 2):
        answer += i
    return answer

# 120833
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 120836
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer

# 120841
def solution(dot):
    answer = 0
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] > 0:
            answer = 2
        else:
            answer = 3
    return answer

# 120847
def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer

# 120849
def solution(my_string):
    answer = my_string
    for m in my_string:
        if m in "aeiou":
            answer = answer.replace(m, "")
        
    return answer

# 120851
def solution(my_string):
    answer = 0
    for m in my_string:
        if m.isdigit():
            answer += int(m)
    
    return answer

# 120854
def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer

# 120889
def solution(sides):
    answer = 0
    sides.sort()
    if sides[-1] < (sides[0] + sides[1]):
        answer = 1
    else:
        answer = 2
    return answer

# 120893
def solution(my_string):
    answer = ''
    for m in my_string:
        if m.islower():
            answer += m.upper()
        elif m.isupper():
            answer += m.lower()
    return answer

# 120897
from math import sqrt

def solution(n):
    
    s = set()
    for i in range(1, int(sqrt(n)) +1 ):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    answer = list(s)
    answer.sort()
    return answer

# 120898
def solution(message):
    return len(message) * 2

# 120899
def solution(array):
    return [max(array), array.index(max(array))]

# 120818
def solution(price):
    answer = 0
    a = 100000
    b = 300000
    c = 500000
    if a <= price < b:
        answer = price * 0.95
    elif b <= price < c:
        answer = price * 0.90
    elif c <= price:
        answer = price * 0.80
    else:
        answer = price
    return int(answer)

# 120813
def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer

# 120839
def solution(rsp):
    result = ''
    dic = {'2':'0', '0':'5', '5':'2'}
    for x in rsp:
        result += dic[x]
    
    return result

'''
# st) dictionary
dict = {key:value}

1. for key, value in dict.items(): = both access on key, val
2. dict.get(key, default_val) = if key DNE, return default_val
3. dic1 = dict(zip(name, year)) = {name:year} for name=[], year=[]
'''

# 120811
import statistics 

def solution(array):
    
    return statistics.median(array)

# 120823
n = int(input())

for i in range(1, n+1):
    print(i * '*')

# 120837
def solution(hp):
    
    return (hp // 5) + ((hp % 5) // 3) + (((hp % 5) % 3) // 1)

# 120845
def solution(box, n):
    
    return ((box[0] // n) * (box[1] // n) * (box[2] // n))

# 120850
def solution(my_string):
    answer = []

    for x in my_string:
        if x.isdigit():
            answer.append(int(x))

    answer.sort()

    return answer

# 120891
def solution(order):
    result = 0

    for x in str(order):
        if (x == '3') or (x == '6') or (x == '9'):
            result += 1

    return result

# 120892
def solution(cipher, code):
    
    answer = ''
    
    for i in range(code-1, len(cipher), code):

        answer += cipher[i]
    
    return answer

# 120895
def solution(my_string, num1, num2):
    char_list = list(my_string)
    char_list[num1], char_list[num2] = char_list[num2], char_list[num1] 
    new_string = "".join(char_list)   

    return new_string

