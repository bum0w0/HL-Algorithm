import sys
sys.setrecursionlimit(100000)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
rainfall = set()

rainfall.add(0) # 아무 지역도 물에 잠기지 않는 경우

for i in graph:
    for j in i:
        rainfall.add(j)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, rain, visited):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > rain):
            dfs(nx, ny, rain, visited)

result = 0

for rain in rainfall:
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > rain:
                dfs(i, j, rain, visited)
                count += 1
    result = max(result, count) # 안전 영역 개수가 가장 많을 때

print(result)