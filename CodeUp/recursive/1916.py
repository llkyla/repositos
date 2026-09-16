import sys

sys.setrecursionlimit(10000)

dp = [0] * 201

def f(n):
    if n == 1 or n == 2:
        return 1

    if dp[n] != 0:
        return dp[n]

    dp[n] = (f(n - 1) + f(n - 2)) % 10009

    return dp[n]

n = int(input())

print(f(n))