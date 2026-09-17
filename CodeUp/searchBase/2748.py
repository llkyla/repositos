# 2748

m = int(input())
n = int(input())
nums = list(map(int, input().split()))

dp = {0:1} # sum = 0, method to make sum = 1

for x in nums:
    new_dp = {}

    for tot, cnt in dp.items():
        new_dp[tot + x] = new_dp.get(tot + x, 0) + cnt
        new_dp[tot - x] = new_dp.get(tot - x, 0) + cnt

    dp = new_dp

print(dp.get(m, 0))




'''
def f(i, tot):
    if i == n:
        if tot == m:
            return 1
        return 0

    cnt = 0

    cnt += f(i+1, tot + nums[i])
    cnt -= f(i+1, tot - nums[i])

    return cnt

print(f(0,0))
'''