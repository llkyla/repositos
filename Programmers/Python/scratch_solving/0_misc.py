# import random

# A = [""] # 공
# B = ["2"] # 수

# a = random.choice(A)
# b = random.choice(B)

# res = a + b

# print("""
# ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

#     공: %s

#     수: %s

# ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
# """ % (a, b))

# n1 = [1,2,3,4,5]
# n2 = [6,7,8,9,10]

# res = [x**2 for x in n1]
# print(res)

# ans = map(lambda x,y: x+y, n1, n2)
# print(list(ans))

# text = '안녕하세요! 저는 파이썬을 배우고 있습니다.'
# f_t = ''.join(filter(lambda x: x != '!', text))
# print(f_t)

# N = int(input())
# words = [input() for _ in range(N)]

# words = sorted(words)

# for word in words:
# 	print(word)

def comp(x):
	return x

# arr1 = [4, 2, 3, 1, 5]
# print(sorted(arr1))
# print(sorted(arr1, key=lambda x: -x))
# print()

# arr2 = [(2, 3), (2, 1), (1, 3), (1, -1), (3, 2)]
# print(sorted(arr2))
# print(sorted(arr2, key=lambda x: x[1]))
# print()

arr3 = [(2, 1, 1), (1, 1, 3), (1, 2, 1), (1, 1, 2)]
print(sorted(arr3))
print(sorted(arr3, key=lambda x: -x[1]))
print()

'''
스트라이크와 볼에 대한 정보가 N개 주어지면, 해당 조건을 만족하는 답의 개수를 구하는 문제
    - 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수
'''

from itertools import permutations

N = int(input())
infos = [input().split() for _ in range(N)]
ans = 0

for cur in permutations(range(1, 10), 3):
    ok = True

    for num, st, bl in infos:
        cur_st = cur_bl = 0

        for i in range(3):
            if str(cur[i]) == num[i]:
                cur_st += 1
            elif str(cur[i]) in num:
                cur_bl += 1

        if cur_st != int(st) or cur_bl != int(bl):
            ok = False
            break

    if ok:
        ans += 1

print(ans)