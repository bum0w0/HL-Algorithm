import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(node):
    for i in graph[node]: # 인접한 노드 중에서
        if visited[i] == 0: # 방문한 적이 없다면
            visited[i] = node # 해당 노드를 부모 노드로
            dfs(i)

dfs(1)

for i in range(2, n + 1):
    print(visited[i])