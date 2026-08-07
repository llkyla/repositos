# 181848
def solution(n_str):
    
    return int(n_str)

# 181888
def solution(num_list, n):
    answer = []
    
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
        
    return answer

# 181843
def solution(my_string, target):
    
    return 1 if target in my_string else 0

# 181850
def solution(flo):
    
    return int(flo)

# 181889
def solution(num_list, n):
    
    return num_list[:n]

# 181841
def solution(str_list, ex):
    x = list(ex)
    result = ""
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            result += str_list[i]
    
    return result

# 181840
def solution(num_list, n):
    
    return 1 if (n in num_list) else 0

# 181845
def solution(n):
    
    return str(n)

# 181847
def solution(n_str):
    
    result = ''
    
    for i in range(0, len(n_str)):
        if n_str[i] != "0":
            result = n_str[i:]
            return result
        
    return result

# 181849
def solution(num_str):

    num_int = list(int(x) for x in num_str)
    sum_list = sum(num_int)
    
    return sum_list

# 181852
def solution(num_list):
    result = []
    num_list.sort()
    result = num_list[5:]

    return result

# 181853
def solution(num_list):
    result = []
    num_list.sort()
    result = num_list[:5]

    return result

# 181854
def solution(arr, n):
    
    if (len(arr) % 2 == 0):
        for i in range(1, len(arr), 2):
            arr[i] += n
        return arr
    
    else:
        for i in range(0, len(arr), 2):
            arr[i] += n
        return arr
    
# 181856
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
    
# 181861
def solution(arr):
    answer = []
    for x in arr:
        for i in range(1, x+1):
            answer.append(x)

    return answer

# 181863
def solution(rny_string):
    
    return rny_string.replace('m', 'rn') # replace m -> rn

# 181864
def solution(myString, pat):

    temp = ""
    temp2 = ""
    result = ""
    
    temp = myString.replace("A", "C")
    temp2 = temp.replace("B", "A")
    result = temp2.replace("C", "B")

    return 1 if (pat in result) else 0

# 181865
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
        
# 181867
def solution(myString):
    answer = []
    n = 0
    for i in range(len(myString)):
        if myString[i] == "x":
            answer.append(len(myString[n:i]))
            n = i+1

    answer.append(len(myString[n:]))   
    
    return answer

# 181868
def solution(my_string):

    return my_string.split()

# 181869
def solution(my_string):

    return my_string.split()

# 181870
def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if "ad" not in strArr[i]:
            answer.append(strArr[i])
    
    return answer

# 181873
def solution(my_string, alp):

    answer = ''

    if alp in my_string:
        answer = my_string.replace(alp, alp.upper())
        
    else:
        answer = my_string
    
    return answer

# 181874
def solution(myString):

    return myString.lower().replace("a", "A") 

# 181875
def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        
        else:
            answer.append(strArr[i].upper())

    return answer

# 181876
def solution(myString):

    return myString.lower()

# 181878
def solution(myString, pat):
    
    return 1 if ((pat.lower()) in (myString.lower())) else 0

# 181879
def solution(num_list):
    answer = 1
    if len(num_list) <= 10:
        for i in range(len(num_list)):
            answer *= num_list[i]
        return answer
    else:
        sum_ans = sum(num_list)
        return sum_ans
    
# 181882
def solution(arr):

    for i in range(len(arr)):
        if ((arr[i] >= 50) & (arr[i] % 2 == 0)):
            arr[i] = int(arr[i] / 2)
            

        elif ((arr[i] < 50) & (arr[i] % 2 != 0)):
            arr[i] = arr[i] * 2
            
    return arr

# 181884
def solution(numbers, n):
    
    for i in range(len(numbers)+1):

        if sum(numbers[:i]) > n:
        
            return sum(numbers[:i])
        
# 181886
def solution(names):
    answer = []
    
    for i in range(0, len(names), 5):
        answer.append(names[i])
        
    return answer

# 181887
def solution(num_list):
    even = 0
    odd = 0
    
    for i in range(0, len(num_list), 2):
        even += num_list[i]

    for j in range(1, len(num_list), 2):
        odd += num_list[j]

    return max(even, odd)

# 181891
def solution(num_list, n):
    
    return num_list[n:] + num_list[:n]

# 181895
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
            # print(res1)
        if i in range(y[0], y[1]+1):
            res2.append(arr[i])
            # print(res2)
    
    return res1 + res2

# 181898
def solution(arr, idx):
    temp = []
    for i in range(idx, len(arr)):
        if (arr[i] >= arr[idx]) and (arr[i] == 1):
            temp.append(i)
            return int(min(temp))
        
    return -1

# 181899
def solution(start_num, end_num):
    answer = []
    
    for x in range(start_num, end_num-1, -1):
        answer.append(x)
    
    return answer

# 181896
def solution(num_list):
    
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            return i

    return -1

# 181835
def solution(arr, k):
    if k % 2 != 0:
        for i in range(len(arr)):
            arr[i] *= k

    else:
        for i in range(len(arr)):
            arr[i] += k
    return arr