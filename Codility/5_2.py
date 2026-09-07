##

def solution(A, B, K):
    # Implement your solution here
    # cnt = 0
    # for n in range(A, B+1):
    #     if n % K == 0:
    #         cnt += 1
    # return cnt

    return B // K - (A - 1) // K

print(solution(6, 11, 2))