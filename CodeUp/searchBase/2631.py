# 2631

n, k = map(int, input().split()) # 5 7
nums = list(map(int, input().split())) # [1,2,3,4,5]

cnt = 0
left = 0
tot = 0

for right in range(n):
    tot += nums[right]

    while tot >= k:
        if tot == k:
            cnt += 1

        tot -= nums[left]
        left += 1


print(cnt)
