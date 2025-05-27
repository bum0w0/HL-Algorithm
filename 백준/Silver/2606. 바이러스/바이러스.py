n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

def dfs(node):
    global count
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += 1
            dfs(neighbor)

dfs(1)
print(count)