##

def solution(A):
    N = len(A)
    min_avg = (A[0] + A[1]) / 2.0 # arbitrary
    min_pos = 0

    for P in range(N - 1):
        avg2 = (A[P] + A[P + 1]) / 2.0
        if avg2 < min_avg:
            min_avg = avg2
            min_pos = P

        if P < N - 2:
            avg3 = (A[P] + A[P + 1] + A[P + 2]) / 3.0
            if avg3 < min_avg:
                min_avg = avg3
                min_pos = P

    return min_pos

print(solution([4, 2, 2, 5, 1, 5, 8]))