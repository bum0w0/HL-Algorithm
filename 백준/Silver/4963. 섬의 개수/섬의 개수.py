import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    graph[y][x] = 0 
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    # 5 4
    # [1, 1, 1, 1]
    # [0, 0, 0, 0]
    # [1, 0, 1, 0]
    # [0, 0, 0, 1]
    # [0, 0, 1, 0]

    count = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1
    
    print(count)