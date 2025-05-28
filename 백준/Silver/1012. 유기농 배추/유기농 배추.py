import sys
sys.setrecursionlimit(10**6)

# 테스트 케이스 개수
T = int(input())

# 상, 하, 좌, 우 이동 좌표
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    graph[y][x] = 0  # 방문 처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())     # M(가로 길이), N(세로 길이), K(배추가 심어진 개수) 입력 받기
    graph = [[0] * M for _ in range(N)]     # N x M 크기의 2차원 리스트(graph) 0으로 초기화

    # K개의 배추가 심어진 좌표(graph[y][x])를 1로 설정 
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1

    print(count)
