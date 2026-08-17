# 132265

'''
topping	                    result
[1, 2, 1, 3, 1, 4, 1, 2]	2
[1, 2, 3, 1, 4]	            0
'''
from collections import Counter
def solution(topping):
    res = 0
    left = set()
    right = Counter(topping) # Counter({1: 4, 2: 2, 3: 1, 4: 1})

    for t in topping:
        right[t] -= 1
        # print(right)
        if right[t] == 0: # if no more such topping left:
            del right[t] # delete from the dict so that len(right) can have num of sort of toppings
        left.add(t)
        if len(left) == len(right):
            res += 1
    
    return res
    #pass

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))