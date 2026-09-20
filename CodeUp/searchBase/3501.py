# 3501

n = int(input())

cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)] # row = house num; col = colour

# 1st house
dp[0][0] = cost[0][0] # ith red
dp[0][1] = cost[0][1] # ith green
dp[0][2] = cost[0][2] # ith blue

# 2nd house
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))