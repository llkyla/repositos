# 2641

def f(n, ban):

    if n == 0:
        return 1

    if n < 0:
        return 0

    cnt = 0

    # 1step
    cnt += f(n-1, max(0, ban - 1))

    # 2steps
    cnt += f(n-2, max(0, ban - 2))

    # 3steps
    if ban == 0:
        cnt += f(n-3, 2)

    return cnt


n = int(input())
print(f(n,0))