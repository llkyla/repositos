##

def solution(A):
    # Implement your solution here
    tot_sum = 0
    for i in range(1, max(A)+1):
        tot_sum += i
    return 1 if tot_sum == sum(A) else 0

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))