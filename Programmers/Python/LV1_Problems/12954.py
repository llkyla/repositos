# 12954

def solution(x, n):
    ans = []
    a = 1
    while a < (n + 1):
        ans.append(x*a)
        a += 1
        if a == (n + 1):
            break
    
    return ans

# or
def solution1(x, n):
    return [i * x + x for i in range(n)] # list comprehension