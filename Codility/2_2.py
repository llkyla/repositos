##
from collections import Counter
def solution(A):
    # Implement your solution here
    cnt = Counter(A)
    for x in A:
        if cnt[x] % 2 == 1:
            return x
    
print(solution([9, 3, 9, 3, 9, 7, 9]))