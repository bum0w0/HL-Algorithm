import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split()) # n = 4, m = 5
board = [list(input().strip()) for _ in range(n)] # board = [['-', '|', '|', '-'], ['-', '|', '|', '-'], ['-', '-', '-', '-'], ['|', '|', '|', '|']]

visited = [[False] * m for _ in range(n)] # 방문 체크용 2차원 리스트 (처음엔 모든 칸이 False, 미방문)

def dfs(x, y, tile):
    visited[x][y] = True # 현재 위치 방문 처리
    # tile : 현재 칸
    if tile == '-':
        # 가로 방향 처리 : 오른쪽 칸이 범위 안에 있고, 아직 방문하지 않았고, 같은 - 모양이면 → 오른쪽으로 DFS 계속 진행
        ny = y + 1
        if ny < m and board[x][ny] == '-' and not visited[x][ny]: # 어느 조각에 이미 포함되어 처리됐을 경우를 가려내기 위함 
            dfs(x, ny, tile)
    else:  # '|'
        # 세로 방향 처리 : 아래쪽 칸이 범위 안에 있고, 아직 방문하지 않았고, 같은 | 모양이면 → 아래로 DFS 계속 진행
        nx = x + 1
        if nx < n and board[nx][y] == '|' and not visited[nx][y]:
            dfs(nx, y, tile)

count = 0
# 2중 루프로 전체 판자를 순회
for i in range(n):
    for j in range(m):
        if not visited[i][j]: # 어느 조각에 이미 포함되어 처리됐을 경우를 가려내기 위함  
            dfs(i, j, board[i][j]) 
            count += 1

print(count)