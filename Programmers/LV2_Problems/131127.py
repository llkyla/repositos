# 131127

'''
want	                    number	        discount	                        result
["banana", "apple", "rice", 
"pork", "pot"]	            [3, 2, 2, 2, 1]	["chicken", "apple", "apple",       3
                                            "banana", "rice", "apple", "pork", 
                                            "banana", "pork", "rice", "pot", 
                                            "banana", "apple", "banana"]

["apple"]	                [10]	        ["banana", "banana", "banana",      0
                                            "banana", "banana", "banana", 
                                            "banana", "banana", "banana", 
                                            "banana"]	
'''
from collections import Counter
def solution(want, number, discount):
    res = 0
    need = dict(zip(want, number))
    
    window = Counter(discount[:10])

    if all(window[w] >= need[w] for w in need):
        res += 1

    for i in range(1, len(discount)-9):
        window[discount[i-1]] -= 1
        window[discount[i+9]] += 1
        if all(window[w] >= need[w] for w in need):
            res += 1

    return res

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple","banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	))