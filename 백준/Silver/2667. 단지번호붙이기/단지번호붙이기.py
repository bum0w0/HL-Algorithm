import sys
sys.setrecursionlimit(100000)

N = int(input()) # N=7

graph = [list(map(int, input().strip())) for _ in range(N)] 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * N for _ in range(N)]
cluster_sizes = []

def dfs(x, y):
    visited[x][y] = True
    count = 1 # 집 개수

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1):
            count += dfs(nx, ny)
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            cluster_sizes.append(dfs(i, j)) # 각 단지에 집 개수 추가

print(len(cluster_sizes))  
for size in sorted(cluster_sizes):
    print(size)