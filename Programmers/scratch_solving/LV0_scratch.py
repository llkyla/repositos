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

# wth1
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

###################################

def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer

print(solution(["We", "are", "the", "world!"]))

# wth1
def solution(strlist):
    return list(len(str) for str in strlist)

###################################

def solution(s1, s2):
    answer = 0
    for s in s1:
        for t in s2:
            if s == t:
                answer += 1
    return answer

#wth
def solution(s1, s2):
    return len(set(s1)&set(s2))

###################################

def solution(s1, s2):
    answer = 0
    for s in s1:
        for t in s2:
            if s == t:
                answer += 1
    return answer

#wth
def solution(s1, s2):
    return len(set(s1)&set(s2))

def solution(n, numlist):
    answer = []
    for m in numlist:
        if m % n == 0:
            answer.append(m)
    return answer

# wth 1 lambda



def solution(n, t):
    for i in range(0, t):
        n *= 2
    return n

# wth
def solution(n, t):
    return n << t



def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

# wth

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)



def solution(n):

    even = 0
    odd = 0
    for m in range(1, n+1):
        if m % 2 != 0:
            odd += m

        else:
            even += (m ** 2)

    return even if (n % 2 == 0) else odd
 
        
print(solution(10))

# wth
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])



def solution(num_list, n):
    answer = []
    
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
        
    return answer

print(solution([4, 2, 6, 1, 7, 6], 2))

# wth
def solution(num_list, n):
    return num_list[::n]



def solution(n, control):
    for c in control:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        else:
            n -= 10
    return n

# wth
def solution(n, control):
    dic = {'w':1, 's':-1, 'd':10, 'a':-10}
    
    for c in control:
        if c in dic:
            n += dic[c]

    return n



def solution(cipher, code):
    
    answer = ''
    
    for i in range(code-1, len(cipher), code):

        answer += cipher[i]
    
    
    return answer

# wth
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer



def solution(my_string, num1, num2):

    x = my_string[num1]
    my_string.replace(my_string[num1], my_string[num2])
    print(my_string.replace(my_string[num1], my_string[num2]))
    my_string.replace(my_string[num2], x)
    return 0

# wth
def solution(my_string, num1, num2):
    char_list = list(my_string)
    char_list[num1], char_list[num2] = char_list[num2], char_list[num1] 
    new_string = "".join(char_list)   
    return new_string



def solution(n_str):
    
    result = ''
    
    for i in range(0, len(n_str)):
        if n_str[i] != "0":
            result = n_str[i:]
            return result
    return result

# wth

def solution(n_str):
    return n_str.lstrip('0')



def solution(num_list):
    result = []
    num_list.sort()
    result = num_list[5:]
    return result

# wth
def solution(num_list):
    return sorted(num_list)[5:]



def solution(myString):
    answer = []
    n = 0
    for i in range(len(myString)):
        if myString[i] == "x":
            answer.append(len(myString[n:i]))
            n = i+1

    answer.append(len(myString[n:]))   
    
    return answer

print(solution("oxooxoxxox"))

# wth
def solution(myString):                                                                                                     
        return [len(substring) for substring in myString.split('x')]      


def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if "ad" not in strArr[i]:
            answer.append(strArr[i])
    
    return answer

print(solution(["and","notad","abcd"]))

# wth
def solution(strArr):
    answer = []
    for x in strArr:
        if 'ad' in x: continue
        answer.append(x)
    return answer



def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
            print(answer)
        
        else:
            answer.append(strArr[i].upper())
            print(answer)
    return answer

print(solution(["AAA","BBB","CCC","DDD"]))

# wth
def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]



def solution(myString, pat):
    
    return 1 if ((pat.lower()) in (myString.lower())) else 0

print(solution("AbCdEfG", "aBc"))
print(sol("AbCdEfG", "aBc"))

# wth
def solution(myString, pat):
    return int(pat.lower() in myString.lower()) # boolean 사용방법



def solution(num_list):
    answer = 1
    if len(num_list) <= 10:
        for i in range(len(num_list)):
            answer *= num_list[i]
        return answer
    else:
        sum_ans = sum(num_list)
        return sum_ans
            

print(solution([2, 3, 4, 5]))

# wth
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)



def solution(names):
    answer = []
    
    for i in range(0, len(names), 5):
        answer.append(names[i])
        
    return answer

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))

# wth
def solution(names):
    return names[::5] # oOo..



def solution1(num_list):
    even = 0
    odd = 0
    
    for i in range(0, len(num_list), 2):
        even += num_list[i]

    for j in range(1, len(num_list), 2):
        odd += num_list[j]

    return max(even, odd)
    
print(solution1([4, 2, 6, 1, 7, 6])) #???


# wth
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))


def solution(str_list, ex):
    x = list(ex)
    result = ""
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            result += str_list[i]
            
            
    
    return result

print(solution(["abc", "def", "ghi"],"ef"))
print(solution(["abc", "bbc", "cbc"],"c"))

# wth
def solution(str_list, ex):
    answer = ''
    for x in str_list:
        if ex in x: continue
        answer+=x
    return answer

def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))

def solution(str_list, ex):
    filtered_list = [s for s in str_list if ex not in s]
    return "".join(filtered_list)



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

# wth
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate) # how to use item
        


def solution(arr, idx):
    temp = []
    for i in range(idx, len(arr)):
        if (arr[i] >= arr[idx]) and (arr[i] == 1):
            temp.append(i)
            return int(min(temp))
        
    return -1
    
    # return 200

print("#1", solution([0, 0, 0, 1], 1))
print("#2", solution([1, 0, 0, 1, 0, 0], 4))
print("#3", solution([1, 1, 1, 1, 0], 3))

# wth
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer



def solution(number):
    res = 0
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    res = sum % 9
    
    return res

print(solution("123"))

# wth
def solution(number):
    return sum(map(int, number)) % 9



def solution(my_strings, parts):
    answer = ''


    for i in range(len(parts)):
        answer += my_strings[i][parts[i][0] : parts[i][1]+1] 

    return answer