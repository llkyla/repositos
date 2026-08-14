##

def solution(A):
    # Implement your solution here
    num_set = set(A)
    n = len(A)

    for i in range(1, n+2):
        if i not in num_set:
            return i
    

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))