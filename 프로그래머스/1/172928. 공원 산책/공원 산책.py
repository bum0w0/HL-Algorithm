def solution(park, routes):
    # 공원의 크기
    n, m = len(park), len(park[0])
    
    # 시작 위치 찾기
    for row in range(n):  # 행
        for col in range(m):  # 열
            if park[row][col] == 'S':  # 'S'를 찾으면
                current_row, current_col = row, col  # 시작 위치 저장 (0, 1)
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
        direction, distance = route.split()  # 방향과 거리 분리
        distance = int(distance)
        
        # 거리 이동이 완료된 좌표를 저장할 변수
        temp_row, temp_col = current_row, current_col
        
        # 거리만큼 이동 시도
        for _ in range(distance):
            # 임시 좌표를 저장할 변수 (이동이 가능한지 후에 검사하고 실제 위치를 갱신하지 않을수도 있으므로 사용하는 것)
            next_row = temp_row + directions[direction][0]
            next_col = temp_col + directions[direction][1]
            
            # 이동 전 유효성 검사
            if not (0 <= next_row < n and 0 <= next_col < m) or park[next_row][next_col] == 'X':
                break  # 조건문이 거짓이면, 이동이 유효하지 않으면 현재 좌표가 갱신되지 않음 (이동 x)
            temp_row, temp_col = next_row, next_col  # 유효하다면 임시 좌표를 이동이 제대로 완료된 좌표로 간주
            
        # 중단된 이동을 포함한 좌표가 갱신될 수 있으므로 else를 사용하여 break 없이 반복문이 끝났을 때만 실제 위치를 갱신하도록 함
        else:
            current_row, current_col = temp_row, temp_col

    return [current_row, current_col]

# 로봇 강아지가 명령을 수행하는 동안 공원을 넘어가거나 장애물이 있다면 해당 명령을 무시함.
# 시작위치가 [0,0] 이고 동쪽으로 2칸, 남쪽으로 2칸 이동한다면 [0,0] -> [0,2] -> [2,2]
