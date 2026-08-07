# 12932

def solution(n):
    answer = []
    n = str(n)
    for i in range(1, len(n)+1):
        
        answer += n[-i]
    
    return list(map(int, answer))

# or
def digit_reverse(n):
    return list(map(int, reversed(str(n)))) # reversed(str(n)) to int()