# 2653

n = int(input()) # 3

dp = [0] * (n + 1) # place to save res

dp[1] = 2 # 2 is res when len is 1 (smallest)

if n >= 2:
    dp[2] = 3 # 3 is res when len is 2 (2nd smallest)

for i in range(3, n + 1): # using 2 bases for the rest
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])