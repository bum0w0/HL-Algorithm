def solution(park, routes):
    # 공원의 크기
    n, m = len(park), len(park[0])
    
    # 시작 위치 찾기
    for i in range(n):  # 행 (y)
        for j in range(m):  # 열 (x)
            if park[i][j] == 'S':  # 'S'를 찾으면
                x, y = j, i  # x는 열, y는 행
                break
        else:
            continue
        break  # 첫 번째로 'S'를 찾으면 반복문 종료

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
            # 새로운 좌표 계산 전에 유효성 검사
            nx, ny = temp_x + directions[dir][1], temp_y + directions[dir][0]
            
            if not (0 <= nx < m and 0 <= ny < n) or park[ny][nx] == 'X':
                break  # 유효하지 않으면 현재 명령 무효
            temp_x, temp_y = nx, ny  # 임시 위치 갱신
            
        else:
            # 모든 이동이 유효한 경우에만 실제 위치 갱신
            x, y = temp_x, temp_y
    
    return [y, x]

