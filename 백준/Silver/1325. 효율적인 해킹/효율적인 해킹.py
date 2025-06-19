import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # b -> a (a가 b를 해킹할 수 있음)

def dfs_stack(start):
    stack = [start]
    visited = [False] * (N + 1)
    visited[start] = True
    count = 1

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count += 1
    return count

result = [0] * (N + 1)

result = [dfs_stack(i) for i in range(1, N+1)]
_max = max(result)

for i in range(N):
    if result[i] == _max:
        print(i+1, end=' ')