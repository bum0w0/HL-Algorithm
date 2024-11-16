def solution(park, routes):
    # 공원의 크기
    n, m = len(park), len(park[0])
    
    # 시작 위치 찾기
    for i in range(n):  # 행 
        for j in range(m):  # 열 
            if park[i][j] == 'S':  # 'S'를 찾으면
                x, y = i, j  # 시작 위치 저장 (0, 1)
                break

    # 방향 정의
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    
    # 경로 처리
    for route in routes:
        dir, dist = route.split()  # 방향, 거리
        dist = int(dist)
        
        # 임시 위치 저장
        temp_x, temp_y = x, y
        
        # dist만큼 이동 시도
        for _ in range(dist):

            # 임시 좌표를 저장할 변수 (이동이 가능한지 후에 검사하고 실제 위치를 갱신하지 않을수도 있으므로 사용하는 것)
            nx, ny = temp_x + directions[dir][0], temp_y + directions[dir][1]
            
            # 새로운 좌표 계산 전에 유효성 검사
            if not (0 <= nx < n and 0 <= ny < m) or park[nx][ny] == 'X':
                break  # # 조건문이 거짓이면, 이동이 유효하지 않으면 현재 좌표가 갱신되지 않음 (이동 x)
            temp_x, temp_y = nx, ny  # 유효하다면 임시 좌표를 이동이 제대로 완료된 좌표로 간주
            
        # 중단된 이동을 포함한 좌표가 갱신될 수 있으므로 else를 사용하여 break 없이 반복문이 끝났을 때만 실제 위치를 갱신하도록 함    
        else:
            x, y = temp_x, temp_y
    
    return [x, y]