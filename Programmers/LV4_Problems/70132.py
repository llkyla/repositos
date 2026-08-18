# 70132

'''
t	                                    result
[[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]]	7
[[2,5],[2,0],[3,2],[4,2],[2,1]]	        4
'''

from collections import defaultdict

def solution(t):
    N = len(t) + 1
    graph = defaultdict(list)
    for v1, v2 in t:
        graph[v1].append(v2)
        graph[v2].append(v1)

    depth = [1] * N
    sub_tree = [1] * N
    parent = [-1] * N
    order = []

    visited = [False] * N
    stack = [0]
    visited[0] = True
    while stack:
        node = stack.pop()
        order.append(node)
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = node
                stack.append(nxt)

    for node in reversed(order):
        children = [c for c in graph[node] if c != parent[node]]
        if not children:
            continue

        depths = sorted(((depth[c], c) for c in children), reverse=True)
        subs = sorted(((sub_tree[c], c) for c in children), reverse=True)

        depth[node] = depths[0][0] + 1

        if len(subs) >= 2:
            if subs[0][1] != depths[0][1]:
                sub_tree[node] = subs[0][0] + depths[0][0] + 1
            else:
                sub_tree[node] = max(
                    subs[0][0] + depths[1][0] + 1,
                    subs[1][0] + depths[0][0] + 1,
                )
        else:
            sub_tree[node] = subs[0][0] + 1

    height = [0] * N
    height[0] = 1
    answer = 1

    for node in order:
        children = [c for c in graph[node] if c != parent[node]]
        subs = sorted(((sub_tree[c], c) for c in children), reverse=True)
        depths = sorted(((depth[c], c) for c in children), reverse=True)

        for c in children:
            next_height = height[node] + 1
            if depths and depths[0][1] != c:
                next_height = max(next_height, depths[0][0] + 2)
            elif len(depths) >= 2 and depths[0][1] == c:
                next_height = max(next_height, depths[1][0] + 2)
            height[c] = next_height

        if len(subs) >= 3:
            answer = max(
                answer,
                subs[0][0] + subs[1][0] + height[node],
                subs[0][0] + subs[2][0] + depths[1][0] + 1,
                subs[0][0] + subs[1][0] + depths[2][0] + 1,
            )
        elif len(subs) == 2:
            answer = max(answer, subs[0][0] + subs[1][0] + height[node])
        elif len(subs) == 1:
            answer = max(answer, subs[0][0] + height[node])
        else:
            answer = max(answer, height[node])

    return answer

print(solution([[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]]))