# 12914

'''
n	result
4	5
3	3
'''
def solution(n): # Fibonacci
    a, b = 1, 2
    if n == 1:
        return 1
    for _ in range(n - 2):
        a, b = b, (a + b) % 1234567
        
    return b