# 1930

while True:
    try:
        k, n = map(int, input().split())
    except EOFError:
        break

    def SuperSum(k,n):
        if k == 0:
            return n

        tot = 0

        for i in range(n):
            tot += SuperSum(k-1, i+1)

        return tot

    print(SuperSum(k,n))