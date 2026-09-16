# 2633

n, k = map(int, input().split())
nums = list(map(int, input().split()))

for i, num in enumerate(nums):
    if num >= k:
        print(i + 1)
        break
else:
    print(n + 1)