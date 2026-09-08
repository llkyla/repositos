a = [100, 200, 300, 400, 500]

a.append(10)
a.pop(2)

value1 = 10
print(value1 in a)
value2 = 40
print(value2 in a)

print(a)

# hash table

dt = {}
# 특정 키에 대한 값 할당
dt["apple"] = 500
dt["banana"] = 1000
dt["cherry"] = 700

# 딕셔너리 출력
print("딕셔너리:", dt)
print()

# 특정 키의 값 조회
print("banana의 값:", dt["banana"])
print()

# 특정 키의 값 삭제
del dt["cherry"]
print("cherry 삭제 후 딕셔너리:", dt)
print()

# 딕셔너리의 크기 확인
print("딕셔너리의 크기:", len(dt))
print()

# 특정 키의 존재 여부 확인
print("apple" in dt)
print("pineapple" in dt)
print(142 in dt)

##

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

c = {1: 'c'}
c[3] = 'b'
print(c)


###

grade = 'A'
match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case 'D':
        print("Poor")
    case _:
        print("Invalid grade")

for number in range(10, -1, -1):
    print(number)
print("-----")


for x in "Hextro nite":
    print(x)
print("-----")

for i in range(2, 10, 2):
    print(i)
print("We have %d even numbers"%(len(range(2, 10, 2))))


print("------")

from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s

def is_prime(n):
	return (len(get_divisors(n)) == 2)

print(is_prime(7))
print(is_prime(8))

print("------")

from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s

def get_GCD(a, b):
	set_a = get_divisors(a)
	set_b = get_divisors(b)
	return max(set_a & set_b)

print(get_GCD(12, 8))

from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s
d = []
for i in range(1, int(a ** 0.5)+1):
         if (a % i) == 0:
            d.append(i)
            if ((i ** 2) != a):
                 d.append(a // i)
                 
def get_GCD(a, b):
	set_a = get_divisors(a)
	set_b = get_divisors(b)
	return max(set_a & set_b)

def get_LCM(a, b):
	return (a * b // get_GCD(a, b))

print(get_LCM(12, 8))

# n 이하의 자연수가 소수인지 아닌지 - 에라토스테네스의 체
from math import sqrt

N = 120
is_prime = [True] * (N + 1)  # 처음에는 모두 true로 초기화
is_prime[1] = False  # 1은 소수가 아니므로

# 에라토스테네스의 체 알고리즘
for i in range(2, int(sqrt(N)) + 1):
    
    if not is_prime[i]: 
          continue  # 이미 소수가 아닌 것으로 표시된 경우 건너뜁니다.
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False

for i in range(1, N + 1):
    print(i, is_prime[i])

# 유클리드
for i in range(1, N + 1):
    print(i, is_prime[i])
	
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

print(gcd(12, 8))

# 유클리드 호제법
def solution(n, m):
    a, b = n, m
    while b != 0:
        a, b = b, (a % b)
    gcd = a
    lcm = (n * m) // gcd
    
    return [gcd, lcm]

# Permutation
N = 4
R = 3
lst = [1, 2, 3, 4]
check = [False] * N # 원소 사용 여부를 체크
# check[k] 가 true 이면 인덱스가 k인 원소가 사용중임을 나타냄.
# check[k] 가 false 이면 인덱스가 k인 원소가 사용중이지 않음을 나타냄.
choose = [] # 나열한 원소를 보관

def permutation(level):
	if level == R:
		# 나열한 R 개의 원소를 출력
		print(choose)
		return

	# for문
	for i in range(0, N):
		if check[i] == True: # 인덱스가 i인 원소가 이미 사용중이라면 continue
			continue

		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가) 
		check[i] = True # 인덱스가 i인 원소를 사용하고 있으므로 true로 초기화

		permutation(level+1) # 다음 for 문으로 들어가는 역할

		check[i] = False # 인덱스가 i인 원소의 사용이 끝났으므로 false로 초기화
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거


permutation(0)

# Combination
N = 4
R = 3
lst = [1, 2, 3, 4]
choose = [] # 선택한 원소를 보관

def combination(index, level):
	if level == R:
		# 선택한 R 개의 원소를 출력
		print(choose)
		return

	# for문
	for i in range(index, N): 
		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

combination(0, 0)

# 재귀함수 조합 알고리즘 
N = 10
R = 5
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choose = [] # 선택한 원소를 보관

def combination(index, level):
	if level == R:
		# 선택한 R 개의 원소를 출력
		print(choose)
		return

	# for문
	for i in range(index, N): 
		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

combination(0, 0)

# 5C3의 두 가지 방법.
# 1 for문 3번 돌리기:
N = 5
lst = [1, 2, 3, 4, 5]
res = []

for i in range(0, N):
	res.append(lst[i]) #omitable
	for j in range(i+1, N):
		res.append(lst[j]) #omitable
		for k in range(j+1, N):
			res.append(lst[k]) #omitable
			print(lst[i], lst[j], lst[k]) # since can access to i, j, k all at once
			res.pop()

# recusrive func
N = 5
R = 3
lst = [1, 2, 3, 4, 5]
res = []

def comb(idx, lv):
	if lv == R:
		print(res)
		return
	
	for i in range(idx, N):
		res.append(lst[i]) # idx=1 선택
		comb(i+1, lv+1) # 
		res.pop() # 넣었던 idx=i 원소 제거

comb(0,0)

# 백준 로또
def comb(idx, lev):
	global choose, arr, k
	# choose, arr, k는 함수 바깥(전역)에서 정의된 변수를 함수 안에서도
    # 그대로 읽고 수정하겠다는 선언 (global 없으면 함수 안에서 새 지역변수로 취급됨)

	# base case 
	if lev == 6: # 지금까지 6개를 선택했으면 하나의 조합이 완성된 것
		for u in choose:
			print(u, end=' ')
			# 완성된 조합의 원소들을 한 줄에 공백으로 구분해 출력
            # end=' '로 줄바꿈 대신 공백을 넣어 한 줄에 이어붙임 ex) 1 2 3 4 ...
		print() # 조합 하나 출력이 끝나면 줄바꿈 (다음 조합은 새 줄에 출력되도록)
		return # break

	# recursive case
	for i in range(idx, k):
		# idx부터 k-1까지의 인덱스를 순서대로 확인
        # idx부터 시작하는 이유: 이미 지나간 원소는 다시 고려하지 않아 중복 조합 방지
		choose.append(arr[i]) # arr의 i번째 원소를 선택 목록에 추가
		comb(i + 1, lev + 1) # 다음 원소는 i+1부터 뽑도록 재귀 호출, 선택한 개수(lev)는 1 증가
		choose.pop() # 재귀 호출이 끝나고 돌아오면 방금 추가한 원소를 다시 제거 (백트래킹)
					 # 다음 반복(i+1)에서 다른 원소를 넣어보기 위한 초기화 작업


while True:
	choose = [] # 매 줄마다 선택 목록을 새로 초기화
	I = list(map(int, input().split())) # 한 줄을 입력받아 = input()
										# ^를 공백 기준으로 나누고 = .split() 
										# 모두 정수로 변환한 = map(int, ~)
										# 리스트 = list()

	k = I[0] # 첫 번째 숫자는 "총 몇 개의 숫자가 있는지"를 의미
	arr = I[1:] # 첫 번째를 제외한 나머지가 실제 뽑을 대상 숫자들
	if k == 0: # k가 0이면 = 총 0개의 숫자가 있으면 break
		break

	comb(0, 0) # 0번째 인덱스부터, 0개를 선택한 상태로 조합 생성 시작
	print() # 한 줄(한 세트)의 모든 조합 출력이 끝나면 구분을 위해 빈 줄 추가

# SAME AS
from itertools import combinations

while True:
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

	for comb in combinations(arr, 6):
		for u in comb:
			print(u, end=' ')
		print()
	print()

# 백준 암호 만들기
vows = ['a', 'e', 'i', 'o', 'u']
choose = []


def is_possible():
	global L, C, choose, arr

	vow = 0
	for c in choose:
		vow += (c in vows)
		# c가 vows 안에 있으면 True(=1), 없으면 False(=0)
        # True/False는 파이썬에서 각각 1/0으로 취급되므로 그냥 더할 수 있음
        # 즉 choose 안의 모음 개수를 하나씩 세는 것
	con = L - vow # 전체 길이(L)에서 모음 개수를 빼면 자음 개수가 나옴

	return (vow >= 1 and con >= 2) # 모음이 1개 이상이고 자음이 2개 이상이면 True, 아니면 False

def combination(idx, lev):
	global L, C, choose, arr

	# base case
	if lev == L:
		if is_possible():
			print(''.join(choose)) # 리스트를 문자열로 합쳐서 출력 (예: ['a','c','d'] → "acd")
		return

	# recursive case
	for i in range(idx, C):
		choose.append(arr[i])
		combination(i + 1, lev + 1)
		choose.pop()


L, C = map(int, input().split()) # L: 암호(비밀번호)의 길이, C: 주어진 알파벳 문자의 총 개수
arr = input().split() # 공백으로 구분된 C개의 알파벳 문자들을 리스트로 받음

arr.sort()
# 사전순으로 출력하려면 뽑기 전에 미리 정렬해야 함
# (조합은 idx부터 순서대로만 뽑으므로, arr이 정렬돼 있으면 자동으로 사전순 조합이 만들어짐)

combination(0, 0)

# SAME AS
from itertools import combinations


vows = ['a', 'e', 'i', 'o', 'u']


def is_possible(word):
	global L, C, arr

	vow = 0
	for w in word:
		vow += (w in vows)
	con = L - vow

	return (vow >= 1 and con >= 2)


L, C = map(int, input().split())
arr = input().split()

arr.sort()

for word in combinations(arr, L):
	if is_possible(word):
		print(''.join(word))