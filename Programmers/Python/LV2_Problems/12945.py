# 12945

# DP
def solution(n):
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 1234567 # calculate right first and store in left

    return a