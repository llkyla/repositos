# 87389

def solution(n):

    d = []
    
    for i in range(1, int((n - 1) ** 0.5)+1):
        if ((n - 1) % i) == 0:
            d.append(i)
            if ((i ** 2) != (n - 1)):
                d.append((n-1) // i)
                
    d.remove(1)
    
    return min(d)