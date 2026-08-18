# 43165

'''
numbers	            target	return
[1, 1, 1, 1, 1]	    3	    5
[4, 1, 2, 1]	    4	    2
'''

def solution(numbers, target):

    def add(cnt, sums):
        # BASE CASE
        if cnt == len(numbers): # using all elements in numbers
            if sums == target:
                return 1
            else:
                return 0
            
        return ((add(cnt + 1, sums + numbers[cnt])) + (add(cnt + 1, sums - numbers[cnt])))

    return add(0,0)

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))