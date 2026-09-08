# 120903
def solution(s1, s2):
    answer = 0
    for s in s1:
        for t in s2:
            if s == t:
                answer += 1
    return answer

# 120905
def solution(n, numlist):
    answer = []
    for m in numlist:
        if m % n == 0:
            answer.append(m)
    return answer

# 120906
def solution(n):
    answer = 0
    n = str(n)
    for m in n:
        answer += int(m)
    return answer

# 120908
def solution(str1, str2):
    if str2 in str1:
        return 1
    else: 
        return 2
    
# 120909
from math import sqrt

def solution(n):
    return 1 if sqrt(n).is_integer() else 2

# 120910
def solution(n, t):
    for i in range(0, t):
        n *= 2
    return n

# 120904
def solution(num, k):
    num = str(num)
    for i in range(0, len(num)):
        if num[i] == str(k):
            return i+1
        
    return -1

# 120911
def solution(my_string):
    char_list = list(my_string.lower())
    char_list.sort()
    result = "".join(char_list)

    return result
'''
st) ''.join(x)
from x make it as one str
'''
