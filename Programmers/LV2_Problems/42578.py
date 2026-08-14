# 42578
# 17'58"
'''
clothes	                                                                                    return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	            3
'''
from collections import Counter
from math import prod

def solution(clothes):

    type_count = Counter(type for c, type in clothes)
    #print(type_count)
    res = prod(v+1 for v in type_count.values())
        
    return res - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))