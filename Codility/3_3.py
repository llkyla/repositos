##

def solution(A):
    # Implement your solution here
    tot = sum(A)
    left = 0
    min_diff = float('inf')

    for i in range(len(A)-1):
        left += A[i]
        right = tot - left
        diff = abs(left - right)
        min_diff = min(min_diff, diff)

    return min_diff

print(solution([3, 1, 2, 4, 3]))