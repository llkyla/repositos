# 87946
# 26'11"

'''
k	dungeons	                result
80	[[80,20],[50,40],[30,10]]	3
'''
from itertools import permutations
def solution(k, dungeons):
    res = 0
    for order in permutations(range(len(dungeons))):
        cur_k = k
        cnt = 0
        for i in order:
            need, least = dungeons[i]
            if cur_k >= need:
                cur_k -= least
                cnt += 1
            else:
                break
        res = max(res, cnt)

    return res

print(solution(80,[[80,20],[50,40],[30,10]]))