# 2832

n, k = map(int, input().split())

# dp[i][j] = num of methofs till i-th, j times moving

dp = [[0] * k for _ in range(n + 1)]

dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(1, k):
        
        # 1
        dp[i][j] += dp[i - 1][j - 1]

        # 2
        if i >= 2:
            dp[i][j] += dp[i - 2][j - 1]

print(sum(dp[n]))