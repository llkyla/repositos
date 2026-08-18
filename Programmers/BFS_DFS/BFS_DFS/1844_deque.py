# 1844_deque ver

'''
maps	        answer
[[1,0,1,1,1],   11
 [1,0,1,0,1],
 [1,0,1,1,1],
 [1,1,1,0,1],
 [0,0,0,0,1]]

[[1,0,1,1,1],   -1
 [1,0,1,0,1],
 [1,0,1,1,1],
 [1,1,1,0,0],
 [0,0,0,0,1]]	
'''

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    distx = [-1,1,0,0]
    disty = [0,0,-1,1]

    visited = {(0,0)}
    q = deque([(0,0,1)])

    while q:
        x, y, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx, ny = x + distx[i], y + disty[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))