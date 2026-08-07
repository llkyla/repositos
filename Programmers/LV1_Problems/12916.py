# 12916

def solution(s):

    t = s.lower()
    
    p = t.count('p')
    y = t.count('y')
    
    if p == y:
        return True
    else:
        return False