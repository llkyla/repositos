# 3002

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
question = list(map(int, input().split()))

for i, n in enumerate(nums):
    if nums[i] in question:
        print(i)
    else:
        print(-1)

