# for i in range(5):
#     print(i, number % 100)
#     answer += number % 100
#     number //= 100

# print(answer)


# def solution(my_string):
#     answer = ''
#     for i in range(1, len(my_string)+1):
#         answer += my_string[-i]
#     return answer

# print(solution("helio")



# 문자 반복 출력하기
def solution(my_string, n): # my_string = "hello"
    answer = ''
    for i in range(len(my_string)): # i \in [0, 5)
        for j in range(n): # j \in [0, 3)
            answer += my_string[i] # ans = ans + my_string[i]
    return answer                  # ans = 'hhh' -> 'hhheee' ... -> 'hhheeellllllooo'

print(solution("hello", 3))

# wth: 굳이 for loop nesting 안해도 n이 정수라 mult 가능
def solution(my_string, n):
    answer = ''
    for m in my_string:
        answer += (m * n)
    return answer



# 특정 문자 제거하기
def solution(my_string, letter):
    answer = ''
    for m in my_string:
        if m != letter:
            answer += m
    return answer

print(solution("BCBdbe", "B"))

# wth
def solution(my_string, letter):
    return my_string.replace(letter, '') # 제거라서 letter -> 공백 가능



def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4



def solution(n):
    answer = 0
    for i in range(0, n + 1, 2):
        print(i)
        answer += i
    return answer

print(solution(10))



def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

print(solution([1, 2, 3, 4, 5], 1, 3))



def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer



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



g = [1, 2, 3, 4, 5]
def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer



def solution(my_string):
    answer = my_string
    for m in my_string:
        if m in "aeiou":
            answer = answer.replace(m, "")
        
    return answer

print(solution("bus"))



def solution(my_string):
    answer = 0
    for m in my_string:
        if m.isdigit():
            answer += int(m)
    
    return answer

print(solution("aAb1B2cC34oOp"))



def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer

print(solution(["We", "are", "the", "world!"]))

# wth1
def solution(strlist):
    return list(len(str) for str in strlist)



def solution(sides):
    answer = 0
    sides.sort()
    if sides[-1] < (sides[0] + sides[1]):
        answer = 1
    else:
        answer = 2
    return answer

print(solution([1, 4, 3]))

# wth 1
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2



def solution(my_string):
    answer = ''
    for m in my_string:
        if m.islower():
            answer += m.upper()
        elif m.isupper():
            answer += m.lower()
    return answer

print(solution("cccCCC"))

# lol
def solution(my_string):
    return my_string.swapcase()

def solution(array):
    return [max(array), array.index(max(array))]

print(solution([1, 8, 3]))

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


def solution(n):
    answer = 0
    n = str(n)
    for m in n:
        answer += int(m)
    return answer

# wth

def solution(str1, str2):
    if str2 in str1:
        return 1
    else: 
        return 2
    
# wth
def solution(str1, str2):
    return 1 if str2 in str1 else 2

from math import sqrt

def solution(n):
    return 1 if sqrt(n).is_integer() else 2

def solution(n, t):
    for i in range(0, t):
        n *= 2
    return n

# wth
def solution(n, t):
    return n << t

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

print(solution(24))

def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer

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

print(solution([1, 2, 3, 4, 5]))

def solution(myString):
    return myString.upper()

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

def solution(my_string, n):
    return my_string[-n:]

def solution(arr, k):
    answer = []
    if k % 2 != 0:
        for a in arr:
            answer.append(a * k)

    else:
        for a in arr:
            answer.append(a + k)
    return answer

print(solution([1, 2, 3, 100, 99, 98], 3))

# wth

def solution(arr, k):

    if k%2==0:
        return [a+k for a in arr]
    else: 
        return [a*k for a in arr] 
    
def solution(arr, k):
    if k % 2 != 0:
        for i in range(len(arr)):
            arr[i] *= k

    else:
        for i in range(len(arr)):
            arr[i] += k
    return arr


def solution(num_list):
    
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            return i

    return -1

def solution(a, b):
    x = str(a) + str(b)
    y = 2 * a * b
    if int(x) < y:
        return y
    else:
        return int(x)
    
# wth
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

def solution(number, n, m):
    
    return 1 if ((number % n == 0) & (number % m == 0)) else 0

def solution(flo):
    
    return int(flo)

def solution(my_string, n):
    
    return my_string[:n]

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

def solution(my_string, target):
    
    return 1 if target in my_string else 0

def solution(num_list, n):
    
    return num_list[:n]

a = int(input())

if a % 2 == 0:
    print("%d is even"%a)
else:
    print("%d is odd"%a)

# wth
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")

def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b
    
def solution(array, n):
    count = 0
    for a in array:
        if a == n:
            count += 1
    return count

import statistics 

def solution(array):
    
    return statistics.median(array)

# real way
def solution(array):
    return sorted(array)[len(array) // 2]

n = int(input())

for i in range(1, n+1):
    print(i * '*')

def solution(hp):
    
    return (hp // 5) + ((hp % 5) // 3) + (((hp % 5) % 3) // 1)

def solution(rsp):
    result = ''
    dic = {'2':'0', '0':'5', '5':'2'}
    for x in rsp:
        result += dic[x]
    
    return result

def solution(num_list):
    
    mult = 1
    
    for x in num_list:
        mult *= x
    
    sq = sum(num_list) ** 2
    
    return 1 if (mult < sq) else 0

def solution(box, n):
    
    return ((box[0] // n) * (box[1] // n) * (box[2] // n))

def solution(my_string):
    answer = []
    for x in my_string:
        if x.isdigit():
            answer.append(int(x))
    answer.sort()
    return answer

def solution(order):
    result = 0
    for x in str(order):
        if (x == '3') or (x == '6') or (x == '9'):
            result += 1
    return result

def solution(cipher, code):
    
    answer = ''
    
    for i in range(code-1, len(cipher), code):

        answer += cipher[i]
    
    
    return answer

# wth
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

my_string = "hello"
num1 = 1
num2 = 2
x = my_string[num2]
print(my_string.replace(my_string[num2], my_string[num1]))
print(my_string.replace(my_string[num1], x))

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

def solution(num, k):
    num = str(num)
    for i in range(0, len(num)):
        if num[i] == str(k):
            return i+1
    return -1

# wth
def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1

def solution(my_string):

    char_list = list(my_string.lower())
    char_list.sort()
    result = "".join(char_list)
    return result

print(solution("Bcad"))

def solution(num_list, n):
    
    return 1 if (n in num_list) else 0

def solution(n):
    
    return str(n)

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

def solution(n_str):
    
    return int(n_str)

def solution(num_str):

    num_int = list(int(x) for x in num_str)
    sum_list = sum(num_int)
    
    return sum_list

print(solution("123456789"))

# wth
def solution(num_str):
    return sum([int(i) for i in num_str])

# wth
def solution(num_str):
    answer = 0
    for i in num_str:
        answer+=int(i)
    return answer

def solution(num_list):
    result = []
    num_list.sort()
    result = num_list[5:]
    return result

# wth
def solution(num_list):
    return sorted(num_list)[5:]

def solution(arr, n):
    
    if (len(arr) % 2 == 0):
        for i in range(1, len(arr), 2):
            arr[i] += n
        return arr
    else:
        for i in range(0, len(arr), 2):
            arr[i] += n
        return arr
    
def solution(arr1, arr2):
    answer = 0
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
        
    elif len(arr1) > len(arr2):
        return 1
    
    else:
        return -1
    
def solution(arr):
    answer = []
    for x in arr:
        for i in range(1, x+1):
            answer.append(x)
    return answer

print(solution([5, 1, 4]))

def solution(rny_string):
    
    return rny_string.replace('m', 'rn')

def solution(myString, pat):

    temp = ""
    temp2 = ""
    result = ""

    temp = myString.replace("A", "C")
    temp2 = temp.replace("B", "A")
    result = temp2.replace("C", "B")

    return 1 if (pat in result) else 0


print(solution("ABBAA","AABB"))


def solution(binomial):
    a = ""
    b = ""
    for i in range(len(binomial)):
        if binomial[i] == "+":
            a = int(binomial[:i-1])
            b = int(binomial[i+2:])
            return a + b
        elif binomial[i] == "-":
            a = int(binomial[:i-1])
            b = int(binomial[i+2:])
            return a - b
        elif binomial[i] == "*":
            a = int(binomial[:i-1])
            b = int(binomial[i+2:])
            return a * b
        
    
print(solution("43 + 12"))

# wth
def solution(binomial):
    a, op, b = binomial.split()

    a = int(a)
    b = int(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b

    return result

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
                                                                                                                                
print(solution("oxooxoxxox")) # Output: [1, 2, 1, 0, 1, 0]

def solution(my_string):

    return my_string.split()

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

def solution(my_string, alp):

    answer = ''

    if alp in my_string:
        answer = my_string.replace(alp, alp.upper())
        
    else:
        answer = my_string
    
    return answer

print(solution("programmers", "p"))

# wth
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

def solution(myString):

    str = myString.lower()
    
    for i in range(len(str)):
        if str[i] == "a":
            return str.replace("a", "A")

print(solution("abstract algebra"))
print(solution("PrOgRaMmErS"))
print(solution("aaaaa"))
print(solution("AAAAAAA"))

# wth
def solution(myString):

    return myString.lower().replace("a", "A") 

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

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i%2: answer.append(strArr[i].upper())
        else: answer.append(strArr[i].lower())
    return answer

def solution(myString):
    return myString.lower()

def solution(myString, pat):
    str = myString.lower()
    patt = pat.lower()
    return 1 if patt in str else 0

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

def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))

def solution(arr):

    for i in range(len(arr)):
        if ((arr[i] >= 50) & (arr[i] % 2 == 0)):
            arr[i] = int(arr[i] / 2)
            

        elif ((arr[i] < 50) & (arr[i] % 2 != 0)):
            arr[i] = arr[i] * 2
            
    return arr

print(solution([1, 2, 3, 100, 99, 98]))

# wth
def solution(arr):
    answer = []

    for item in arr:
        if item >= 50 and not item % 2:
            answer.append(item // 2)
        elif item < 50 and item % 2:
            answer.append(item * 2)
        else:
            answer.append(item)

    return answer # 걍 이건 뭘까 싶음 다른 방향?

def solution(numbers, n):
    answer = 0
    
    for i in range(len(numbers)):
        if sum(numbers[:i]) > n:
            s = sum(numbers[:i])
            return s # why it only works with certain input([34, 5, 71, 29, 100, 34], 123)


def solution(numbers, n):
    
    for i in range(len(numbers)+1):

        if sum(numbers[:i]) > n:
        
            return sum(numbers[:i]) # but this all work
    

print(solution([58, 44, 27, 10, 100], 139)) # wth


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

def solution(num_list, n):
    
    return num_list[n:] + num_list[:n]

print(solution([5, 2, 1, 7, 5], 3))

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

def solution(arr, intervals):
    res1 = []
    res2= []
    x = intervals[0]
    y = intervals[1] 
    # print(x[0])
    # print(x[1])
    for i in range(len(arr)):
        if i in range(x[0], x[1]+1):
            res1.append(arr[i])
            #print(res1)
        if i in range(y[0], y[1]+1):
            res2.append(arr[i])
            #print(res2)
        
    
    return res1 + res2

print(solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))

# wth
def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1]
    return answer

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

def solution(start_num, end_num):
    answer = []
    
    for x in range(start_num, end_num-1, -1):
        answer.append(x)
    
    return answer

# wth
def solution(start, end):
    return list(range(start,end-1,-1))

def solution(n, k):
    answer = []
    
    for x in range(k, n+1, k):
        answer.append(x)
    
    return answer

# wth
def solution(n, k):
    return list(i for i in range(k,n+1,k))

def solution(my_string, is_prefix):
    
    if my_string.startswith(is_prefix) == True:
        return 1
    else:
        return 0
    

print(solution("banana", "ban"))

def solution(my_string):
    temp = []
    res = []
    
    for i in range(len(my_string)-1, -1, -1):
        # print(my_string[i:])
        temp.append(my_string[i:])
    temp.sort()
    #print(temp)
    return temp

print(solution("banana"))

# wth
def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))


#########
def solution(my_strings, parts):
    answer = ''
    
    
    for i in range(len(parts)):
        for j in range(len(parts)):
            x = parts[i][j]
            print(i)
            print(j)
            print(x) 
    
    
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))

def solution(my_strings, parts):
    answer = ''


    for i in range(len(parts)):
        answer += my_strings[i][parts[i][0] : parts[i][1]+1] 

    return answer

#########


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

def solution(n):
    res = [n]
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res.append(n)

        
    return res


print(solution(10))



def solution(numLog):
    res = ''
    
    dic = {1:"w", -1:"s", 10:"d", -10:"a"}
    
    for i in range(1, len(numLog)):
        res += dic[numLog[i] - numLog[i-1]]


    return res






# def solution(numbers):
#     l1 = []
#     mult = 0
#     for x in numbers:
        
            
#     return 0

# print(solution([1, 2, -3, 4, -5]))