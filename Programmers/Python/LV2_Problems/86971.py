# 86971

def solution(n, wires):
    answer = n

    for a, b in wires:

        graph = [[] for _ in range(n + 1)]

        for x, y in wires:
            if (x, y) == (a, b):
                continue

            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * (n + 1)

        def dfs(node):
            visited[node] = True
            count = 1

            for next_node in graph[node]:
                if not visited[next_node]:
                    count += dfs(next_node)

            return count

        group1 = dfs(1)
        group2 = n - group1

        answer = min(answer, abs(group1 - group2))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))