board = [list(map(str, input().split())) for _ in range(5)]  # 5x5 숫자판 입력
result = set()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, depth, current_num):
    if depth == 6:
        result.add(current_num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, depth + 1, current_num + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, board[i][j])

print(len(result))
