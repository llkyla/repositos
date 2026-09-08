# Dictionary

dic = {"x": 1, "y": 2}
dic1 = dict(x = 1, y = 2)

print(dic) # OUPUT: {"x": 1, "y": 2}
print(dic1["x"]) # OUTPUT: 1

print(dic1.get("a")) # OUTPUT: None if "a" DNE
print(dic1.get("a", 0)) # OUTPUT: 0 if "a" DNE

for key in dic:
    print(key, dic[key]) # OUTPUT: x 1 
                         #         y 2
for x in dic1.items():
    print(x) # OUTPUT: ('x', 1)
             #         ('y', 2)
    

for key, value in dic.items():
    print(key, value) # OUTPUT: x 1 
                      #         y 2

a = {
    "Sajjad": {"math": 100, "English": 95},
    "David": {"math": 90, "English": 85}
}

print(a["Sajjad"]["English"]) # OUTPUT: 95 // [][] 형식 여긴 ~nested
a["David"]["math"] = 100 # updating the value
a["Alex"] = {"math": 80, "English": 75} # adding to dictionary
del a["Sajjad"] # deleting 

b = {
    "Sajjad": {"math": 100, "English": 95},
    (1, 2): "cat",
    "x" : [1, 2, 3],
    "y" : (4, 5, 6),
    2095: "I will not be alive this year."
} # list cannot be key

print(b.values()) # OUTPUT: values of b
print(b.items()) # OUTPUT: (key, value)s of b
# x.clear() # clear all = empty dict
# x.pop(2095)



# .join // only str
x = "123"
print(", ".join(x)) # OUTPUT: 1, 2, 3



# lambda
def add(x, y):
    return x + y
print(add(4, 5))

print((lambda x, y: x + y)(4, 5))


def my_map(my_func, my_iter):
    res = []
    for item in my_iter:
        new_item = my_func(item)
        res.append(new_item)
    return res

nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x ** 3, nums)

print(cubed)

# map
# map() 함수는 iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환합니다. 
# 이때, function 함수는 각 요소를 인자로 받아서 처리하며, 함수의 반환값이 새로운 iterator의 각 요소가 됩니다.

def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # [1, 4, 9, 16, 25]


items = [
	("Product1", 10),
	("Product2", 9),
	("Product3", 12)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

prices = []
for item in items:
	prices.append(item[1])

x = map(lambda item: item[1], items)
print(x) # OUTPUT: <map object at 0x000001C2B7088700>
for item in x:
     print(item) # OUTPUT: 10 // 9 // 12

prices = list(map(lambda item: item[1], items))
print(prices) # OUTPUT: [10, 9, 12]


# 비트 쉬프트 연산 << >> 
n = 10
print(n<<1) # n * 2 = 20
print(n>>1) # n / 2 = 5
print(n<<2) # n * 2^2 = 40
print(n>>2) # (n / 2) / 2 = 2
print(n<<3) # n * 2^3 = 80
print(n<<4) # n * 2^4 = 80



# num_list[::n]
def solution(names):
    answer = []
    
    for i in range(0, len(names), 5):
        answer.append(names[i])
        
    return answer

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))

# wth
def solution(names):
    return names[::5] # = names[start=0 : stop=len(names) : step=5]



# enumerate
for entry in enumerate(['A', 'B', 'C']):
    print(entry) # OUTPUT: (0, 'A')
#                          (1, 'B')
#                          (2, 'C')

for i, letter in enumerate(['A', 'B', 'C']):
    print(i, letter) # OUTPUT: 0 A
#                              1 B
#                              2 C 


# Boolean
def solution(myString, pat):
    
    return 1 if ((pat.lower()) in (myString.lower())) else 0

print(solution("AbCdEfG", "aBc"))


# wth
def solution(myString, pat):
    return int(pat.lower() in myString.lower()) # boolean?

# map
def make_even(num):
    if num % 2 == 1:
        return num+1
    else:
        return num

x = [551, 641, 891, 122, 453, 223, 234, 343, 115]

y =[]

for num in x:
    y.append(make_even(num))

print(y)

z=[]

z = list(map(make_even, x)) # map(func, iterable)

print(z)
d = []
# 약수찾기
for i in range(1, int(n ** 0.5)+1):
        if (n % i) == 0:
            d.append(i)
            if ((i ** 2) != n):
                d.append(n // i)

# 콜라츠 
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1


# ── 리스트/문자열/실수 관련 메서드 정리 ──

# .remove(값)
#   1) 쓸 수 있는 type : list, set
#   2) 원본 변경 여부   : O (원본 자체를 바꿈, 반환값 없음 → 재대입 금지)
#   3) 비용            : O(n) - 값을 찾기 위해 처음부터 순회

# .append(값)
#   1) 쓸 수 있는 type : list
#   2) 원본 변경 여부   : O (원본 끝에 추가, 반환값 없음)
#   3) 비용            : O(1) - 끝에 붙이기만 하므로 매우 빠름

# .replace(old, new)
#   1) 쓸 수 있는 type : str
#   2) 원본 변경 여부   : X (새 문자열을 반환, 원본은 그대로 → 재대입 필요)
#   3) 비용            : O(n) - 문자열 전체를 훑으며 치환

# .sort()
#   1) 쓸 수 있는 type : list
#   2) 원본 변경 여부   : O (원본 리스트 자체를 정렬, 반환값 없음)
#                        ※ sorted()는 반대로 새 리스트를 반환 (원본 유지)
#   3) 비용            : O(n log n)

# .isupper()
#   1) 쓸 수 있는 type : str
#   2) 원본 변경 여부   : X (True/False만 반환)
#   3) 비용            : O(n) - 문자열 길이만큼 확인

# .isdigit()
#   1) 쓸 수 있는 type : str
#   2) 원본 변경 여부   : X (True/False만 반환)
#   3) 비용            : O(n)

# .is_integer()
#   1) 쓸 수 있는 type : float (int에는 없음)
#   2) 원본 변경 여부   : X (True/False만 반환)
#   3) 비용            : O(1)

# .is_string() → 파이썬에 존재하지 않는 메서드
#   대신 isinstance(값, str) 사용
# isinstance(d, str)


# 등차수열   Arithmetical Series
def arithmetic_nth(a1, d, n):
    # a1: 첫 번째 항
    # d : 공차 
    # n : 몇 번째 항을 구할지
    
    # 공식: an = a1 + (n-1) * d
    # n번째 항은 첫 항에서 공차를 (n-1)번 더한 값이라는 뜻
    # 예: a1=2, d=3, n=4 → 2 + 3*3 = 11 (2,5,8,11에서 4번째 항)
    return a1 + (n - 1) * d

# 등차수열 합 Arithmetical Series
def arithmetic_sum(a1, d, n):
    # a1: 첫 번째 항, d: 공차, n: 몇 항까지 더할지
    
    # n번째 항의 값을 먼저 구함 (위 함수와 같은 공식)
    an = a1 + (n - 1) * d
    
    # 공식: Sn = n * (a1 + an) / 2
    # "첫 항과 마지막 항을 더한 값"에 "항의 개수"를 곱하고 2로 나누는 원리
    # (사다리꼴 넓이 공식과 같은 아이디어: 등차수열은 그래프로 그리면 사다리꼴 모양)
    return n * (a1 + an) / 2

def geometric_nth(a1, r, n):
    # a1: 첫 번째 항의 값
    # r : 공비 (이웃한 두 항의 비율)
    # n : 몇 번째 항을 구할지
    
    # 공식: an = a1 * r^(n-1)
    # n번째 항은 첫 항에 공비를 (n-1)번 곱한 값이라는 뜻
    # 예: a1=2, r=3, n=4 → 2 * 3^3 = 54 (2,6,18,54에서 4번째 항)
    return a1 * (r ** (n - 1))

def geometric_sum(a1, r, n):
    # a1: 첫 번째 항, r: 공비, n: 몇 항까지 더할지
    
    if r == 1:
        # 공비가 1이면 모든 항이 a1로 동일하므로
        # 단순히 a1을 n번 더한 값이 됨 (분모가 0이 되는 걸 방지하기 위한 예외 처리)
        return n * a1
    
    # 공식: Sn = a1 * (1 - r^n) / (1 - r)
    # 등비수열 합의 일반 공식 (r이 1이 아닐 때만 성립)
    return a1 * (1 - r ** n) / (1 - r)


# 유클리드 호제법
def solution(n, m):
    a, b = n, m
    while b != 0:
        a, b = b, (a % b)
    gcd = a # while문이 도는 동안 계속하여 a에는 이전 b값이 저장되므로
    lcm = (n * m) // gcd
    
    return [gcd, lcm]

# n 이하의 자연수가 소수인지 아닌지 - 에라토스테네스의 체
from math import sqrt

N = 120
is_prime = [True] * (N + 1)  # 처음에는 모두 true로 초기화
is_prime[1] = False  # 1은 소수가 아니므로

# 에라토스테네스의 체 알고리즘


def sieve_of_eratosthenes(n):
    # True로 초기화된 배열 (소수 여부를 판별할 범위)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # i의 배수들을 False로 변경
            for j in range(i*i, n + 1, i):
                sieve[j] = False
                
    # True인 인덱스만 리스트로 반환
    return [i for i, prime in enumerate(sieve) if prime]

print(sieve_of_eratosthenes(50))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 49는 제외, 47]

# 그리디(탐욕) 알고리즘
def solution(d, budget):
    d.sort()
    tot = 0
    ans = 0
    
    for a in d: # 정렬된 순서대로(가장 적은 금액부터) 하나씩 확인
        tot += a # 현재 부서의 신청 금액을 누적 합계에 더해봄 (일단 배정한다고 가정)
        if tot <= budget: # 누적 합계가 예산을 넘지 않으면
            ans += 1
        else:
            break # 이미 오름차순 정렬했으므로 남은 부서는 더 큰 금액이라 지원 불가능)
    return ans

from itertools import combinations

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

# wth
def solution(food):
    left = ''
    for i in range(1, len(food)):
        count = food[i] // 2
        left += str(i) * count
    
    return left + "0" + left[::-1] # :: 아직도 헷갈림

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

data = ["abce", "abcd", "cdx"]
sorted(data, key=lambda s: (s[2], s))

# 오름차순 lambda x: x
# 내림차순 lambda x: -x
# 문자열 길이순 lambda x: len(x)
# 길이순, 동점이면 사전순 lambda x: (len(x), x)
# 대소문자 무시정렬 lambda w: w.lower()

def solution(array, commands):
    ans = []
    
    for c in commands:
        i, j, k = c
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
    
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
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
        heapq.heappush(hall, s) # 새 점수를 힙에 추가
        
        if len(hall) > k: # k명을 초과하면
            heapq.heappop(hall) # 가장 낮은 점수를 제거 (힙에서 자동으로 최솟값 제거)
            
        ans.append(hall[0]) # 현재 힙에서 가장 작은 값이 곧 발표 점수
        
    return ans

# wth 
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
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


print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))

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
            score += dic.get(person, 0)

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
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])

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

# ── arr.sort() vs sorted(arr) ──

# arr.sort()  : arr 자체를 정렬시키는 코드 (원본 변경, 반환값 없음)
# sorted(arr) : arr은 변화가 없으며, arr을 정렬한 결과를 반환하는 코드 (원본 유지)
arr = [3, 1, 2]

# arr.sort() 사용 예시
arr.sort()
print(arr)  # [1, 2, 3]  ← 원본 arr 자체가 바뀜


arr2 = [3, 1, 2]

# sorted(arr) 사용 예시
result = sorted(arr2)
print(arr2)    # [3, 1, 2]  ← 원본은 그대로
print(result)  # [1, 2, 3]  ← 정렬된 새 리스트가 반환됨


nums = [3, 1, 2]

# reverse=True → 내림차순
sorted(nums, reverse=True)  # [3, 2, 1]

# key function → 사용자 정의 정렬 기준
words = ["banana", "kiwi", "apple"]
sorted(words, key=len)  # 길이 기준 정렬 → ['kiwi', 'apple', 'banana']

# sort()도 리스트에서는 key, reverse 옵션을 동일하게 사용 가능
words.sort(key=len)


# ── 자세히 알아보기 ──

# .sort() 함수는 파이썬 리스트 클래스의 메소드로, 리스트 자료형에서만 사용 가능하다.

# sorted() 함수는 파이썬의 내장 함수로 iterable(순서가 존재하는) 객체에 대해 모두 사용 가능하다.

"""
.sort()   : 리스트(list)에만 있는 메소드, 원본을 직접 바꿈, 반환값 None
sorted()  : 모든 iterable(list, tuple, str, dict 등)에 쓸 수 있는 내장 함수
            원본은 그대로 두고 정렬된 새 리스트를 반환
즉 원본을 보존해야 하면 sorted(), <- 더 비쌈 복잡도는 O(n log n)으로 동일 ∵ 리스트 복사해야해서
원본을 그대로 정렬해도 되면 .sort() 사용

# iterable : 배열과 같이 원소간의 순서가 존재하는 객체를 의미
# 입력으로 넣은 iterable 객체를 오름차순으로 정렬하여 리스트 형태로 반환
# reverse 옵션을 True로 하면 내림차순으로 정렬한 결과를 반환한다
# key function을 넣으면 사용자 정렬이 가능하다
"""

# bin() 은 언제나 정수를 2진수임을 표시하는 접두사 0b와 실제 이진수를 str로 반환
# .zfill(n) len = n까지 앞에 0을 붙임