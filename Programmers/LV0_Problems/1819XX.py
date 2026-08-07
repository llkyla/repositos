# 181936
def solution(number, n, m):
    
    return 1 if ((number % n == 0) & (number % m == 0)) else 0

# 181938
def solution(a, b):
    x = str(a) + str(b)
    y = 2 * a * b
    if int(x) < y:
        return y
    else:
        return int(x)

# 181935
def solution(n):

    even = 0
    odd = 0
    for m in range(1, n+1):
        if m % 2 != 0:
            odd += m

        else:
            even += (m ** 2)

    return even if (n % 2 == 0) else odd

# 181937
def solution(num, n):

    return 1 if (num % n == 0) else 0

# 181926
def solution(n, control):
    dic = {'w':1, 's':-1, 'd':10, 'a':-10}
    
    for c in control:
        if c in dic:
            n += dic[c]

    return n

# 181929
def solution(num_list):
    
    mult = 1
    
    for x in num_list:
        mult *= x
    
    sq = sum(num_list) ** 2
    
    return 1 if (mult < sq) else 0

# 181928
def solution(num_list):
    answer = 0
    even = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
            
        else:
            odd += str(i)
            

    answer = int(even) + int(odd)
    return answer

# 181933
def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b
    
# 181944
a = int(input())

if a % 2 == 0:
    print("%d is even"%a)
else:
    print("%d is odd"%a)

# 181910
def solution(my_string, n):
    return my_string[-n:]

# 181901
def solution(n, k):
    answer = []
    
    for x in range(k, n+1, k):
        answer.append(x)
    
    return answer

# 181906
def solution(my_string, is_prefix):

    return 1 if (my_string.startswith(is_prefix) == True) else 0 #.startswith()

# 181909
def solution(my_string):
    temp = []
    
    for i in range(len(my_string)-1, -1, -1):
        temp.append(my_string[i:])
        
    temp.sort()
    
    return temp

# 181911
def solution(my_strings, parts):
    answer = ''

    for i in range(len(parts)):
        answer += my_strings[i][parts[i][0] : parts[i][1]+1] 

    return answer

# 181914
def solution(number):
    res = 0
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    res = sum % 9
    
    return res

# 181919
def solution(n):
    res = [n]
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res.append(n)
        
    return res

# 181925
def solution(numLog):
    res = ''
    
    dic = {1:"w", -1:"s", 10:"d", -10:"a"}
    
    for i in range(1, len(numLog)):
        res += dic[numLog[i] - numLog[i-1]]

    return res

# 181907
def solution(my_string, n):
    
    return my_string[:n]