# 17680

from collections import deque

def solution(cacheSize, cities):
    q = deque()
    cnt = 0

    
    for c in cities:
        c = c.lower()

        if c in q:
            cnt += 1
            q.remove(c)
            q.append(c)

        else:
            cnt += 5

            if len(q) == cacheSize:
                if cacheSize > 0:
                    q.popleft()
            if cacheSize > 0:
                q.append(c)

    return cnt

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))