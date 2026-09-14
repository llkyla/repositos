# 42626

# runtime error
'''
def solution(scoville, K):

    scoville.sort()
    cnt = 0

    while scoville[0] < K:
        a = scoville.pop(0)
        b = scoville.pop(0)

        new = a + b * 2

        scoville.append(new)
        scoville.sort()

        cnt += 1

    return cnt
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0

    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a + b * 2)
        count += 1

    if scoville and scoville[0] >= K:
        return count

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))

'''
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
'''