from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

bfs(0, 0)

print(board[N - 1][M - 1])  