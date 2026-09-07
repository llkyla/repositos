##

def solution(A):
    # Implement your solution here
    n = len(A)
    if len(set(A)) != n: # after changing in to set, len diff = ∃ repeated element
        return 0
    if max(A) != n: # max(A) = len guarantees permutation after checking repeated ones 
        return 0
    return 1

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))