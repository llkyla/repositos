# 42747

'''
citations	        return
[3, 0, 6, 1, 5]	    3
'''

def solution(citations):
    citations.sort(reverse=True)
    res = 0

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            res = i + 1

    return res

print(solution([3, 0, 6, 1, 5]))

# or
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    # enumerate(citations, start=1) := (1, 6), (2, 5), (3, 3), (4, 1), (5, 0)
    # map(min, enumerate(citations, start=1)) := min(1, 6) = 1
    #                                            min(2, 5) = 2
    #                                            min(3, 3) = 3
    #                                            min(4, 1) = 1
    #                                            min(5, 0) = 0

    return answer