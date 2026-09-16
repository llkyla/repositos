# 2626

n = int(input())
cnt = 0

for a in range(1, n // 3 + 1):
    for b in range(a, (n - a) // 2 + 1):
        c = n - a - b

        if b <= c and a + b > c:
            cnt += 1
print(cnt)
