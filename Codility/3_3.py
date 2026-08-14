##

def solution(A):
    # Implement your solution here
    tot = sum(A)
    left = 0

    for i in range(len(A)-1):
        left += A[i]
    print(left)

print(solution([3, 1, 2, 4, 3]))