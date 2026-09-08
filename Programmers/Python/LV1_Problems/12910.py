# 12910

def solution(arr, divisor):
    ans = []
    
    for a in arr:
        if a % divisor == 0:
            ans.append(a)
            ans.sort()
    
    if len(ans) == 0:
        return [-1]
    else:
        return ans