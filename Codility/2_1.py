##
def solution(A, K):
    n = len(A)
    if n == 0:
        return A
    K = K % n
    return A[n-K:] + A[:n-K]

print(solution([1, 2, 3, 4], 4))