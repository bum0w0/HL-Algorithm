import sys
sys.setrecursionlimit(100000)
    
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

# 모눈종이에 직사각형 좌표 입력 및 색칠
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split()) # 0 2 4 4
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1 # 영역 개수와 넓이를 구하는 문제이므로 좌표계가 바뀌더라도 상관 없지만 필요 시에는 graph[M-1-y][x]로 뒤집어서 저장하면 됨

visited = [[False] * N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[y][x] = True
    area = 1 # 방문 처리와 동시에 해당 영역을 채움
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and graph[ny][nx] == 0:
            area += dfs(nx, ny) # 영역의 넓이를 구하기 위해 area 변수에 누적
    return area

areas = []

for y in range(M):
    for x in range(N):
        if not visited[y][x] and graph[y][x] == 0:
            areas.append(dfs(x, y))

areas.sort()

print(len(areas))
print(" ".join(map(str, areas)))