# 12933

def solution(n):
    ans = 0
    
    l = list(map(int, str(n)))
    l.sort(reverse=True)
    
    for x in l:
        ans = ans * 10 + x
    
    return ans

# or
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls)) # int() at the very last to be less expensive
