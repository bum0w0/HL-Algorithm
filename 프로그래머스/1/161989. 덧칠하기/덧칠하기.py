def solution(n, m, section):
    
    count = 0  
    current_end = 0
    
    for start in section:
        if start > current_end:
            count += 1
            current_end = start + m - 1  # 덧칠한 범위 업데이트
    
    return count