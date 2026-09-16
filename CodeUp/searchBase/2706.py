# 2706

n = input()
l = len(n)
'''
138947192
'''

dp = [0] * (l + 1)

dp[1] = int(n[0])

'''
dp[i] = 0 # max sum cutting by size i
e.g. dp[1] = 1
'''

if l >= 2:
    dp[2] = int(n[:2])

for i in range(3, l+1):
    one = int(n[i-1])
    two = int(n[i-2:i])

    dp[i] = max(
        dp[i-1] + one,
        dp[i-2] + two
    )
'''
dp[1] = 1
dp[2] = 13
dp[3] = max(dp[1] + 38, dp[2] + 8)
'''

print(dp[l])