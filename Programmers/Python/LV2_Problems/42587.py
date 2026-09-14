# 42587

from collections import deque
def solution(priorities, location):
    q = deque((priority, i) for i , priority in enumerate(priorities))
    res = 0

    while q:
        priority, index = q.popleft()

        if any(priority < p for p, _ in q):
            q.append((priority, index))

        else:
            res += 1

            if index == location:
                return res


print(solution([2, 1, 3, 2], 2))