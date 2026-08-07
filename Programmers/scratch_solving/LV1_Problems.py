# ADD INT IN RANGE
def solution(a, b):
    answer = 0
    
    for i in range(min(a,b), max(a,b)+1, 1):
        answer += i
        
    
    return answer

# wth
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2


print(adder(3, 5))


# STR -> INT
def solution(s):
    
    return int(s)



# SUM OF DIVISORS
from math import sqrt

def solution(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
                  
	return sum(s)

# wth
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])



# 자릿수 더하기
def solution(n):
    
    ans = 0
    
    n = str(n)
    
    for i in range(len(n)):
        a = int(n[i])
        ans += a

    return ans

# wth
def sum_digit(number):
    return sum(map(int, str(number)))



def solution(n):
    answer = []
    n = str(n)
    for i in range(1, len(n)+1):
        
        answer += n[-i]
    
    return list(map(int, answer)) # answer을 모두 int()로

# wth
def digit_reverse(n):
    return list(map(int, reversed(str(n)))) # reversed(str(n))을 모두 int()로



def solution(n):
    ans = 0
    
    l = list(map(int, str(n)))
    l.sort(reverse=True)
    
    for x in l:
        ans = ans * 10 + x
    
    return ans

# wth
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))



def solution(n):
    
    m = n ** (1/2)
    
    if ((m * 10) % 10) == 0: 
        return int((m + 1) ** 2)
    
    else:
        return -1
    
print(solution(121))

# wth
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'


def solution(num):
    
    return "Even" if (num % 2 == 0) else "Odd"


def solution(arr):
    
    return (sum(arr) / len(arr))

def solution(x):
    temp = 0
    y = str(x)
    
    for i in range(len(y)):
        z = int(y[i])
        temp += z
        
    if x % temp == 0:
        return True
    else:
        return False
    
print(solution(10))

def solution(x, n):
    ans = []
    a = 0
    while a < n:
        ans.append(x)
        a += 1
        x += x
        if a == n:
            break
    
    return ans

print(solution(2, 5))

def solution1(x, n):
    ans = []
    a = 1
    while a < (n + 1): # iterate 할 범위
        ans.append(x*a)
        a += 1
        if a == (n + 1):
            break
    
    return ans

print(solution1(2, 5))

# wth
def solution1(x, n):
    return [i * x + x for i in range(n)]


def solution(n):

    d = []
    
    for i in range(1, int((n - 1) ** 0.5)+1):
        if ((n - 1) % i) == 0:
            d.append(i)
            if ((i ** 2) != (n - 1)):
                d.append((n-1) // i)
                
    d.remove(1)
    
    return min(d)

# wth
def solution(n):
    i = 2
    while (n-1)%i: i += 1

    return i

# wth
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]

def solution(s):
    answer = True
    
    t = s.lower()
    
    p = t.count('p')
    y = t.count('y')
    
    if p == y:
        return True
    else:
        return False
    
print(solution("vbksjvbdskj"))
print(solution("pppyYy"))


def solution(numbers):
    
    numl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    miss = []
    
    for n in numl:
        if n not in numbers:
            miss.append(n)
            
    return sum(miss)

print(solution([1,2,3,4,6,7,8,0]))

# wth
def solution(numbers):
    return 45 - sum(numbers)

# wth
solution = lambda x: sum(range(10)) - sum(x)

def solution(arr, divisor):
    ans = []
    
    for a in arr:
        if a % divisor == 0:
            ans.append(a)
            ans.sort()
    
    if len(ans) == 0:
        return [-1]
    else:
        return ans
    
# wth
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

def solution(seoul):
    x = seoul.index("Kim")
    return "김서방은 {0}에 있다".format(x) # wth "김서방은 {}에 있다".format(seoul.index('Kim'))

def solution(arr):
    if len(arr) <= 1:
        return [-1]
        
    arr.remove(min(arr))
    return arr

# wth 뭐는 저장이고 뭐는 modify인지

def solution(num):
    count = 0
    
    while num != 1:

        if count == 500:
            return -1
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        count += 1
            
    return count

# wth
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1


def solution(phone_number):
     return "*" * (len(phone_number) - 4) + phone_number[-4:] # wth


def solution(absolutes, signs):
    
    ans = 0
    
    for i in range(len(signs)):
        if signs[i] == False:
            ans -= absolutes[i]
        else:
            ans += absolutes[i]

    return ans

def solution(a, b):
    
    res = 0

    for i in range(len(a)):
        res += a[i]*b[i]
        
    return res

print(solution([1,2,3,4],[-3,-1,0,2]))

# wth
solution = lambda x, y: sum(a*b for a, b in zip(x, y)) # : 뒤가 반환값 
# zip(x,y)는 두 리스트를 같은 인덱스끼리 튜플로
'''
x = [1, 2, 3, 4]
y = [-3, -1, 0, 2]
list(zip(x, y))
# [(1, -3), (2, -1), (3, 0), (4, 2)]
'''

def solution(s):
    
    if len(s) % 2 != 0:
        return s[int((len(s) / 2))]
    else:
        return s[int((len(s) / 2) - 1)] + s[int((len(s) / 2))]
    
# wth
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

def solution(n):
    a = 0
    ans = ""
    while a < n:
        if a % 2 == 0:
            ans = ans + "수"
        else:
            ans = ans + "박"
        a += 1
        
    
    return ans

# wth
def water_melon(n):
    
    str = "수박"*n
    return str[:n]

def solution(left, right):
    ans = 0
    
    for i in range(left, right+1):
        temp = []

        for j in range(1, (int(i**0.5) +1)):
            if i % j == 0: # j가 i를 나누어 떨어지게 하면 j는 i의 약수
                temp.append(j)
                if j != (i // j): # j와 짝을 이루는 약수(i//j)가 j와 다른 값이면
                                  # = i가 완전제곱수가 아니어서 j가 자기 자신과 짝이 아니라면
                    temp.append(i // j)

        if len(temp) % 2 == 0:
            ans += i
        else:
            ans -= i
    return ans


print(solution(13, 17))


# wth
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


def solution(s):
    ans = ''.join(sorted(s, reverse=True))
    
    return ans

print(solution("Zbcdefg"))

# wth more
s = "dBaCzA"
result = sorted(s, key=lambda c: (c.isupper(), -ord(c) if c.isupper() else ord(c)))
print(''.join(result))
# 소문자(a, d, z)는 오름차순으로 앞: a, d, z
# 대문자(A, B, C)는 내림차순으로 뒤: C, B, A
# 최종 결과: "adzCBA"

def solution(price, money, count):
    tot = 0 

    for i in range(1, (count+1)):
        tot += price * i
    
    if tot > money:
        return tot - money
    else:
        return 0

print(solution(3, 20, 4))

# wth 등차수열, 등비수열의 합 공식
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

def solution(s):
    
    if (len(s) == 4) or (len(s) == 6):
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
         return False   
    
# wth
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]

def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[i])): # 현재 row의 col만큼 반복
            row.append(arr1[i][j] + arr2[i][j])
        ans.append(row)
    return ans

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# wth
def sumMatrix(arr1,arr2):
    # zip(A, B): A와 B의 같은 행끼리 짝지어 (A의 행, B의 행) 튜플로 묶음
    # x는 그 튜플, 예: x = ([1,2], [3,4])
    
    # zip(*x): x를 다시 풀어서(*로 unpacking) zip(A의 행, B의 행)을 실행
    # 즉 같은 열 위치의 원소끼리 (1,3), (2,4)처럼 짝지음
    
    # map(sum, ...): 각 짝지어진 튜플 (1,3), (2,4)에 sum()을 적용해 1+3=4, 2+4=6 계산
    
    # list(...): map 결과를 리스트로 변환
    
    # 바깥 for x in zip(A,B): 모든 행에 대해 위 과정을 반복 → 리스트 컴프리헨션으로 감쌈
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]
            # zip(*x)  ==  zip([1,2], [3,4])  ==  [(1,3), (2,4)]  # (같은 열 위치끼리 짝지음)

a, b = map(int, input().strip().split(' '))
# "  3 5  ".strip()  # "3 5" (양쪽 공백만 제거, 중간 공백은 남음)
# 문자열을 지정한 구분자를 기준으로 잘라서 리스트로 ex)' '을 기준으로 나눔
# "3 5".split(' ')  # ['3', '5']  ← 아직 문자열 리스트임에 주의
for i in range(1, b+1):
    print('*' * a)

# wth
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

def solution(arr):
    ans = []
    for i in range(len(arr)):
        if (i == 0) or arr[i] != arr[i-1]:
            ans.append(arr[i])

    return ans

def solution(n, m): # wth 유클리드 호제법
    a, b = n, m
    while b != 0:
        a, b = b, (a % b)
    gcd = a
    lcm = (n * m) // gcd
    
    return [gcd, lcm]

def solution(t, p):
    count = 0
    
    for i in range(len(t)):
        temp = t[i:len(p)+i]
        if len(temp) < len(p):
            break
        print(temp)

        if int(temp) <= int(p):
            count += 1
        else:
            count += 0
    
    return count

print(solution("3141592", "271"))
print(solution("500220839878", "7"))

# wth
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer

# wth 그리디(탐욕) 알고리즘
def solution(d, budget):
    d.sort()
    tot = 0
    ans = 0
    
    for a in d:
        tot += a
        if tot <= budget:
            ans += 1
        else:
            break
    return ans

# wth
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

# wth
def solution(number):
    ans = 0
    
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                # i<j<k 순서로 서로 다른 세 인덱스를 뽑음 (중복 조합 방지)
                if number[i] + number[j] + number[k] == 0:
                    ans += 1
    
    return ans

# wth
from itertools import combinations

def solution(number):
    answer = 0
    for combo in combinations(number, 3):  # number에서 3개씩 뽑는 모든 조합 생성
        if sum(combo) == 0: # 세 수의 합이 0이면
            answer += 1  # 카운트 증가
    return answer

# wth
def solution(s):
    ans = ''
    i = 0
    
    for a in s:
        if a == " ": # 공백을 만나면 다음 단어에서 다시 짝수번째부터 시작하도록 초기화
            ans += a
            i = 0
        else:
            if i % 2 == 0:
                ans += a.upper()
            else:
                ans += a.lower()
            i += 1
                
    return ans

# wth
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

def solution(n):
    
    tri = ''
    
    while n > 0:
        tri += str(n % 3)
        print(tri)
        n = n // 3
    
    return int(tri, 3) #내장함수 wth

print(solution(45))

def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        small = min(w, h) # 현재 명함에서 더 작은 변을 구함 (회전 후 가로가 될 후보)
        large = max(w, h) # 현재 명함에서 더 큰 변을 구함 (회전 후 세로가 될 후보)
        max_w = max(max_w, small)  # 지금까지 나온 작은 변들 중 최댓값을 계속 갱신
        max_h = max(max_h, large)  # 지금까지 나온 큰 변들 중 최댓값을 계속 갱신
        
    return max_w * max_h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

# wth
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

from itertools import chain
data = [[60, 50], [30, 70], [60, 30], [80, 40]]
flat = list(chain.from_iterable(data))
print(flat)  # [60, 50, 30, 70, 60, 30, 80, 40]

data = [[60, 50], [30, 70], [60, 30], [80, 40]]
flat = [num for row in data for num in row]
print(flat)  # [60, 50, 30, 70, 60, 30, 80, 40]

# 일반 for문
numbers = []
for x in range(1, 6):
    numbers.append(x)
print(numbers)  # [1, 2, 3, 4, 5]

# 리스트 컴프리헨션
numbers = [x for x in range(1, 6)]
print(numbers)  # [1, 2, 3, 4, 5]

# 일반 for문
squared = []
for x in [1, 2, 3, 4, 5]:
    squared.append(x * 2)
print(squared)  # [2, 4, 6, 8, 10]

# 리스트 컴프리헨션
squared = [x * 2 for x in [1, 2, 3, 4, 5]]
print(squared)  # [2, 4, 6, 8, 10]

data = [[60, 50], [30, 70], [60, 30], [80, 40]]

# 일반 이중 for문
flat = []
for row in data:        # 1단계: data에서 작은 리스트(row)를 하나씩 꺼냄
    for num in row:      # 2단계: 그 작은 리스트(row) 안의 숫자(num)를 하나씩 꺼냄
        flat.append(num)  # 꺼낸 숫자를 flat에 추가
print(flat)

# 리스트 컴프리헨션
flat = [num for row in data for num in row]
print(flat)

# wth
def solution(s):
    answer = []

    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            for j in range(i-1, -1, -1): # 바로 앞부터 거꾸로 훑으며 가장 가까운 같은 글자를 찾음
                if s[j] == s[i]:
                    answer.append(i - j) # 현재 위치와의 거리 계산
                    break
    
    return answer

# wth
def solution(s, n):
    answer = ''
    
    for c in s:
        if c == " ":
            answer += c
        elif c.isupper():
            answer += chr((ord(c) - ord("A") + n) % 26 + ord("A")) 
            # (ord(c) - ord("A"): 현재 c가 A로부터 얼마나 떨어져있는지 계산 A=0 .. Z=25
            # + n: 그 위치에서 n만큼 이동
            # % 26: 25를 넘으면 다시 0부터 시작하도록 순환 처리 Z->A
            # + ord("A"): 계산된 위치값을 다시 아스키코드로 변환
            # chr: 아스키코드를 실제 문자로 변환해 추가

            # ord는 아스키코드 참고해서 문자를 숫자로
            # chr는 그 숫자를 아스키코드 참고해서 문자로
        else:
            answer += chr((ord(c) - ord("a") + n) % 26 + ord("a"))
    
    return answer

# wth 잘 생각해보기
def solution(numbers):
    res = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp = numbers[i] + numbers[j]
            if tmp not in res:
                res.append(tmp)

    return sorted(res)

# i를 뽑고 i 다음의 인덱스의 j를 뽑고 tmp에 i+j를 저장하는데
# 이 tmp가 res에 없으면 append = 중복값을 허하지 않노라
# return은 오름차순으로 

# wth
def solution(food):
    left = ''
    for i in range(1, len(food)):
        count = food[i] // 2
        left += str(i) * count
    
    return left + "0" + left[::-1] # :: 아직도 헷갈림 [start:end:step] [::-1] = 시작부터 끝까지 역순으로

def solution(strings, n):
    answer = []
    tmp = []
    for s in strings:
        
        print(s[n])
    
    return answer

print(solution(["sun", "bed", "car"], 1))

# wth
def solution(strings, n):

    return sorted(strings, key=lambda s: (s[n], s))
    # key = : the key you want to sort
    # key=lambda: 정렬기준을 직접 만들때 씀
    # key는 sorted에게 이 함수가 계산해주는 값을 정렬하라, 함
    # key=lambda s:(s[n], s): s 하나 받으면 (s[n], s)라는 튜플을 반환해라
    # 각 문자열 s마다 (n번째 문자, 전체)를 만들어 비교 기준으로 삼음
    # 왜 튜플: python에서 튜플끼리 비교할 때 첫번째 요소 비교 후 같으면 두번째 비교함
    # sorted(strings, key=lambda s: (s[n], s)) <- 여기에서 리턴이 튜플은 아님 비교만 함
    # 정렬 알고리즘이 두 원소를 비교할 때 참고할 값을 만들어주는 것뿐

data = ["abce", "abcd", "cdx"]
sorted(data, key=lambda s: (s[2], s))

# 오름차순 lambda x: x
# 내림차순 lambda x: -x
# 문자열 길이순 lambda x: len(x)
# 길이순, 동점이면 사전순 lambda x: (len(x), x)
# 대소문자 무시정렬 lambda w: w.lower()

def solution(array, commands):
    ans = []
    
    for i, j, k in commands:
        sliced = array[i-1:j]
        sliced.sort()
        ans.append(sliced[k-1])
    
    return ans

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# wth
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# wth hahahahahaha DICT
def solution(s):
    answer = 0
    
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", 
           "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for key, val in dic.items():
        s = s.replace(key, val)
    
    
    return int(s)

def solution(a, b, n):
    tot = 0
    empty = n

    while empty >= a:
        get = (empty // a) * b # 교환 가능한 횟수만큼 받는 콜라 수
        tot += get
        empty = empty % a + get # 교환하고 남은 빈 병 + 새로 받은 콜라(다 마시면 빈 병이 됨)
    
    return tot

# wth heapq 쓰는 방법
import heapq

def solution(k, score):
    ans = []
    hall = [] # 명예의 전당 목록 (최소 힙)
    
    for s in score:
        heapq.heappush(hall, s) # 매일 새로 들어온 점수 s를 힙에 추가
                                # 이 시점에서 hall은 항상 최소 힙 상태를 유지하므로
                                # 가장 작은 값이 자동으로 hall[0]에 위치
        
        if len(hall) > k: # k명을 초과하면
            heapq.heappop(hall) # 가장 낮은 점수를 제거 (힙에서 자동으로 최솟값 제거)
            
        ans.append(hall[0]) # 현재 힙에서 가장 작은 값이 곧 발표 점수
        
    return ans

'''
heapq.heappush(heap, item): 힙에 새 원소를 추가
                            그냥 리스트에 append하는 게 아니라
                            힙의 구조(가장 작은 값이 맨 앞에 오도록)를 유지하면서 알맞은 위치에 삽입
                            시간복잡도 = O(log n)

heapq.heappop(heap): 힙에서 가장 작은 값을 꺼내면서 동시에 제거
                     남은 원소들도 힙 구조를 유지하도록 재정렬
                     시간복잡도 = O(log n)                         

'''

# wth 
def solution(k, score):

    q = []
    answer = []

    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q)) # 그냥 min으로 써도 되네
        answer.append(min(q))

    return answer

# wth
def solution(N, stages):
    fail_rate = {} # key= stageNum; val=실패율
    tot_users = len(stages)

    for stage in range(1, N+1):
        stuck = stages.count(stage) # stage의 숫자가 몇 개 인가 = stage에 도달했으나 멈춰있는 수
        if tot_users == 0: # 도달 못하면 끝이고
            fail_rate[stage] = 0 
        else: # 유저가 남아있다면 = 다음 stage에 도달을 했다면
            fail_rate[stage] = stuck / tot_users # 실패율 계산하기
        tot_users -= stuck # stage 통과자만 다음 계산에 포함

    ans = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True) # wth?
    return ans


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# wth
def solution(cards1, cards2, goal):
    i, j = 0, 0 # cards1, cards2에서 다음에 사용할 카드의 idx

    for word in goal: 
        if i < len(cards1) and cards1[i] == word: 
            i += 1 # 맨 앞부터 cards1의 카드 사용, goal의 요소에 있다면 i를 늘림
        elif j < len(cards2) and cards2[j] == word:
            j += 1 # 맨 앞부터 cards2의 카드 사용, goal의 요소에 있다면 j를 늘림
        else:
            return "No" # 없다면 No
    
    return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
# wth
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

# wth
def solution(name, yearning, photo):
    
    dic = dict(zip(name, yearning))
    ans = []

    for pic in photo:
        score = 0
        for person in pic:
            score += dic.get(person, 0) # dic에 person이 있으면 점수, 없으면 0반환 

        ans.append(score)

    return ans

# wth
def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

# wth
def solution(nums):
    n = len(nums) # tot pokemon
    take = n // 2
    kind = len(set(nums)) # 존재하는 폰켓몬 종류 수

    return min(take, kind)

# wth
def solution(number, limit, power):
    divisor_count = [0] * (number + 1)
    # idx0부터number까지 리스트를 만들고 모두 0으로 초기화
    # divisor_count[i] = i의 약수 개수 저장
    
    # j를 1부터 number까지 하나씩 확인(약수후보확인)
    for j in range(1, number+1):
        # j의 배수들(j, 2j, 3j, ...)을 number까지 하나씩 확인
        # ex) j=3이면 3, 6, 9, 12... 를 차례로 multiple에 담음
        for multiple in range(j, number+1, j):
            # multiple은 j를 약수로 가진다는 뜻 = multiple 위치의 약수 개수를 1 증가
            divisor_count[multiple] += 1
        
    tot = 0 # 철 무게

    # 1번 기사부터 number번 기사까지 하나씩 확인
    for i in range(1, number+1):
        if divisor_count[i] > limit:
            tot += power # 협약기관에서 정한 power 값을 공격력으로 사용해서 더함
        else:
            tot += divisor_count[i] # 제한수치 이하이면 원래 약수 개수를 그대로 공격력으로 사용해서 더함
    
    return tot

# wth 에라토네스 체
def cf(n): # 공약수 출력
    a = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i) <= limit else power for i in range(1,number+1)])

# wth
import datetime

def solution(a, b):
    day = datetime.date(2016, a, b) # 2016년 a월 b일이라는 날짜 객체 생성
    
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"] # weekday() 순서에 맞춘 요일 이름
    
    return days[day.weekday()] # 해당 날짜의 요일 인덱스를 찾아 이름으로 변환

def solution(a, b):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2016년은 윤년이라 2월=29일
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]  # 1월 1일=금요일 기준

    total_days = sum(days_in_month[:a-1]) + b - 1  # 1월 1일부터 며칠이 지났는지 계산
    return week[total_days % 7]

# 17681
def solution(n, arr1, arr2):
    res = []
    
    for i in range (n):
        b1 = bin(arr1[i])[2:].zfill(n)
        b2 = bin(arr2[i])[2:].zfill(n)

        tmp = ''

        for j in range(n):
            if b1[j] == '1' or b2[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        res.append(tmp)

    return res

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))

# wth
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

def solution(answers):
    res = []
    
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5] 
    n3 = [3,3,1,1,2,2,4,4,5,5] 
    
    score = [0,0,0]
    
    for i, answer in enumerate(answers):
        if answer == n1[i % len(n1)]:
            score[0] += 1
        if answer == n2[i % len(n2)]:
            score[1] += 1
        if answer == n3[i % len(n3)]:
            score[2] += 1
            
    max_n = max(score)
    for j, s in enumerate(score):
        print(j,s)

    return list((j + 1) for j, s in enumerate(score) if s == max_n)

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([4,4,2,4,2]))

# 그리디 wth
def solution(n, m, section):
    answer = 0 # 롤러로 페인트칠한 횟수(정답)
    painted_until = 0    
        # 지금까지 페인트가 칠해진 마지막 구역 번호 (시작 = 0)
    for s in section:
            # section은 이미 오름차순으로 정렬되어 주어짐 (문제 제한사항)
            # 왼쪽부터 순서대로 "칠해야 할 구역"을 하나씩 확인
        if s > painted_until:
                # 현재 구역 s가 아직 칠해지지 않은 곳이라면
                # (painted_until 이하이면 이미 이전 페인트칠로 커버된 상태이므로 건너뜀)
            painted_until = s + m - 1
                # 지금 이 구역(s)부터 롤러를 대고 오른쪽으로 칠한다고 가정
                # 롤러 길이가 m이므로, s부터 시작해 s, s+1, ..., s+m-1까지 칠해짐
                # 즉 새로 칠해진 마지막 구역 번호를 갱신
            answer += 1
                # 롤러로 한 번 칠했으므로 횟수 1 증가

    return answer

# wth
def solution(n, m, section):
    # n=8, m=4, section=[2,3,6] 을 넣고 실행한다고 가정
    answer = 0
    # answer = 0  ← 아직 아무 곳도 칠하지 않았으니 횟수 0으로 시작
    painted_until = 0
    # painted_until = 0  ← 지금까지 칠해진 마지막 구역 번호, 아직 없으니 0

    for s in section:
        # section = [2, 3, 6] 이므로 s는 순서대로 2 → 3 → 6이 됨

        # ── 1번째 반복: s = 2 ──
        # 현재 상태: painted_until = 0
        if s > painted_until:
            # 2 > 0 → True (아직 칠해지지 않은 구역이므로 새로 칠해야 함)
            painted_until = s + m - 1 # (] thus -1
            # painted_until = 2 + 4 - 1 = 5
            # → 2번부터 롤러(길이4)를 대면 2,3,4,5번까지 칠해짐
            # painted_until 값이 0 → 5로 바뀜
            answer += 1
            # answer = 0 + 1 = 1
            # → 첫 번째 페인트칠 완료, 횟수 1로 증가

        # ── 2번째 반복: s = 3 ──
        # 현재 상태: painted_until = 5, answer = 1
        if s > painted_until:
            # 3 > 5 → False
            # → 3번은 이미 아까 칠한 범위(2~5)에 포함되어 있으므로 아무것도 안 함
            # painted_until, answer 모두 변화 없음 (그대로 5, 1)
            pass

        # ── 3번째 반복: s = 6 ──
        # 현재 상태: painted_until = 5, answer = 1
        if s > painted_until:
            # 6 > 5 → True (아직 칠해지지 않은 구역이므로 새로 칠해야 함)

            painted_until = s + m - 1
            # painted_until = 6 + 4 - 1 = 9
            # → 6번부터 롤러(길이4)를 대면 6,7,8,9번까지 칠해짐(9번은 벽 밖이지만 계산상 상관없음)
            # painted_until 값이 5 → 9로 바뀜

            answer += 1
            # answer = 1 + 1 = 2
            # → 두 번째 페인트칠 완료, 횟수 2로 증가

    return answer
    # for문이 section의 원소를 모두 순회했으므로 반복 종료
    # 최종적으로 answer = 2 를 반환

def solution(wallet, bill):
    res = 0
    
    while (min(bill) > min(wallet)) or (max(bill) > max(wallet)):
        if bill[0] > bill[1]:
            bill[0] = int(bill[0] // 2)
        else:
            bill[1] = int(bill[1] // 2)
        res += 1
     
    return res  

print(solution([30, 15],[26, 17]))

# wth 코드의 형태 알고리즘
'''
1. 지폐를 접은 횟수를 저장할 정수 변수 answer를 만들고 0을 저장합니다.
2. 반복문을 이용해 bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 큰 동안 아래 과정을 반복합니다.
    2-1. bill[0]이 bill[1]보다 크다면
        bill[0]을 2로 나누고 나머지는 버립니다.
    2-2. 그렇지 않다면
        bill[1]을 2로 나누고 나머지는 버립니다.
    2-3. answer을 1 증가시킵니다.
3. answer을 return합니다.
'''
# wth 1107
def solution(babbling):
    sounds = {"aya": "1", "ye": "2", "woo": "3", "ma": "4"}
    count = 0

    for word in babbling:
        temp = word
        for sound, code in sounds.items():
            temp = temp.replace(sound, code) # word 안의 각 발음을 해당 숫자 문자로 전부 치환
        # temp는 "12" 처럼 발음이 성공적으로 매칭됐다면 숫자로만 구성됨
        if temp.isdigit(): # 발음이 아닌 글자가 하나도 안 남았다는 뜻 (모두 매칭됨)
            has_consecutive = False
            for i in range(len(temp) - 1):
                if temp[i] == temp[i+1]: # 같은 숫자(=같은 발음)가 연속되면 위반
                    has_consecutive = True
                    break
            
            if not has_consecutive:
                count += 1

    return count

# wth
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer

# wth 그리디
def solution(k, m, score):
    score.sort(reverse=True)
    total = 0

    for i in range(m - 1, len(score), m): # m-1부터 시작하는 이유:
                                          # 인덱스가 0부터 시작하는 m개 묶음의 마지막 자리가 m-1
                                         
        print(score)
        # m-1번째, 2m-1번째, 3m-1번째, ... 인덱스를 확인
        # 정렬된 상태에서 각 상자의 "가장 낮은 점수(=끝 원소)" 위치를 순서대로 짚음

        total += score[i] * m
        # 그 상자의 가격(최저점수 × m)을 누적

    return total
    # 남는 사과(마지막에 m개가 안 되는 부분)는 자연스럽게 range에서 제외되어 버려짐

print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))

# wth
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

# wth 에라토스테네스의 체
def solution(n):
    is_prime = [True] * (n + 1)
    # 0부터 n까지, 처음엔 모두 소수라고 가정 (True)
    # 인덱스를 숫자 그대로 쓰기 위해 크기를 n+1로 잡음

    is_prime[0] = is_prime[1] = False
    # 0과 1은 소수가 아니므로 미리 False로 처리

    for i in range(2, int(n ** 0.5) + 1):
        # 2부터 √n까지만 확인하면 충분함 (그 이상의 배수는 이미 작은 수에서 걸러짐)

        if is_prime[i]:
            # i가 아직 소수로 남아있다면 (아직 지워지지 않았다면)

            for j in range(i * i, n + 1, i):
                # i의 배수들을 i*i부터 시작해서 i씩 건너뛰며 모두 False로 지움
                is_prime[j] = False

    return sum(is_prime)
    # True로 남은 개수(=소수 개수)를 합산해서 반환

# wth
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# wth 완전탐색
from itertools import combinations

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def solution(nums):
    answer = 0

    for combo in combinations(nums, 3):
        if is_prime(sum(combo)):
            answer += 1

    return answer

# itertools 없이 완전탐색:def solution(nums):
def solution(nums):
    answer = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # i < j < k 순서로 인덱스를 잡아 서로 다른 3개를 뽑음
                # (예: i=0,j=1,k=2 / i=0,j=1,k=3 ... 처럼 중복 없이 모든 조합을 만듦)

                total = nums[i] + nums[j] + nums[k]
                # 뽑은 3개의 합 계산

                if total < 2:
                    continue
                    # 1 이하는 소수가 아니므로 바로 다음 조합으로 넘어감

                is_prime = True
                # 일단 소수라고 가정

                for d in range(2, int(total ** 0.5) + 1):
                    # 2부터 √total까지 나눠보며 약수가 있는지 확인
                    if total % d == 0:
                        is_prime = False
                        break

                if is_prime:
                    answer += 1

    return answer

#wth ord
def solution(s, skip, index):
    alphabet = list(chr(i) for i in range(97, 123))
    avail = list(c for c in alphabet if c not in skip)

    ans = ''

    for ch in s:
        loc = avail.index(ch) # 원래 문자가 available 리스트에서 몇 번째 위치인지 찾음
        new_loc = (loc + index) % len(avail) # index만큼 뒤로 이동, len(available)을 넘으면 처음(a)으로 순환
        ans += avail[new_loc]

    return ans

# wth
def solution(board, h, w):
    n = len(board)
    count = 0
    color = board[h][w]
    # 기준 칸의 색깔을 미리 변수에 저장

    if h > 0:
        # 위쪽 칸이 보드 안에 있는지 (h가 0이면 위쪽은 존재하지 않음)
        if board[h-1][w] == color:
            count += 1

    if h < n - 1:
        # 아래쪽 칸이 보드 안에 있는지 (h가 마지막 줄이면 아래쪽은 없음)
        if board[h+1][w] == color:
            count += 1

    if w > 0:
        # 왼쪽 칸이 보드 안에 있는지
        if board[h][w-1] == color:
            count += 1

    if w < n - 1:
        # 오른쪽 칸이 보드 안에 있는지
        if board[h][w+1] == color:
            count += 1

    return count

# ^wth
def solution(board, h, w):
    n = len(board)
    count = 0

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count

# wth
def solution(s):
    answer = 0
    while s:
        x = s[0]
        same = 0
        diff = 0
        cut = 0
        for i in range(len(s)):
            if s[i] == x:
                same += 1
            else:
                diff += 1
            
            if same == diff:
                # 두 횟수가 같아지는 순간 발견
                cut = i + 1
                # 여기까지(i번째 포함) 잘라야 하므로 +1
                break
        else:
            # for문이 break 없이 끝까지 다 돌았다면
            # (=끝까지 가도 두 횟수가 같아지지 않은 경우)
            cut = len(s)
            # 남은 문자열 전체가 마지막 조각이 됨
        
        answer += 1
        # 조각 하나를 분리했으므로 개수 1 증가
        
        s = s[cut:]
        # 분리한 부분을 제외한 나머지로 s를 갱신
    
    return answer

# wth
from collections import deque

def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans

# wth dic
def solution(lottos, win_nums):
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    
    count = 0
    max_cnt = 0
    
    for l in lottos:
        if l in win_nums:
            count += 1
        if l == 0:
            max_cnt += 1
    
    max_sc = max_cnt + count
    min_sc = count
    
    rank_max = dic.get(max_sc, 6)
    rank_min = dic.get(min_sc, 6)
    
    answer = [rank_max, rank_min]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# wth
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# wth dic
def solution(keymap, targets):
    cost = {} # 각 문자를 입력하는 데 필요한 최소 누름 횟수를 저장할 딕셔너리

    for key in keymap:
        for i, ch in enumerate(key): # 키 안에서 문자의 위치(0부터 시작)를 순서대로 확인
            presses = i + 1 # 실제 누르는 횟수는 위치+1 (0번째 위치=1번 누름)

            if ch not in cost or presses < cost[ch]: # 이 문자가 처음 나왔거나, 더 적은 횟수로 입력 가능하다면 갱신
                cost[ch] = presses

    answer = []
    for target in targets:
        total = 0
        possible = True

        for ch in target:
            if ch not in cost: # 이 문자를 아예 입력할 수 없는 키가 없다면
                possible = False
                break
            total += cost[ch]

        answer.append(total if possible else -1)

    return answer

# wth 다트
def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    scores = []
    i = 0
    n = len(dartResult)

    while i < n:
        # 1. 숫자 부분 읽기 (한 자리 또는 두 자리, "10"만 두 자리)
        if dartResult[i:i+2] == '10':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1

        # 2. 보너스(S/D/T) 읽기
        b = dartResult[i]
        i += 1
        score = num ** bonus[b]

        # 3. 옵션(* 또는 #)이 있는지 확인
        if i < n and dartResult[i] in ('*', '#'):
            opt = dartResult[i]
            i += 1
            if opt == '*':
                score *= 2
                if len(scores) >= 1:
                    scores[-1] *= 2
            elif opt == '#':
                score *= -1

        scores.append(score)

    return sum(scores)

# wth re
import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    # 보너스 문자를 제곱 지수로 매핑 (Single=1제곱, Double=2제곱, Triple=3제곱)

    parts = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    # 정규표현식으로 "숫자 + S/D/T + (옵션이 있으면 */#)" 패턴을 모두 뽑아냄
    # 예: "1S2D*3T" → [('1','S',''), ('2','D','*'), ('3','T','')]

    scores = []
    # 각 기회의 최종 점수를 저장할 리스트

    for num, b, opt in parts:
        score = int(num) ** bonus[b]
        # 점수를 보너스에 맞게 거듭제곱 (예: 2에 D면 2**2=4)

        if opt == '*':
            score *= 2
            # 이번 점수를 2배로 만듦
            if len(scores) >= 1:
                scores[-1] *= 2
                # 바로 전 점수도 2배로 만듦 (전 점수가 있을 때만)

        elif opt == '#':
            score *= -1
            # 이번 점수만 마이너스로 만듦

        scores.append(score)
        # 계산이 끝난 이번 점수를 리스트에 추가

    return sum(scores)
    # 세 기회의 점수를 모두 더해서 반환

# wth dic
def solution(participant, completion):
    count = {}

    for p in participant:
        count[p] = count.get(p, 0) + 1
        # 참가자 이름이 나올 때마다 개수를 1씩 늘림

    for c in completion:
        count[c] -= 1
        # 완주자 이름이 나올 때마다 개수를 1씩 줄임

    for name, cnt in count.items():
        if cnt > 0:
            # 참가자 수보다 완주자 수가 적게 차감된 이름 = 완주 못한 사람
            return name
        
# wth collection
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# wth 그리디
def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    both = lost_set & reserve_set
    # 도난당했지만 여벌도 가진 학생 (자기 걸로 자기가 입음)

    lost_set -= both
    reserve_set -= both

    lost = sorted(lost_set)
    reserve = sorted(reserve_set)

    for r in reserve:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)

# wth
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# wth
def solution(X, Y):
    countX = [0] * 10          # 0~9 각 숫자가 X에 몇 번 나오는지 저장할 배열 (초기값 0)
    countY = [0] * 10          # 0~9 각 숫자가 Y에 몇 번 나오는지 저장할 배열 (초기값 0)

    for ch in X:                # X의 문자를 하나씩 순회 (ch는 '5', '2' 같은 문자)
        countX[int(ch)] += 1     # 해당 숫자의 개수를 1 증가시킴 (문자를 정수로 바꿔 인덱스로 사용)
    for ch in Y:                # Y의 문자를 하나씩 순회
        countY[int(ch)] += 1     # 해당 숫자의 개수를 1 증가시킴

    tmp = []                    # 짝꿍을 구성할 숫자들을 담을 리스트
    for d in range(10):          # 숫자 0부터 9까지 순서대로 확인
        cnt = min(countX[d], countY[d])  # X와 Y 양쪽에서 공통으로 쓸 수 있는 최대 개수 (더 적은 쪽이 기준)
        tmp += [str(d)] * cnt     # 그 개수만큼 숫자 d를 문자열로 tmp에 추가

    if not tmp:                  # tmp가 비어있다면 (공통으로 쓸 수 있는 숫자가 하나도 없음)
        return "-1"               # 짝꿍이 존재하지 않으므로 "-1" 반환

    tmp.sort(reverse=True)        # 가장 큰 정수를 만들기 위해 내림차순 정렬 (큰 숫자가 앞으로)
    ans = ''.join(tmp)            # 정렬된 숫자 리스트를 하나의 문자열로 합침

    if ans[0] == '0':             # 맨 앞 자리(가장 큰 자리)가 0이라면
        return "0"                 # 전체가 0으로만 구성된 경우이므로 "0" 하나만 반환

    return ans                   # 완성된 짝꿍 문자열 반환

# wth LIFO stack 후입선출
def solution(ingredient):
    stack = []          # 재료를 쌓아나갈 스택
    count = 0            # 완성된 햄버거 개수

    for item in ingredient:      # 재료를 순서대로 하나씩 처리
        stack.append(item)        # 새 재료를 스택 맨 위에 쌓음

        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 스택 길이가 4 이상이고, 맨 위 4개가 빵-야채-고기-빵 순서면
            stack.pop()             # 맨 위 빵 제거
            stack.pop()             # 고기 제거
            stack.pop()             # 야채 제거
            stack.pop()             # 맨 아래 빵 제거

            count += 1              # 햄버거 1개 완성

    return count          # 완성된 햄버거 총 개수 반환

# wth data
'''
def solution(data, ext, val_ext, sort_by):
    tmp = [[]]
    dic = {'num':0, 'date':1, 'maximum':2, 'remain':3}
    
    for d in data:
        code = d[dic['code']]
        date = d[dic['date']]
        maximum = d[dic['maximum']]
        remain = d[dic['remain']]
    
    
    return answer
'''
def solution(data, ext, val_ext, sort_by):
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    filtered = list(row for row in data if row[dic[ext]] < val_ext)
    filtered.sort(key=lambda row: row[dic[sort_by]])
    
    return filtered

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],"date",20300501,"remain"))

# wth 보드게임/ 안됨 이거
def solution(board, moves):

    cols =[[row[i] for row in board] for i in range(len(board[0]))]
    tmp =[]
    
    for m in moves:
        col = cols[m-1]
        count = 0
        
        for i in range(len(col)):
            if col[i] != 0:
                tmp.append(col[i])
                col[i] = 0
                break
        else:
            tmp.append(0)
            
        if len(tmp) >= 2 and tmp[-1] != 0 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()
            count += 1

    return count * 2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# wth stack
def solution(board, moves):
    # board의 각 열(column)을 미리 뽑아서 리스트로 만들어둠
    # board[row][col] 형태를 cols[col][row] 형태로 뒤집는 것(전치)
    cols = [[row[i] for row in board] for i in range(len(board[0]))]

    tmp = []    # 크레인으로 뽑은 인형들을 순서대로 쌓아두는 바구니(스택 역할)
    count = 0   # 터져서 사라진 인형의 총 개수

    for m in moves:
        # moves는 1부터 시작하는 열 번호이므로, 인덱스는 m-1로 접근
        col = cols[m-1]

        # 해당 열을 위에서부터(인덱스 0부터) 확인하며
        # 0이 아닌 첫 번째 인형(값)을 찾음
        for i in range(len(col)):
            if col[i] != 0:
                tmp.append(col[i])   # 찾은 인형을 바구니에 추가
                col[i] = 0            # 원래 자리는 빈 칸(0)으로 표시
                break                  # 하나만 뽑으면 되므로 반복 종료
        else:
            # break 없이 for문이 끝까지 실행됨 = 그 열에 인형이 하나도 없었음
            tmp.append(0)   # 뽑을 인형이 없으므로 0을 넣어 자리표시

        # 방금 넣은 인형이 바로 아래(바구니의 이전 값)와 같은지 확인
        # len(tmp) >= 2: 비교할 대상이 최소 2개는 있어야 함
        # tmp[-1] != 0: 뽑은 게 없어서 0이 들어간 경우는 비교 대상에서 제외
        # tmp[-1] == tmp[-2]: 방금 넣은 값과 바로 아래 값이 같은지 확인
        if len(tmp) >= 2 and tmp[-1] != 0 and tmp[-1] == tmp[-2]:
            tmp.pop()     # 방금 넣은 값 제거
            tmp.pop()     # 바로 아래 있던 같은 값도 제거
            count += 2     # 인형 2개가 한꺼번에 터졌으므로 count에 2 더함

    return count   # 최종적으로 터져서 사라진 인형의 총 개수를 반환

# wth 자료구조
def solution(board, moves):
    stacklist = []   # 뽑은 인형들을 쌓아두는 바구니(스택)
    answer = 0        # 터져서 사라진 인형의 총 개수

    for i in moves:
        # i는 몇 번째 열(1부터 시작)인지를 나타냄
        for j in range(len(board)):
            # j는 행 번호(위에서부터 0, 1, 2, ...)
            # board[j][i-1]: j번째 행의 (i-1)번째 열 값 (moves가 1부터 시작하므로 -1)
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])   # 0이 아닌 값을 발견하면 바구니에 추가
                board[j][i-1] = 0                  # 원래 자리는 0으로 비움

                if len(stacklist) > 1:
                    # 바구니에 2개 이상 있어야 비교 가능
                    if stacklist[-1] == stacklist[-2]:
                        # 방금 넣은 값과 바로 아래 값이 같으면
                        stacklist.pop(-1)   # 방금 넣은 값 제거
                        stacklist.pop(-1)   # 그 아래 값도 제거
                        answer += 2           # 인형 2개가 터졌으므로 2 더함
                break
                # 한 열에서 값을 하나 찾으면 더 아래쪽은 볼 필요 없으므로 반복 종료

    return answer

# wth 성격진단
def solution(survey, choices):
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # 8개 성격 유형별 점수를 저장할 딕셔너리, 모두 0으로 초기화

    for s, c in zip(survey, choices):
        # s: 해당 질문의 지표 문자열 (예: "AN")
        # c: 검사자가 선택한 값 (1~7)
        disagree, agree = s[0], s[1]
        # s[0]: 비동의 관련 성격 유형, s[1]: 동의 관련 성격 유형

        if c < 4:
            score[disagree] += 4 - c
            # 비동의 쪽 선택 (1,2,3) → 점수는 4-c (1→3점, 2→2점, 3→1점)
        elif c > 4:
            score[agree] += c - 4
            # 동의 쪽 선택 (5,6,7) → 점수는 c-4 (5→1점, 6→2점, 7→3점)
        # c == 4(모르겠음)이면 아무 점수도 추가하지 않음

    pairs = [('R','T'), ('C','F'), ('J','M'), ('A','N')]
    # 지표 번호 순서대로 비교할 유형 쌍

    result = ''
    for a, b in pairs:
        if score[a] >= score[b]:
            result += a
            # 점수가 같거나 a가 높으면 a 선택 (사전순으로 더 빠른 쪽 우선)
        else:
            result += b

    return result

# wth keypad dic 맨하튼 거리
def solution(numbers, hand):
    # 키패드 좌표 매핑: (행, 열)
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left = keypad['*']    # 왼손 시작 위치
    right = keypad['#']   # 오른손 시작 위치
    result = ''

    def distance(p1, p2):
        # 상하좌우로만 이동하므로 맨해튼 거리(행 차이 + 열 차이) 사용
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    for num in numbers:
        if num in (1, 4, 7):
            result += 'L'
            left = keypad[num]
        elif num in (3, 6, 9):
            result += 'R'
            right = keypad[num]
        else:
            # 2, 5, 8, 0인 경우: 두 손과의 거리 비교
            target = keypad[num]
            dist_left = distance(left, target)
            dist_right = distance(right, target)

            if dist_left < dist_right:
                result += 'L'
                left = target
            elif dist_right < dist_left:
                result += 'R'
                right = target
            else:
                # 거리가 같으면 hand(오른손잡이/왼손잡이)에 따라 결정
                if hand == 'right':
                    result += 'R'
                    right = target
                else:
                    result += 'L'
                    left = target

    return result

# wth re
import re

def solution(new_id):
    new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id

# wth 선형스캔 그리디과
def solution(wallpaper):
    # 파일("#")들의 최소/최대 행·열을 찾기 위한 초기값 설정
    # min_row, min_col은 "가장 큰 값"으로 시작해서 실제 값이 나오면 점점 줄어들도록 함
    # (len(wallpaper): 전체 행 개수, len(wallpaper[0]): 한 행의 길이=열 개수)
    min_row, min_col = len(wallpaper), len(wallpaper[0])

    # max_row, max_col은 "가장 작은 값"으로 시작해서 실제 값이 나오면 점점 커지도록 함
    # -1로 시작하는 이유는 실제 인덱스(0 이상)보다 확실히 작은 값이기 때문
    max_row, max_col = -1, -1

    # wallpaper의 각 행을 순회 (i는 행 번호, row는 그 행의 문자열)
    for i, row in enumerate(wallpaper):
        # 그 행의 각 문자를 순회 (j는 열 번호, char는 해당 칸의 문자)
        for j, char in enumerate(row):
            if char == '#':
                # 파일("#")을 발견했을 때만 경계값 갱신

                min_row = min(min_row, i)
                # 지금까지 찾은 min_row와 현재 행(i) 중 더 작은 값으로 갱신
                # → 파일이 있는 "가장 위쪽" 행을 추적

                max_row = max(max_row, i)
                # 지금까지 찾은 max_row와 현재 행(i) 중 더 큰 값으로 갱신
                # → 파일이 있는 "가장 아래쪽" 행을 추적

                min_col = min(min_col, j)
                # 파일이 있는 "가장 왼쪽" 열을 추적

                max_col = max(max_col, j)
                # 파일이 있는 "가장 오른쪽" 열을 추적

    # 최종적으로 [시작점 행, 시작점 열, 끝점 행, 끝점 열] 형태로 반환
    # max_row+1, max_col+1을 하는 이유:
    # 좌표는 "격자점" 기준이라, 파일이 있는 마지막 칸을 완전히 포함하려면
    # 그 칸의 오른쪽 아래 꼭짓점(칸의 인덱스+1)까지 드래그해야 하기 때문
    return [min_row, min_col, max_row + 1, max_col + 1]

# wth or 
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]

# wth 약관
def solution(today, terms, privacies):
    def to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return (y * 12 + m) * 28 + d
        # 연도를 달 단위로 환산(y*12) 후 월(m)을 더해 총 달 수를 구하고
        # 28을 곱해 일 단위로 바꾼 뒤 일(d)을 더함

    term_dict = {}
    for term in terms:
        kind, period = term.split(' ')
        term_dict[kind] = int(period)
        # "약관 종류: 유효기간(달)" 형태로 딕셔너리에 저장

    today_days = to_days(today)
    answer = []

    for idx, privacy in enumerate(privacies, start=1):
        date_str, kind = privacy.split(' ')
        collected_days = to_days(date_str)
        expire_days = collected_days + term_dict[kind] * 28
        # 유효기간(달)만큼 28일씩 더해서 파기 시작일을 계산

        if expire_days <= today_days:
            answer.append(idx)
            # 오늘 날짜가 파기 시작일과 같거나 지났으면 파기 대상

    return answer

# or
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire

# wth 유연근무제 
def solution(schedules, timelogs, startday):
    def add_10min(time):
        h, m = time // 100, time % 100
        m += 10
        if m >= 60:
            m -= 60
            h += 1
        return h * 100 + m

    answer = 0

    for schedule, timelog in zip(schedules, timelogs):
        allowed = add_10min(schedule)   # 출근 인정 시각
        is_late = False

        for day in range(7):
            weekday = (startday - 1 + day) % 7 + 1
            # startday부터 시작해 7일간의 요일을 1~7로 순환 계산

            if weekday in (6, 7):
                continue   # 토요일(6), 일요일(7)은 검사하지 않음

            if timelog[day] > allowed:
                is_late = True
                break   # 한 번이라도 지각하면 더 볼 필요 없음

        if not is_late:
            answer += 1

    return answer

# wth dic
def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    # 각 선수 이름이 몇 번째 등수(인덱스)인지 저장
    # c리스트에서 이름을 직접 찾아 자리를 바꾸면 시간초과
    # "이름→등수" 딕셔너리를 만들어 O(1)로 조회하는 방식

    for called in callings:
        idx = rank[called]        # 추월한 선수의 현재 등수(인덱스)
        prev_player = players[idx - 1]   # 바로 앞에 있던 선수(추월당한 선수)

        # 두 선수의 위치를 서로 교환
        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        # 딕셔너리에도 새로운 등수를 반영
        rank[called] = idx - 1
        rank[prev_player] = idx

    return players

# wth simul
def solution(park, routes):
    H, W = len(park), len(park[0])
    # H: 공원의 세로 길이(행 개수), W: 공원의 가로 길이(열 개수)

    for i in range(H):
        if 'S' in park[i]:
            # park의 각 행을 확인하며 시작지점 'S'가 포함된 행을 찾음
            y, x = i, park[i].index('S')
            # 그 행에서 'S'의 위치(열 인덱스)를 찾아 (y, x)로 저장
            break
            # 시작지점은 하나뿐이므로 찾으면 즉시 반복 종료

    moves = {
        'N': (-1, 0),  # 북쪽: 세로좌표 -1 (위로)
        'S': (1, 0),   # 남쪽: 세로좌표 +1 (아래로)
        'W': (0, -1),  # 서쪽: 가로좌표 -1 (왼쪽으로)
        'E': (0, 1)    # 동쪽: 가로좌표 +1 (오른쪽으로)
    }
    # 방향 문자를 (세로 이동량, 가로 이동량) 튜플로 매핑해둔 딕셔너리

    for route in routes:
        # routes에 담긴 명령을 순서대로 하나씩 처리

        direction, n = route.split()
        # "E 5" 같은 문자열을 공백 기준으로 나눠 방향과 거리로 분리
        n = int(n)
        # 거리는 문자열이므로 정수로 변환

        dy, dx = moves[direction]
        # 현재 명령의 방향에 해당하는 이동량을 가져옴

        ny, nx = y, x
        # 실제 위치(y, x)는 아직 바꾸지 않고, 임시 좌표(ny, nx)로 이동을 시도

        valid = True
        # 이 명령이 끝까지 유효한지 여부를 저장하는 플래그

        for _ in range(n):
            # 명령에 적힌 거리(n)만큼 한 칸씩 이동을 시도

            ny += dy
            nx += dx
            # 한 칸 이동

            if not (0 <= ny < H and 0 <= nx < W) or park[ny][nx] == 'X':
                # 공원 범위를 벗어났는지, 혹은 장애물('X')을 만났는지 확인
                valid = False
                # 조건에 걸리면 이 명령 전체가 무효
                break
                # 더 이상 진행할 필요 없으므로 반복 종료

        if valid:
            # 모든 칸을 문제없이 이동했다면
            y, x = ny, nx
            # 실제 위치를 새 위치로 갱신
        # valid가 False이면 y, x는 그대로 유지되어 명령이 무시됨

    return [y, x]
    # 모든 명령을 처리한 뒤 최종 위치를 [세로, 가로] 순서로 반환

# wth 완전탐색 그리디
def solution(mats, park):
    row, col = len(park), len(park[0])
    mats.sort(reverse=True)   # 큰 돗자리부터 시도하면 가장 먼저 찾은 게 곧 최댓값

    def check(r, c, size): # (r,c)에 size 크기의 돗자리를 깔 수 있나
        if r + size > row or c + size > col:
            return False   # 공원 범위를 벗어나면 실패
        for i in range(r, r + size):
            for j in range(c, c + size):
                if park[i][j] != "-1":
                    return False   # 사람이 하나라도 있으면 실패
        return True

    for size in mats: # mats의 각 크기(size)에 대해, park의 모든 칸(i, j)을 확인
        for i in range(row):
            for j in range(col):
                if park[i][j] == "-1" and check(i, j, size): # 빈 칸("-1")이면서 check(i, j, size)가 성공
                    return size   # 성공하면 즉시 반환

    return -1   # 어떤 돗자리도 깔 수 없는 경우

# wth 회복
def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    cur_health = health
    combo = 0

    attack_dict = {time: damage for time, damage in attacks} # "공격 시간: 피해량"
    last_time = attacks[-1][0]

    for time in range(1, last_time + 1): # 1초부터 마지막 공격 시각(last_time)까지 1초씩
        if time in attack_dict:
            cur_health -= attack_dict[time] # 그 시각의 피해량만큼 체력을 깎움
            combo = 0 # 붕대 감기가 취소되므로 combo(연속 성공 시간)를 0으로 초기화
            if cur_health <= 0:
                return -1
        else: # 공격 안 받는 시간
            combo += 1
            cur_health += x # 초당 회복량(x)만큼 체력 더하기
            if combo == t: # if combo == 붕대 감기 완료 시간
                cur_health += y # 추가 회복량 더해주고
                combo = 0 # 다시 초기화
            cur_health = min(cur_health, max_health) # 체력은 언제나 < max_health

    return cur_health

# or
def solution(bandage, health, attacks):
    hp = health
    start = 1
    # start: 현재 공격과 다음 공격 사이에서 회복이 시작되는 시각

    for i, j in attacks:
        # i: 이번 공격이 발생하는 시각, j: 이번 공격의 피해량

        hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1]
        # (i - start): 이전 공격 이후부터 이번 공격 직전까지 회복 가능한 시간(초)
        # (i - start) // bandage[0]: 그 시간 동안 붕대 감기를 몇 번 "완전히" 성공했는지
        #   (bandage[0]=t, 완전히 성공한 횟수 × 추가 회복량 y를 더함)
        # (i - start) * bandage[1]: 매 초마다 받는 기본 회복량(x)을 모두 더함
        # 즉, "구간 전체 동안의 기본 회복 + 완전 성공 보너스"를 한 번에 계산

        start = i + 1
        # 다음 회복 구간은 이번 공격 바로 다음 초부터 다시 시작
        # (공격당한 시각에는 회복이 없고, 붕대 감기도 처음부터 다시 시작하므로)

        if hp >= health:
            hp = health
        # 회복 후 체력이 최대 체력을 넘으면 최대 체력으로 제한

        hp -= j
        # 이번 공격의 피해량만큼 체력 감소

        if hp <= 0:
            return -1
        # 체력이 0 이하가 되면 캐릭터가 죽은 것이므로 -1 반환

    return hp
    # 모든 공격을 처리하고 살아남았다면 최종 체력 반환

# wth dic
def solution(id_list, report, k):
    reports = {user: set() for user in id_list}
    # print(reports) # {'muzi': set(), 'frodo': set(), 'apeach': set(), 'neo': set()}
    for r in report:
        reporter, target = r.split()
        reports[reporter].add(target)
    # print(reports) # {'muzi': {'frodo', 'neo'}, 'frodo': {'neo'}, 'apeach': {'frodo', 'muzi'}, 'neo': set()} 
    report_count = {user:0 for user in id_list}
    for reporter in reports:
        for target in reports[reporter]:
            report_count[target] += 1
    # print(report_count) # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    banned = {user for user in id_list if report_count[user] >= k}
    res = []
    for user in id_list:
        count = len(reports[user] & banned)
        res.append(count)

    return res

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# wth sec
def solution(video_len, pos, op_start, op_end, commands):
    
    def to_sec(time_str): # 전부 sec으로 바꿔서 계산하기
        m, s = map(int, time_str.split(':')) # : 기준으로 나누어 정수로 변환
        return m * 60 + s

    def to_str(sec): # 다시 'mm:ss'로 바꾸기
        return f"{sec // 60:02d}:{sec % 60:02d}" #:02d는 한자리일때 두 자리로 바꿔줌 5->05

    tot = to_sec(video_len)
    cur = to_sec(pos)
    start = to_sec(op_start)
    end = to_sec(op_end)

    if start <= cur <= end: # 코드 돌리기 전에 pos가 오프닝 구간 안에 있으면
        cur = end # 바로 오프닝의 엔딩시간으로 옮김

    for c in commands:
        if c == 'prev':
            cur = max(0, cur - 10) # 10초 빼더라도 00보단 작지 않아지도록 lower bound 설정
        else:
            cur = min(tot, cur + 10) # 10초 더하더라도 전체len보다 커지지 않게 upper bound 설정

        if start <= cur <= end:
            cur = end # 다 하고 나서 오프닝 구간 안에 있으면 오프닝 끝나는 시간으로 옮김
    
    return to_str(cur) # 'mm:ss'로 변환해서 리턴

# wth 격자
def solution(n, w, num):
    # 총 층수를 계산합니다. (n-1)//w + 1은 n개의 상자를 w개씩 쌓을 때
    # 마지막 층이 다 채워지지 않아도 올림 처리되어 정확한 층수가 나옵니다.
    layers = (n - 1) // w + 1

    # layers x w 크기의 2차원 격자를 만들고 전부 0으로 초기화합니다.
    # grid[layer][col]에는 해당 위치에 놓인 상자 번호가 저장됩니다.
    grid = [[0] * w for _ in range(layers)]

    k = 1  # 지금 놓을 상자의 번호 (1번부터 시작)
    target_layer, target_col = -1, -1  
    # num번 상자가 위치한 (층, 열)을 저장할 변수, 아직 못 찾았으므로 -1로 초기화

    for layer in range(layers):
        # 각 층을 아래층부터 위층 순서로 확인

        cols = range(w) if layer % 2 == 0 else range(w - 1, -1, -1)
        # 짝수 층(0,2,4...)은 왼쪽→오른쪽(0,1,2,...,w-1) 순서로 놓고
        # 홀수 층(1,3,5...)은 오른쪽→왼쪽(w-1,...,1,0) 순서로 놓음
        # (지그재그로 쌓는 규칙을 그대로 반영)

        for col in cols:
            # 이번 층에서 정해진 순서대로 열(col)을 하나씩 방문

            if k > n:
                break
            # 이미 n개의 상자를 모두 놓았다면 더 이상 놓지 않고 멈춤
            # (마지막 층이 다 채워지지 않는 경우를 처리)

            grid[layer][col] = k
            # 현재 위치(layer, col)에 상자 번호 k를 기록

            if k == num:
                target_layer, target_col = layer, col
            # 지금 놓은 상자가 우리가 찾는 num번 상자라면
            # 그 위치를 target_layer, target_col에 저장해둠

            k += 1
            # 다음에 놓을 상자 번호를 1 증가

    count = 0  # 꺼내야 하는 상자의 총 개수를 저장할 변수

    for layer in range(target_layer, layers):
        # num번 상자가 있는 층(target_layer)부터 맨 위층까지 확인
        # (그 아래층은 위에 있는 상자가 아니므로 확인할 필요 없음)

        if grid[layer][target_col] != 0:
            count += 1
        # 같은 열(target_col)에 상자가 실제로 존재하면(0이 아니면)
        # 그 상자는 num번 상자 위(또는 자기 자신)에 있는 것이므로 개수에 포함

    return count
    # 최종적으로 꺼내야 하는 상자의 총 개수를 반환

# or
def solution(n, w, num):
    m1 = num % (w * 2)  # num을 2w로 나눈 나머지. 이 값이 num이 속한 "열 그룹"을 나타냄
    m2 = ((w * 2 + 1) - m1) % (w * 2) # m1과 짝을 이루는 반대편 나머지 값을 계산
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num, n+1, w*2)) + len(range(num + (m2-m1) % (w*2), n+1, w*2))
'''
# 첫 번째 항: num부터 n까지, num과 같은 나머지(m1)를 갖는 번호들의 개수
    #   (num 자기 자신과 그 위에 쌓인 같은 그룹의 상자들)
    # 두 번째 항: num보다 크거나 같으면서 나머지가 m2인 첫 번째 번호부터 n까지의 개수
    #   (반대편 열 그룹에서 num 위에 쌓인 상자들)
    # 두 항을 더하면 num과 물리적으로 같은 열에 있는, num 포함 그 위의 상자 총개수
'''
# 설명:
'''
지그재그로 쌓다 보면, 같은 물리적 열(column)에 있는 상자 번호들은 2w(짝수 층 + 홀수 층 한 세트)를 주기로 반복되는 두 가지 나머지 값 중 하나를 가진다는 규칙이 있습니다.

짝수 층에서 왼→오른쪽으로 놓인 열의 번호들은 mod 2w 값이 서로 같음

홀수 층에서 오른→왼쪽으로 놓인 열의 번호들도 mod 2w 값이 서로 같음

그리고 이 두 그룹의 나머지 값은 서로 짝을 이룹니다: 하나가 m1이면 짝은 m2 = (2w+1-m1) mod 2w

즉, num과 같은 열에 있는 모든 상자는 num mod (2w) == m1이거나 num mod (2w) == m2인 번호들
'''

# wth 이차원
def solution(friends, gifts):
    n = len(friends)
    # 친구들의 총 수를 n에 저장

    idx = {name: i for i, name in enumerate(friends)}
    # 각 친구 이름을 인덱스(순서 번호)로 매핑한 딕셔너리
    # 예: {"muzi":0, "ryan":1, "frodo":2, "neo":3}
    # 이후 리스트 검색(O(n)) 대신 딕셔너리 조회(O(1))로 빠르게 찾기 위함

    given = [[0] * n for _ in range(n)]
    # n x n 크기의 2차원 배열을 만들고 모두 0으로 초기화
    # given[i][j]는 "i번 친구가 j번 친구에게 준 선물 개수"를 저장할 공간

    for g in gifts:
        # gifts 배열의 각 기록("A B" 형태 문자열)을 하나씩 확인

        a, b = g.split()
        # 공백으로 나눠서 a=선물을 준 사람, b=선물을 받은 사람으로 분리

        given[idx[a]][idx[b]] += 1
        # a가 b에게 준 선물 횟수를 1 증가
        # idx[a], idx[b]로 이름을 배열의 인덱스로 변환해서 접근

    index = [0] * n
    # 각 친구의 "선물 지수"를 저장할 배열, 모두 0으로 초기화

    for i in range(n):
        # 모든 친구 i에 대해 선물 지수를 계산

        for j in range(n):
            # i를 기준으로 다른 모든 친구 j와의 관계를 확인

            index[i] += given[i][j]
            # i가 j에게 준 선물 개수를 더함 (준 선물 총합)

            index[i] -= given[j][i]
            # j가 i에게 준 선물 개수를 뺌 (즉, i가 받은 선물 총합만큼 차감)
            # 결과적으로 index[i] = (i가 준 선물) - (i가 받은 선물)

    receive = [0] * n
    # 다음 달에 각 친구가 받을 선물 개수를 저장할 배열

    for i in range(n):
        # 선물을 받을 친구 후보 i

        for j in range(n):
            # i와 비교할 상대방 친구 j

            if i == j:
                continue
            # 자기 자신과는 비교하지 않고 건너뜀

            if given[i][j] > given[j][i]:
                # i가 j에게 준 선물이 j가 i에게 준 선물보다 많다면
                # (i가 이 관계에서 더 "베푼" 사람이므로 다음 달엔 i가 받음)
                receive[i] += 1

            elif given[i][j] == given[j][i]:
                # 두 사람이 주고받은 선물 개수가 같다면(기록이 없는 경우 포함)

                if index[i] > index[j]:
                    # 선물 지수가 더 큰 사람이 선물을 받는 규칙에 따라
                    # i의 선물 지수가 j보다 크면 i가 받음
                    receive[i] += 1
                # 선물 지수도 같다면 아무 조건도 만족하지 않으므로
                # receive[i]가 증가하지 않음 (아무도 선물을 주지 않음)

    return max(receive)
    # 모든 친구의 받을 선물 개수 중 가장 큰 값을 반환

# wth gcd
from math import gcd
# 최대공약수(gcd)를 구하는 함수를 표준 라이브러리에서 가져옴
# 이 함수를 이용해 최소공배수(lcm)를 계산할 것임

def solution(signals):

    def lcm(a, b):
        # 두 수 a, b의 최소공배수를 구하는 함수
        return a * b // gcd(a, b)
        # 공식: (a*b) / gcd(a,b) = lcm(a,b)
        # 정수 나눗셈(//)을 쓰는 이유는 a*b가 항상 gcd(a,b)로 나누어지기 때문

    cycles = [sum(s) for s in signals]
    # 각 신호등의 전체 주기(초록+노란+빨간 지속시간의 합)를 리스트로 저장
    # 예: [2,1,2] → 5, [5,1,1] → 7

    total_cycle = 1
    # 모든 신호등 주기의 최소공배수를 저장할 변수, 처음엔 1로 시작

    for c in cycles:
        total_cycle = lcm(total_cycle, c)
        # 지금까지 계산한 lcm과 새로운 주기 c의 lcm을 다시 구해서 갱신
        # 이렇게 반복하면 모든 신호등 주기의 공통 lcm이 완성됨

    for t in range(1, total_cycle + 1):
        # 1초부터 total_cycle초까지 1초씩 확인
        # total_cycle을 넘어가면 모든 신호등의 패턴이 정확히 반복되므로
        # 그 이후는 확인할 필요가 없음

        all_yellow = True
        # 이번 시각(t)에 모든 신호등이 노란불인지 여부를 저장하는 플래그
        # 일단 True로 가정하고 하나라도 아니면 False로 바꿈

        for G, Y, R in signals:
            # 각 신호등의 초록(G), 노란(Y), 빨간(R) 지속시간을 하나씩 확인

            pos = (t - 1) % (G + Y + R)
            # 시간은 1초부터 시작하지만 나머지 연산은 0부터 계산하는 게 편리하므로
            # (t-1)로 바꿔서 0초 기준으로 맞춤
            # pos는 "이번 신호 주기 안에서 몇 번째 초에 해당하는지"를 의미
            # 예: G+Y+R=5이고 t=13이면 pos = 12 % 5 = 2

            if not (G <= pos < G + Y):
                # pos가 초록불 구간(0~G-1)을 지나
                # 노란불 구간(G ~ G+Y-1)에 있는지 확인
                # 조건을 만족하지 않으면(=노란불이 아니면) 아래로 진입

                all_yellow = False
                # 이 신호등이 노란불이 아니므로 전체 조건 실패로 표시
                break
                # 하나라도 노란불이 아니면 더 볼 필요 없으므로 반복 종료

        if all_yellow:
            # 모든 신호등을 확인했는데 all_yellow가 여전히 True라면
            # (=모든 신호등이 동시에 노란불이라는 뜻)
            return t
            # 그 시각을 바로 반환 (가장 빠른 시각이므로 즉시 반환해도 됨)

    return -1
    # total_cycle까지 다 확인했는데도 찾지 못했다면
    # 영원히 그런 순간이 오지 않는다는 뜻이므로 -1 반환

# wth
def solution(message, spoiler_ranges):
    n = len(message)
    is_spoiler = [False] * n
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            is_spoiler[i] = True

    words_pos = []
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        j = i
        while j < n and message[j] != ' ':
            j += 1
        words_pos.append((message[i:j], i, j - 1))
        i = j

    important_set = set()      # 지금까지 카운트된 중요한 단어
    non_spoiler_set = set()    # 일반 구간에 등장한 단어
    seen_spoiler_set = set()   # 이미 공개(카운트)된 스포 단어

    for word, ws, we in words_pos:
        hidden = any(is_spoiler[ws:we + 1])
        if hidden:
            # 조건 2, 3: 일반 구간에 등장한 적 없고, 아직 공개된 적 없어야 함
            if word not in non_spoiler_set and word not in seen_spoiler_set:
                important_set.add(word)
                seen_spoiler_set.add(word)
        else:
            non_spoiler_set.add(word)
            # 이미 중요한 단어로 카운트했었지만 뒤에서 일반 구간에 등장하면 취소
            if word in important_set:
                important_set.remove(word)

    return len(important_set)

# or
def solution(message, spoiler_ranges):
    a = list(message)
    result = 0
    message = message.split()
    for i in spoiler_ranges:
        b = a[i[0]:i[1] + 1]
        for j in b:
            if j == " ":
                continue
            b[b.index(j)] = "-"
        a[i[0]:i[1] + 1] = b
    a = "".join(a).split()
    for i,j in enumerate(a):
        if "-" in j and not message[i] in a:
            result+=1
            a[i] = message[i]
    return result