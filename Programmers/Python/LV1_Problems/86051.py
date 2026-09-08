# 86051

def solution(numbers):
    
    numl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    miss = []
    
    for n in numl:
        if n not in numbers:
            miss.append(n)
            
    return sum(miss)

# or
def solution(numbers):
    return 45 - sum(numbers)