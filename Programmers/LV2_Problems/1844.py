# 1844_not importing

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

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited = [[False] * m for _ in range(n)] # visited = True vice versa
    distance = [[0] * m for _ in range(n)] # count num of map went thru
    # Base:
    visited[0][0] = True
    distance[0][0] = 1

    q = [(0,0)] # gonna visit pos
    head = 0 # how many elements we went

    while head < len(q): # while there still left elements to visit:
        x, y = q[head]
        head += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    result = distance[n-1][m-1]
    return result if result != 0 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))