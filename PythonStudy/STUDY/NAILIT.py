n = input()
arr = input()

print(arr.swapcase())

#
a, b = list(map(float, input().split()))

print(f"{a + b:.6f}")

#
N = int(input())
arr = list(map(int, input().split()))

for i, s in sorted(enumerate(arr), key=lambda x: x[1], reverse=True)[:3]:
	print(i+1)

    # 여기서 x = (i, s) 니까 key=lambda x:는 x[1] 이 sorting의 기준이다
	
#
N = int(input())
arr = list(map(int, input().split()))

#tmp = list(int(oct(a)[2:]) for a in arr)

print(oct(sum(arr))[2:])

# 완탐 + 그리디
N = int(input())

events = [tuple(map(int, input().split())) for _ in range(N)]

events.sort(key=lambda x: x[1])

count = 0
prev_end = -1

for start, end in events:
    if start > prev_end:
        count += 1
        prev_end = end

print(count)

#
N = int(input())

coins = [40, 20, 10, 5, 1]
cnt = 0

for coin in coins:
	cnt += N // coin
	N %= coin

print(cnt)

#
N, M = map(int, input().split())

seen = set()

for i in range(M):
    x = int(input())
    seen.add(x)

    if len(seen) == N:
        print(i + 1)
        break
else:
    print(-1)

#
'''
Write Python code. for string S and E, is S included in E, print E with erased S; i.e., S=GOO, E=GOOedGOO, output should be ed. if E is consisted of all A, print EMPTY


if can, estimate num of tokens that u used to answer my chat. include num of tokens that I used to ask u too based on GPT 5.2 model; also, advice for making u to use less token and aiming for the less run time. if Korean takes less token, also tell me too.
 
=> Python code only. Remove all S from E. If E becomes empty, print EMPTY.
'''
S, E = list(map(int, input().split()))
Sstr = str(input())
Estr = str(input())

res = Estr.replace(Sstr, "")

print("EMPTY" if res == "" else res)