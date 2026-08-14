##

def solution(A):
    # Implement your solution here
    N = len(A)
    tot = (N+1)*(N+2) // 2
    return tot - sum(A)
    
print(solution([2,3,1,5]))