##

def solution(X, A):
    # Implement your solution here
    covered = set()

    for time, pos in enumerate(A):
        if pos <= X:
            covered.add(pos)
        if len(covered) == X:
            return time
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))