def solution(sequence, k):
    answer = [0, 0]
    left, right = 0, 0  
    current_sum = 0  
    min_length = float('inf')  # 최소 구간 길이를 추적

    for right in range(len(sequence)):  # 오른쪽 포인터 이동
        current_sum += sequence[right]  # 현재 값을 더함

        # 현재 합이 k보다 크다면 왼쪽 포인터 이동
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1

        # 합이 정확히 k인 경우
        if current_sum == k:
            # 더 짧은 구간이거나, 시작 인덱스가 더 앞서는 경우 갱신
            if min_length > right - left:
                min_length = right - left
                answer = [left, right]

    return answer