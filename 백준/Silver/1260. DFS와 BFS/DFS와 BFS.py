import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(neighbor)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end= ' ')

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)