##

def solution(A):
    # Implement your solution here
    n = len(A)
    min_idx = 0
    min_avg = (A[0] + A[1]) / 2.0 # arbitrary avg

    for i in range(n-1):
        avg2 = (A[i] + A[i+1]) / 2.0
        if avg2 < min_avg:
            min_avg = avg2
            min_idx = i
        if i < n-2:
            avg3 = (A[i] + A[i+1] + A[i+2]) / 3.0
            if avg3 < min_avg:
                min_avg = avg3
                min_idx = i
    return min_idx

print(solution([4, 2, 2, 5, 1, 5, 8]))