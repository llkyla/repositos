# 138476
# greedy

'''
k	tangerine	                result
6	[1, 3, 2, 5, 4, 5, 2, 3]	3
4	[1, 3, 2, 5, 4, 5, 2, 3]	2
2	[1, 1, 1, 1, 2, 2, 2, 3]	1
'''

# sort()
'''
[1, 3, 2, 5, 4, 5, 2, 3]
[1, 2, 2, 3, 3, 4, 5, 5]

'''
def solution(k, tangerine):
    
    counts = {}
    for size in tangerine:
        '''
        if size in counts:
            counts[size] += 1
        else:
            counts[size] = 1
        '''
        counts[size] = counts.get(size, 0) + 1
    # counts = {1: 1, 3: 2, 2: 2, 5: 2, 4: 1}

    sorted_counts = sorted(counts.values(), reverse=True) # from the largest val
    # sorted_counts = [2, 2, 2, 1, 1]

    ans = 0
    for cnt in sorted_counts:
        if k <= 0:
            break
        k -= cnt
        ans += 1

    return ans

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))

# or
from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    sorted_counts = sorted(counts.values(), reverse=True)
    
    answer = 0
    for cnt in sorted_counts:
        if k <= 0:
            break
        k -= cnt
        answer += 1
    
    return answer