# 49994

def solution(dirs):
    x, y = 0, 0
    visited = set()

    move ={
        "U":(0,1),
        "D":(0,-1),
        "L":(-1,0),
        "R":(1,0)
    }

    for d in dirs:
        dx, dy = move[d]

        nx = x + dx
        ny = y + dy

        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        road = tuple(sorted([(x, y), (nx, ny)]))

        if road not in visited:
            visited.add(road)

        x, y = nx, ny

    return len(visited)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))