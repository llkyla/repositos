# 12934

def solution(n):
    
    m = n ** (1/2)
    
    if ((m * 10) % 10) == 0:
        return int((m + 1) ** 2)
    
    else:
        return -1
    
# not using math sqrt but ** 0.5